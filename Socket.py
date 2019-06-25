import socket
from Observation import *


class Socket:
    def __init__(self, host, receive_port, send_port):
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.orig = (host, receive_port)
        self.dest = (host, send_port)
        self.udp.bind(self.orig)

        print('binded')

    def process(self, string_data):
        obs = Observation(string_data)

        s = np.array([obs.month, obs.day, obs.monday, obs.tuesday, obs.wednesday, obs.thursday, obs.friday, obs.hour,
                      obs.minute, obs.positionNothing, obs.positionBought, obs.positionSold, obs.operationPoints,
                      obs.lastValue, obs.lastRealVolume, obs.lastTickVolume])

        for i in range(0, 15):
            candles = np.array([obs.M1_open[i], obs.M1_high[i], obs.M1_low[i], obs.M1_close[i], obs.M1_real_volume[i],
                               obs.M1_tick_volume[i], obs.M5_open[i], obs.M5_high[i], obs.M5_low[i], obs.M5_close[i],
                               obs.M5_real_volume[i], obs.M5_tick_volume[i], obs.M15_open[i], obs.M15_high[i],
                               obs.M15_low[i], obs.M15_close[i], obs.M15_real_volume[i], obs.M15_tick_volume[i],
                               obs.M30_open[i], obs.M30_high[i], obs.M30_low[i], obs.M30_close[i],
                               obs.M30_real_volume[i], obs.M30_tick_volume[i], obs.H1_open[i], obs.H1_high[i],
                               obs.H1_low[i], obs.H1_close[i], obs.H1_real_volume[i], obs.H1_tick_volume[i],
                               obs.D1_open[i], obs.D1_high[i], obs.D1_low[i], obs.D1_close[i], obs.D1_real_volume[i],
                               obs.D1_tick_volume[i], obs.W1_open[i], obs.W1_high[i], obs.W1_low[i], obs.W1_close[i],
                               obs.W1_real_volume[i], obs.W1_tick_volume[i]])

            s = np.concatenate((s, candles))

        for i in range(0, 12):
            candles = np.array([obs.MN1_open[i], obs.MN1_high[i], obs.MN1_low[i], obs.MN1_close[i],
                                obs.MN1_real_volume[i], obs.MN1_tick_volume[i]])

            s = np.concatenate((s, candles))

        return s, obs.reward
