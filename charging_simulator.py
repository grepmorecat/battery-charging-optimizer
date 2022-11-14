import datetime
import time
from random import randint, uniform

'''
gerSampling function generates reports of the battery
we assume the current battery level is 100%
function runs in a infinite loop
there are 4 condition in total 2 to check the battery level for charging and discharging
and another 2 to check to see if the battery has reached its max range and one for min range
stores the data in a list and a counter iterates through the list to get every report
time.sleep(1) makes sure that each report is generated 1second apart
'''
def getSampling():
    batteryLevel = 100
    maxRange = 80
    minRange = 20
    states = ("Charging", "Discharging")
    battery = []
    counter = 0
    while (True):
        if (batteryLevel <= minRange):
            condition1 = True
            while (condition1 == True):
                now1 = datetime.datetime.now()
                info = ([batteryLevel, states[0], now1.strftime("%H:%M:%S")])
                battery.append(info)
                print("Battery Percentage: %i, State: %s, Time: %s" % (battery[counter][0], battery[counter][1], battery[counter][2]))
                counter += 1
                batteryLevel += randint(1, 3)
                #batteryLevel += uniform(.01, .05)
                time.sleep(1)
                if (batteryLevel >= maxRange):
                    condition1 = False
        if (batteryLevel >= minRange):
            condition2 = True
            while (condition2 == True):
                now = datetime.datetime.now()
                info = ([batteryLevel, states[1], now.strftime("%H:%M:%S")])
                battery.append(info)
                print("Battery Percentage: %i, State: %s, Time: %s" % (battery[counter][0], battery[counter][1], battery[counter][2]))
                counter += 1
                batteryLevel -= randint(1, 3)
                #batteryLevel += uniform(.01, .05)
                time.sleep(1)
                if (batteryLevel <= minRange):
                    condition2 = False
    return

if __name__ == "__main__":
    getSampling()