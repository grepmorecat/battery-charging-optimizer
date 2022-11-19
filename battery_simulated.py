# import datetime
import time
from random import randint, uniform, random
import threading
# import sqlite3
# import keyboard

class Battery():
    def __init__(self, range=60):
        self.level = None
        self.time = None
        self.state = None
        self.keyboard = None
        self.range = range
        self.lowerThreshold = None
        self.upperThreshold = None
        backgroundProcess = threading.Thread(target=self.samplingSimulator)
        backgroundProcess.start()

    def __str__(self):
        batteryInfo = "Battery Level: {0}, Battery State: {1}, Time: {2}"
        return batteryInfo.format(self.level, self.state, self.time)

    def set_upperThreshold(self, threshold):
        self.upperThreshold = threshold
        return

    def set_lowerThreshold(self, threshold):
        self.lowerThreshold = threshold
        return
    def charge(self, states, upperThreshold):
        global batteryLevel
        global counter
        condition1 = True
        while (condition1 == True):
            if (counter == 85600):
                exit()
            self._setLevel(batteryLevel)
            self._setState(states)
            self._setTime(time.time())
            counter += 1
            charge = randint(1, 2)
            batteryLevel += charge
            time.sleep(1)
            if (batteryLevel >= upperThreshold):
                condition1 = False
        return

    def discharge(self, states, lowerThreshold):
        global batteryLevel
        global counter
        condition2 = True
        while (condition2 == True):
            if (counter == 85600):
                exit()
            counter += 1
            self._setLevel(batteryLevel)
            self._setState(states)
            self._setTime(time.time())
            discharge = randint(1, 2)
            batteryLevel -= discharge
            time.sleep(1)
            if (batteryLevel <= lowerThreshold):
                condition2 = False
        return

    def notCharging(self, states):
        global batteryLevel
        global counter
        if (counter == 85600):
            exit()
        condition = True
        while (condition == True):
            self.level = batteryLevel
            self.state = states
            self.time = time.time()
            counter += 1
        return

    def samplingSimulator(self):
        global batteryLevel
        global counter
        batteryLevel = 80
        self.upperThreshold = 100 - ((100 - self.range) / 2)
        self.lowerThreshold = (100 - self.range) / 2
        states = ("Charging", "Not Charging", "Discharging")
        counter = 0
        while (True):
            if (counter == 85600):
                exit()
            if (self.keyboard == True):
                if (self.getLevel >= 80):
                    self.notCharging(states[1])
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

    def setkeyboard(self, k):
        self.keyboard = k


if __name__ == "__main__":
    s = Battery()
    while (True):
        e = s.get_info()
        print(e)
        time.sleep(1)
