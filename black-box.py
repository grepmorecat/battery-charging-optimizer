import time
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
        self._notPluggedOut - if the laptop is still plugged in
        '''

        """
        These values are hardcoded for the purpose of black-box testing
        """
        self._states = ("Charging", "Not Charging", "Discharging")
        self._level = 22
        self._time = None
        self._state = "Charging"
        self._lowerThreshold = 34
        self._upperThreshold = 65
        self._stop = 0
        self._charge = 4
        self._workload = 12
        self._pluggedIn = False
        self._notPluggedOut = False
        self._counter = 0
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
        firstly we set the self._level to 65%(since this is a simulator we assume that is what the battery level starts at when first called)
        upperThreshold and lowerThresold are predetermined for this simulator
        self._level and self._counter are set to global so they can get accessed and modified by other methods
        self._counter is set to 0 (and will end after 86400 interations)
        infinite loop checks to see if the battery needs to be charged or discharged or in Not Charging state based on self._level and pluggedIn conditions
        '''
        self._counter = 0
        while (True):
            if (self._stop == 1):
                sys.exit()
            if (self._counter == 86400):
                break
            if (self._level >= self._upperThreshold and self._pluggedIn == True):
                self.setInfo(self._level, self._states[1])
                self.notCharging(self._states[1])
            elif (self._level <= self._lowerThreshold or self._pluggedIn == True):
                self.setInfo(self._level, self._states[0])
                self.charge(self._states[0], self._upperThreshold)
            elif (self._level >= self._lowerThreshold and self._pluggedIn == False):
                self.setInfo(self._level, self._states[2])
                self.discharge(self._states[2], self._lowerThreshold)
        return

    def charge(self, state, upperThreshold):
        '''
        method simulates a battery charging
        starts by entering an infinite loop with conditions to break infinite loop
        first condition stop the whole program
        second condition if laptop not plugged in break loop as it cant be charged
        third condition if battery has hits the threshold or above then quit inifnite loop or if self._counter hits 86400 set info and then break loop
                         else set info and continue loop
        '''
        self.setPluggedIn(True)
        while (True):
            if (self._stop == 1):
                sys.exit()
            self._counter += 1
            if (self._pluggedIn == False):
                self.setInfo(int(self._level), state)
                time.sleep(0.5)
                break
            if (self._counter == 86400 or self._level + self._charge >= upperThreshold):
                if (self._level <= upperThreshold):
                    self._level = self._upperThreshold
                self.setInfo(int(self._level), state)
                time.sleep(0.5)
                self.setPluggedIn(False)
                break
            else:
                self._level += self._charge
                self.setInfo(int(self._level), state)
            time.sleep(0.5)
        return

    def discharge(self, state, lowerThreshold):
        '''
        method simulates a battery discharging
        starts by entering an infinite loop with conditions to break the loop
        first condition stop the whole program
        second condition if laptop not plugged out, set notPluggedOut to true and break loop as battery cannot be discharged when plugged in
        third condition if battery has hits the lower threshold or above then quit inifnite loop or if self._counter hits 86400 set info and then break loop
                         else set info and continue loop
        NOTE: for the third condition we are to assume the lower threshold is when the user plugs in their laptop for charging
        '''
        while (True):
            if (self._stop == 1):
                sys.exit()
            self._counter += 1
            discharge = self._workload
            if (self._notPluggedOut == True):
                self.setPluggedIn(True)
                break
            if (self._counter == 86400 or self._pluggedIn == True):
                self.setInfo(int(self._level), state)
                time.sleep(0.5)
                break
            if (self._level - discharge <= lowerThreshold):
                self._level = self._lowerThreshold
                self.setInfo(int(self._level), state)
                time.sleep(0.5)
                break
            else:
                self._level -= discharge
                self.setInfo(int(self._level), state)
            time.sleep(0.5)
        return

    def notCharging(self, state):
        '''
        method simulates a battery not charging
        starts by entering an infinite loop with conditions to break the loop
        first condition stop the whole program
        second condition if laptop not plugged in or if self._counter hits 86400 break loop as it cannot be in Not Charging State without being plugged in
        third condition if not plugged out then set info
                        else set info and break infinite loop
        '''
        while (True):
            if (self._stop == 1):
                sys.exit()
            if (self._counter == 86400 or self._pluggedIn == False):
                break
            self._counter += 1
            if (self._notPluggedOut == True):
                if (self._level >= self._upperThreshold):
                    self.setInfo(int(self._level), state)
                    time.sleep(0.5)
                else:
                    self._level = self._upperThreshold
            else:
                self._level = self._upperThreshold
                self.setInfo(int(self._level), state)
                time.sleep(0.5)
                break
        return

    '''getters and setters'''
    def setInfo(self, level, state):
        '''method called by other methods in the class to set the level, state and time'''
        self._level = level
        self._state = state
        self._time = time.time()

    def get_info(self):
        return (self._level, self._state, self._time)

    '''Battery Levels'''
    def getLevel(self):
        return self._level

    def _setLevel(self, level):
        self._level = level

    '''Battery self._states'''
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
        self._upperThreshold = int(threshold)

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

    def setNotPluggedOut(self, pluggedOut):
        '''Charger is still plugged in or out depending on True or False statements'''
        self._notPluggedOut = pluggedOut

if __name__ == "__main__":
    s = Battery()
    s.setPluggedIn(True)
    while (True):
        e = s.get_info()
        print(e)
        time.sleep(0.6)