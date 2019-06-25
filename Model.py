import numpy as np
import tensorflow as tf


class Model(tf.keras.Model):
    def __init__(self, num_actions):
        super(Model, self).__init__()

        self.dense1 = tf.keras.layers.Dense(4096, activation='relu')
        self.dense2 = tf.keras.layers.Dense(2048, activation='relu')
        self.dense3 = tf.keras.layers.Dense(1024, activation='relu')
        self.dense4 = tf.keras.layers.Dense(512, activation='relu')
        self.dense5 = tf.keras.layers.Dense(256, activation='relu')
        self.hidden1 = tf.keras.layers.Dense(128, activation='relu')
        self.hidden2 = tf.keras.layers.Dense(128, activation='relu')
        self.value = tf.keras.layers.Dense(1, name='value')
        # logits are unnormalized log probabilities
        self.logits = tf.keras.layers.Dense(num_actions, activation='softmax', name='policy_logits')

    def call(self, inputs):
        x = tf.convert_to_tensor(inputs)
        dense1 = self.dense1(x)
        dense2 = self.dense2(dense1)
        dense3 = self.dense3(dense2)
        dense4 = self.dense4(dense3)
        dense5 = self.dense5(dense4)

        # separate into logits and val
        hidden_logs = self.hidden1(dense5)
        hidden_vals = self.hidden2(dense5)
        return self.logits(hidden_logs), self.value(hidden_vals)

    def action_value(self, obs):
        # executes call() under the hood
        logits, value = self.predict(obs)

        action = tf.random.categorical(logits, 1)

        return np.squeeze(action, axis=-1), np.squeeze(value, axis=-1)
