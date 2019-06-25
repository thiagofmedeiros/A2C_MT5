import numpy as np


class Observation:
    def __init__(self, string_data):
        comma_position = string_data.find(";")
        self.month = int(string_data[0:comma_position])/12
        string_data = string_data[comma_position + 1:]

        comma_position = string_data.find(";")
        self.day = int(string_data[0:comma_position])/31
        string_data = string_data[comma_position + 1:]

        comma_position = string_data.find(";")
        self.monday = int(string_data[0:comma_position])
        string_data = string_data[comma_position + 1:]

        comma_position = string_data.find(";")
        self.tuesday = int(string_data[0:comma_position])
        string_data = string_data[comma_position + 1:]

        comma_position = string_data.find(";")
        self.wednesday = int(string_data[0:comma_position])
        string_data = string_data[comma_position + 1:]

        comma_position = string_data.find(";")
        self.thursday = int(string_data[0:comma_position])
        string_data = string_data[comma_position + 1:]

        comma_position = string_data.find(";")
        self.friday = int(string_data[0:comma_position])
        string_data = string_data[comma_position + 1:]

        comma_position = string_data.find(";")
        self.hour = int(string_data[0:comma_position])/24
        string_data = string_data[comma_position + 1:]

        comma_position = string_data.find(";")
        self.minute = int(string_data[0:comma_position])/60
        string_data = string_data[comma_position + 1:]

        comma_position = string_data.find(";")
        self.positionNothing = int(string_data[0:comma_position])
        string_data = string_data[comma_position + 1:]

        comma_position = string_data.find(";")
        self.positionBought = int(string_data[0:comma_position])
        string_data = string_data[comma_position + 1:]

        comma_position = string_data.find(";")
        self.positionSold = int(string_data[0:comma_position])
        string_data = string_data[comma_position + 1:]

        comma_position = string_data.find(";")
        self.operationPoints = int(string_data[0:comma_position])/10000
        string_data = string_data[comma_position + 1:]

        comma_position = string_data.find(";")
        self.lastValue = int(string_data[0:comma_position])/200000
        string_data = string_data[comma_position + 1:]

        comma_position = string_data.find(";")
        self.lastRealVolume = int(string_data[0:comma_position])/100000
        string_data = string_data[comma_position + 1:]

        comma_position = string_data.find(";")
        self.lastTickVolume = int(string_data[0:comma_position])/100000
        string_data = string_data[comma_position + 1:]

        self.M1_open = np.zeros(15)
        self.M1_high = np.zeros(15)
        self.M1_low = np.zeros(15)
        self.M1_close = np.zeros(15)
        self.M1_real_volume = np.zeros(15)
        self.M1_tick_volume = np.zeros(15)

        for i in range(0, 15):
            comma_position = string_data.find(";")
            self.M1_open[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.M1_high[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.M1_low[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.M1_close[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.M1_real_volume[i] = int(string_data[0:comma_position])/100000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.M1_tick_volume[i] = int(string_data[0:comma_position])/100000
            string_data = string_data[comma_position + 1:]

        self.M5_open = np.zeros(15)
        self.M5_high = np.zeros(15)
        self.M5_low = np.zeros(15)
        self.M5_close = np.zeros(15)
        self.M5_real_volume = np.zeros(15)
        self.M5_tick_volume = np.zeros(15)

        for i in range(0, 15):
            comma_position = string_data.find(";")
            self.M5_open[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.M5_high[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.M5_low[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.M5_close[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.M5_real_volume[i] = int(string_data[0:comma_position])/500000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.M5_tick_volume[i] = int(string_data[0:comma_position])/500000
            string_data = string_data[comma_position + 1:]

        self.M15_open = np.zeros(15)
        self.M15_high = np.zeros(15)
        self.M15_low = np.zeros(15)
        self.M15_close = np.zeros(15)
        self.M15_real_volume = np.zeros(15)
        self.M15_tick_volume = np.zeros(15)

        for i in range(0, 15):
            comma_position = string_data.find(";")
            self.M15_open[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.M15_high[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.M15_low[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.M15_close[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.M15_real_volume[i] = int(string_data[0:comma_position])/1500000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.M15_tick_volume[i] = int(string_data[0:comma_position])/1500000
            string_data = string_data[comma_position + 1:]

        self.M30_open = np.zeros(15)
        self.M30_high = np.zeros(15)
        self.M30_low = np.zeros(15)
        self.M30_close = np.zeros(15)
        self.M30_real_volume = np.zeros(15)
        self.M30_tick_volume = np.zeros(15)

        for i in range(0, 15):
            comma_position = string_data.find(";")
            self.M30_open[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.M30_high[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.M30_low[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.M30_close[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.M30_real_volume[i] = int(string_data[0:comma_position])/3000000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.M30_tick_volume[i] = int(string_data[0:comma_position])/3000000
            string_data = string_data[comma_position + 1:]

        self.H1_open = np.zeros(15)
        self.H1_high = np.zeros(15)
        self.H1_low = np.zeros(15)
        self.H1_close = np.zeros(15)
        self.H1_real_volume = np.zeros(15)
        self.H1_tick_volume = np.zeros(15)

        for i in range(0, 15):
            comma_position = string_data.find(";")
            self.H1_open[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.H1_high[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.H1_low[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.H1_close[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.H1_real_volume[i] = int(string_data[0:comma_position])/6000000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.H1_tick_volume[i] = int(string_data[0:comma_position])/6000000
            string_data = string_data[comma_position + 1:]

        self.D1_open = np.zeros(15)
        self.D1_high = np.zeros(15)
        self.D1_low = np.zeros(15)
        self.D1_close = np.zeros(15)
        self.D1_real_volume = np.zeros(15)
        self.D1_tick_volume = np.zeros(15)

        for i in range(0, 15):
            comma_position = string_data.find(";")
            self.D1_open[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.D1_high[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.D1_low[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.D1_close[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.D1_real_volume[i] = int(string_data[0:comma_position])/(24*6000000)
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.D1_tick_volume[i] = int(string_data[0:comma_position])/(24*6000000)
            string_data = string_data[comma_position + 1:]

        self.W1_open = np.zeros(15)
        self.W1_high = np.zeros(15)
        self.W1_low = np.zeros(15)
        self.W1_close = np.zeros(15)
        self.W1_real_volume = np.zeros(15)
        self.W1_tick_volume = np.zeros(15)

        for i in range(0, 15):
            comma_position = string_data.find(";")
            self.W1_open[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.W1_high[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.W1_low[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.W1_close[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.W1_real_volume[i] = int(string_data[0:comma_position])/(7*24*6000000)
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.W1_tick_volume[i] = int(string_data[0:comma_position])/(7*24*6000000)
            string_data = string_data[comma_position + 1:]

        self.MN1_open = np.zeros(15)
        self.MN1_high = np.zeros(15)
        self.MN1_low = np.zeros(15)
        self.MN1_close = np.zeros(15)
        self.MN1_real_volume = np.zeros(15)
        self.MN1_tick_volume = np.zeros(15)

        for i in range(0, 12):
            comma_position = string_data.find(";")
            self.MN1_open[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.MN1_high[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.MN1_low[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.MN1_close[i] = int(string_data[0:comma_position])/200000
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.MN1_real_volume[i] = int(string_data[0:comma_position])/(30*24*6000000)
            string_data = string_data[comma_position + 1:]

            comma_position = string_data.find(";")
            self.MN1_tick_volume[i] = int(string_data[0:comma_position])/(30*24*6000000)
            string_data = string_data[comma_position + 1:]

        comma_position = string_data.find(";")
        self.reward = int(string_data[0:comma_position]) / 10000
