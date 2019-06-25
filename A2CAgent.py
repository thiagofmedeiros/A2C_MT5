import numpy as np
import logging
import tensorflow as tf
from Socket import *

NOTHING = 0
BUY     = 1
SELL    = 2

HOST = '127.0.0.1'     # Endereco IP do Servidor
receivePORT = 8085            # Porta que o Servidor esta
sendPORT = 8087        # Porta que o Servidor esta

# TODO: implement Experience buffer


class A2CAgent:
    def __init__(self, model):
        # hyperparameters for loss terms, gamma is the discount coefficient
        self.step = 0

        self.socket = Socket(HOST, receivePORT, sendPORT)

        self.params = {
            'gamma': 0.99,
            'value': 0.5,
            'entropy': 0.0001
        }
        self.model = model
        self.model.load_weights('./checkpoints/my_checkpoint')
        self.model.compile(
            optimizer=tf.keras.optimizers.RMSprop(lr=0.0007),
            # define separate losses for policy logits and value estimate
            loss=[self._logits_loss, self._value_loss]
        )

    def train(self, batch_sz=240):
        # storage helpers for a single batch of data
        actions = np.empty((batch_sz,), dtype=np.int32)
        rewards, values = np.empty((2, batch_sz))
        observations = np.empty((batch_sz,) + (718,))

        points = []

        while True:
            msg, client = self.socket.udp.recvfrom(8192)

            string_data = msg.decode('utf-8')

            if len(string_data) > 15:
                next_obs, reward = self.socket.process(string_data)

                rewards[self.step] = reward

                observations[self.step] = next_obs.copy()
                actions[self.step], values[self.step] = self.model.action_value(next_obs[None, :])

                if actions[self.step] == BUY:
                    msg = "BUY"
                    self.socket.udp.sendto(msg.encode('utf-8'), self.socket.dest)

                elif actions[self.step] == SELL:
                    msg = "SELL"
                    self.socket.udp.sendto(msg.encode('utf-8'), self.socket.dest)

                self.step += 1

                if self.step >= batch_sz:
                    self.step = 0
                    _, next_value = self.model.action_value(next_obs[None, :])

                    returns, advs = self._returns_advantages(rewards, values, next_value)

                    acts_and_advs = np.concatenate([actions[:, None], advs[:, None]], axis=-1)

                    print("Training")

                    losses = self.model.train_on_batch(observations, [acts_and_advs, returns])

                    print("Training finished")

                    logging.info("Losses: %s ", losses)

                    self.model.save_weights('./checkpoints/my_checkpoint')

    def _returns_advantages(self, rewards, values, next_value):
        # next_value is the bootstrap value estimate of a future state (the critic)
        returns = np.append(np.zeros_like(rewards), next_value, axis=-1)
        # returns are calculated as discounted sum of future rewards
        for t in reversed(range(rewards.shape[0])):
            returns[t] = rewards[t] + self.params['gamma'] * returns[t + 1]
        returns = returns[:-1]
        # advantages are returns - baseline, value estimates in our case
        advantages = returns - values
        return returns, advantages

    def _value_loss(self, returns, value):
        # value loss is typically MSE between value estimates and returns
        return self.params['value'] * tf.keras.losses.mean_squared_error(returns, value)

    def _logits_loss(self, acts_and_advs, logits):
        # a trick to input actions and advantages through same API
        actions, advantages = tf.split(acts_and_advs, 2, axis=-1)
        # sparse categorical CE loss obj that supports sample_weight arg on call()
        # from_logits argument ensures transformation into normalized probabilities
        weighted_sparse_ce = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
        # policy loss is defined by policy gradients, weighted by advantages
        # note: we only calculate the loss on the actions we've actually taken
        actions = tf.cast(actions, tf.int32)
        policy_loss = weighted_sparse_ce(actions, logits, sample_weight=advantages)
        # entropy loss can be calculated via CE over itself
        entropy_loss = tf.keras.losses.categorical_crossentropy(logits, logits, from_logits=True)
        # here signs are flipped because optimizer minimizes
        return policy_loss - self.params['entropy'] * entropy_loss
