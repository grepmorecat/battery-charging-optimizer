# import datetime
import time
from random import randint, uniform, random
import threading
import sys


# import sqlite3
# import keyboard

class Battery():

    def __init__(self, range=60):
        self.level = None
        self.time = None
        self.state = None
        self.range = range
        self.lowerThreshold = None
        self.upperThreshold = None
        self.flag_exit = 0
        self.workload = 4
        backgroundProcess = threading.Thread(target=self.samplingSimulator)
        backgroundProcess.start()

    def __str__(self):
        batteryInfo = "Battery Level: {0}, Battery State: {1}, Time: {2}"
        return batteryInfo.format(self.level, self.state, self.time)

    def exit(self):
        self.flag_exit = 1
        # pass

    def set_threshold(self, threshold):
        self.set_upperThreshold(threshold)

    def get_threshold(self):
        return self.upperThreshold

    def set_workload(self, i: int):
        self.workload = i

    def set_upperThreshold(self, threshold):
        self.upperThreshold = threshold
        return

    def charge(self, states, upperThreshold):
        # print("max threshold: " + str(upperThreshold))
        global batteryLevel
        condition1 = True
        while (condition1 == True):
            if self.flag_exit:
                sys.exit()
            self._setLevel(batteryLevel)
            self._setState(states)
            self._setTime(time.time())
            charge = randint(6, 10)
            if batteryLevel + charge >= upperThreshold:
                batteryLevel = upperThreshold
                condition1 = False
            else:
                batteryLevel += charge
            time.sleep(0.2)
        return

    def discharge(self, states, lowerThreshold):
        global batteryLevel
        condition2 = True
        while (condition2 == True):
            if self.flag_exit:
                sys.exit()
            self._setLevel(batteryLevel)
            self._setState(states)
            self._setTime(time.time())
            discharge = self.workload
            batteryLevel -= discharge
            time.sleep(0.2)
            if (batteryLevel <= lowerThreshold):
                condition2 = False
        return

    def notCharging(self, states):
        global batteryLevel
        condition = True
        while (condition == True):
            self.level = batteryLevel
            self.state = states
            self.time = time.time()
        return

    def samplingSimulator(self):
        global batteryLevel
        batteryLevel = 80
        # self.upperThreshold = 100 - ((100 - self.range) / 2)
        # self.lowerThreshold = (100 - self.range) / 2
        states = ("Charging", "Not Charging", "Discharging")
        while (not self.flag_exit):
            self.lowerThreshold = 20 + randint(-10, 20)
            # TODO eception if upperThreshold unset
            if (batteryLevel <= self.lowerThreshold):
                self.charge(states[0], self.upperThreshold)
            if (batteryLevel >= self.lowerThreshold):
                self.discharge(states[2], self.lowerThreshold)
        return

    def get_info(self):
        return (int(self.level), self.state, self.time)

    def getLevel(self):
        return self.level

    def _setLevel(self, level):
        self.level = level

    def getState(self):
        return self.state

    def _setState(self, state):
        self.state = state

    def getTime(self):
        return self.time

    def _setTime(self, time):
        self.time = time



if __name__ == "__main__":
    s = Battery()
    while (True):
        e = s.get_info()
        print(e)
        time.sleep(1)
