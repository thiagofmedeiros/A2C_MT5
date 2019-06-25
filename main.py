import gym
import matplotlib.pyplot as plt
from Model import *
from A2CAgent import *

logging.getLogger().setLevel(logging.INFO)

NOTHING = 0
BUY     = 1
SELL    = 2

HOST = '127.0.0.1'
PORT = 8085
sendPORT = 8087

actions = [NOTHING, BUY, SELL]

model = Model(num_actions=len(actions))
agent = A2CAgent(model)

agent.train()