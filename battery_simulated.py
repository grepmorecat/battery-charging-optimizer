import time
from random import randint
import threading
import sys

class Battery():
    '''
    batterySimulator class simulates a real battery (for PC or non-linux users since our program runs with linux OS)
    '''

    def __init__(self):
        '''
        self._level - battery level
        self._time - the time
        self._state - state of the battery (Charging, Not Charging, Discharging)
        self._upperThreshold - highest percentage before discharging
        self._lowerThreshold - lowest percentage before discharging
        self._stop - condition to stop infinite loops
        self._pluggedIn - condition to simulate the laptop being plugged in for charging
        self._workload - amount of battery power needed to execute programs running on laptop
        '''
        self._level = 0
        self._time = None
        self._state = None
        self._lowerThreshold = None
        self._upperThreshold = None
        self._stop = 0
        self._workload = 4
        self._pluggedIn = False
        '''begin a threading process'''
        backgroundProcess = threading.Thread(target=self.samplingSimulator)
        backgroundProcess.start()

    def __str__(self):
        '''method prints out the simulated battery's level, state and the time(in enpoch)'''
        batteryInfo = "Battery Level: {0}, Battery State: {1}, Time: {2}"
        return batteryInfo.format(self._level, self._state, self._time)

    def samplingSimulator(self):
        '''
        method contains the simulator
        firstly we set the batterylevel to 80%(since this is a simulator we assume that is what the battery level starts at when first called)
        upperThreshold and lowerThresold are calculated based on what the range is specified to be(for our starting point it will be 60%)
        batteryLevel and counter are set to global so they can get accessed and modified by other methods
        counter is set to 0 (and will end after 86400 interations)
        infinite loop checks to see if the battery needs to be charged or discharged based on what batteryLevel
        '''
        global batteryLevel
        global counter
        batteryLevel = 65
        # self._upperThreshold = 100 - ((100 - self._range) / 2)
        # self._lowerThreshold = (100 - self.range) / 2
        states = ("Charging", "Not Charging", "Discharging")
        counter = 0
        self._lowerThreshold = 20
        self._upperThreshold = 65
        while (True):
            if (self._stop == 1):
                sys.exit()
            if (counter == 86400):
                break
            if (self._level >= 80 and self._pluggedIn == True):
                self.setInfo(batteryLevel, states[1])
                self.notCharging(states[1])
            elif (batteryLevel <= self._lowerThreshold or self._pluggedIn == True):
                self.setInfo(batteryLevel, states[0])
                self.charge(states[0], self._upperThreshold)
            elif (batteryLevel >= self._lowerThreshold and self._pluggedIn == False):
                self.setInfo(batteryLevel, states[2])
                self.discharge(states[2], self._lowerThreshold)
        return

    def charge(self, state, upperThreshold):
        '''
        method simulates a battery charging
        starts by entering an infinite loop with a nested condition
        if battery has hit 80% or above then quit inifnite loop or if counter hits 86400 also quit or if self._stop is set
        otherwise increase counter, batterylevel and set level, state, time
        '''
        global batteryLevel
        global counter
        self.setPluggedIn(True)
        while (True):
            if (self._stop == 1):
                sys.exit()
            counter += 1
            # charge = randint(1, 2)
            charge = randint(1, 5)
            if (self._pluggedIn == False):
                self.setInfo(int(batteryLevel), state)
                time.sleep(0.5)
                break
            if (counter == 86400 or batteryLevel + charge >= upperThreshold):
                batteryLevel = self._upperThreshold
                self.setInfo(int(batteryLevel), state)
                time.sleep(0.5)
                break
            else:
                batteryLevel += charge
                self.setInfo(int(batteryLevel), state)
            time.sleep(0.5)
        return

    def discharge(self, state, lowerThreshold):
        '''
        method simulates a battery discharging
        starts by entering an infinite loop with a nested condition
        if battery has hit 20% or below then quit inifnite loop or if counter hits 86400 also quit or if self._stop is set
        otherwise increase counter, decrease batterylevel and set level, state, time
        '''
        global batteryLevel
        global counter
        while (True):
            if (self._stop == 1):
                sys.exit()
            counter += 1
            # discharge = randint(1, 2)
            discharge = self._workload
            if (counter == 86400 or self._pluggedIn == True):
                self.setInfo(int(batteryLevel), state)
                time.sleep(0.5)
                break
            if (batteryLevel - discharge <= lowerThreshold):
                batteryLevel = self._lowerThreshold
                self.setInfo(int(batteryLevel), state)
                time.sleep(0.5)
                break
            else:
                batteryLevel -= discharge
                self.setInfo(int(batteryLevel), state)
            time.sleep(0.5)
        return

    def notCharging(self, state):
        '''
        method simulates a battery not charging
        starts by entering an infinite loop with a condition
        if counter hits 86400 also quit or if self._stop is set
        otherwise increase counter and set level, state, time
        '''
        global batteryLevel
        global counter
        while (True):
            if (self._stop == 1):
                sys.exit()
            if (counter == 86400 or self._pluggedIn == False):
                break
            counter += 1
            batteryLevel = self._upperThreshold
            self.setInfo(int(batteryLevel), state)
            time.sleep(0.5)
        return

    def setInfo(self, level, state):
        '''method called by other methods in the class to set the level, state and time'''
        self._level = level
        self._state = state
        self._time = time.time()

    '''getters and setters'''

    def get_info(self):
        return (self._level, self._state, self._time)

    '''Battery Levels'''

    def getLevel(self):
        return self._level

    def _setLevel(self, level):
        self._level = level

    '''Battery states'''

    def getState(self):
        return self._state

    def _setState(self, state):
        self._state = state

    '''Time'''

    def getTime(self):
        return self._time

    def _setTime(self, time):
        self._time = time

    '''Flag to stop loops'''

    def stop(self):
        self._stop = 1

    '''Thresholds(or Range)'''

    def getUpperThreshold(self):
        return self._upperThreshold

    def setUpperThreshold(self, threshold):
        '''method sets the max upper threshold a battery can charge up to'''
        self._upperThreshold = threshold

    def getLowerThreshold(self):
        return self._lowerThreshold

    def setLowerThreshold(self, threshold):
        '''sets the max lower threshold that a battery can discharge to'''
        self._lowerThreshold = threshold

    '''workload'''

    def getWorkload(self):
        return self._workload

    def setWorkload(self, percentage):
        self._workload = percentage

    '''set laptop to be plugged in'''

    def getPluggedIn(self):
        return self._pluggedIn

    def setPluggedIn(self, pluggedIn):
        '''simulates if a battery is plugged in'''
        self._pluggedIn = pluggedIn

if __name__ == "__main__":
    s = Battery()
    s.setPluggedIn(True)
    while (True):
        e = s.get_info()
        print(e)
        time.sleep(0.1)


