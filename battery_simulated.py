import datetime
import time
from random import randint, uniform, random
import threading
import sqlite3
import keyboard

'''
gerSampling function generates reports of the battery
we assume the current battery level is 80%
function runs in a infinite loop
there are 4 condition in total 2 to check the battery level for charging and discharging
and another 2 to check to see if the battery has reached its max range and one for min range
stores the data in a list and a counter iterates through the list to get every report
time.sleep(1) makes sure that each report is generated 1second apart
'''


class getSampling():
    def __init__(self, range):
        self.level = None
        self.state = None
        self.time = None
        self.state = None
        self.keyboard = None
        self.range = range
        backgroundProcess = threading.Thread(target=self.samplingSimulator)
        backgroundProcess.start()

    def __str__(self):
        batteryInfo = "Battery Level: {0}, Battery State: {1}, Time: {2}"
        return batteryInfo.format(self.level, self.state, self.time)

    def charge(self, states, maxRange):
        global batteryLevel
        global counter
        condition1 = True
        while (condition1 == True):
            if (counter == 85600):
                # if (counter <= 0)
                return
            self._setLevel(batteryLevel)
            self._setState(states)
            self._setTime(time.time())
            counter += 1
            '''charge = uniform(.01, .05)'''
            charge = randint(1, 2)
            batteryLevel += charge
            time.sleep(1)
            if (batteryLevel >= maxRange):
                condition1 = False
        return

    def discharge(self, states, minRange):
        global batteryLevel
        global counter
        condition2 = True
        while (condition2 == True):
            if (counter == 85600):
                # if (counter <= 0)
                return
            counter += 1
            self._setLevel(batteryLevel)
            self._setState(states)
            self._setTime(time.time())
            # discharge = uniform(.01, .05)
            discharge = randint(1, 2)
            batteryLevel -= discharge
            # counter -= discharge
            time.sleep(1)
            if (batteryLevel <= minRange):
                condition2 = False
        return

    def notCharging(self, states):
        global batteryLevel
        global counter
        if (counter == 85600):
            return
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
        maxRange = 100 - ((100 - self.range) / 2)
        minRange = (100 - self.range) / 2
        # range = maxRange - minRange
        states = ("Charging", "Not Charging", "Discharging")
        counter = 0
        # counter = range
        while (True):
            '''
            laptop should be plugged in for the state "Not Charging" 
            to simulate this im rolling a number between 0 and 2 for the state
            '''
            if (counter == 85600):
                return
            if (self.keyboard == True):
                if (self.getLevel >= 80):
                    self.notCharging(states[1])
            if (batteryLevel <= minRange):
                self.charge(states[0], maxRange)
            if (batteryLevel >= minRange):
                self.discharge(states[2], minRange)
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
    defaultRange = 60
    s = getSampling(defaultRange)
    while (True):
        pluggedIn = False
        if keyboard.is_pressed(" "):
            pluggedIn = True
        if pluggedIn == True:
            s.setkeyboard(True)
        else:
            s.setkeyboard(False)
        e = s.get_info()
        print(e)
        time.sleep(1)