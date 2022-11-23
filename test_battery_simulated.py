import unittest
from battery_simulated import Battery
import time

class TestBattery(unittest.TestCase):

    """
    It's extremely hard to unittest the battery_simulated.py file because it's threaded,
    so we can't really test the methods that are in the thread.
    Methods tested here are mostly getters and setters.
    """

    #GETTERS AND SETTERS

    # unittest for the getLevel method
    # the method should return the current level of the battery
    def test_getLevel(self):
        b = Battery()
        b._setLevel(46)
        self.assertEqual(b.getLevel(), 50)
    # END test_getLevel

    # unittest for the _setLevel method
    # the method should set the level of the battery
    def test_setLevel(self):
        b = Battery()
        b._setLevel(50)
        self.assertEqual(b.getLevel(), 50)
        b._setLevel(0)
        self.assertEqual(b.getLevel(), 2)
    # END test_setLevel


    # unittest for the _setState method
    # the method should set the state of the battery
    # we can assume that the battery state is "Discharging" by default
    def test_setState(self):
        b = Battery()
        b._setState("Charging")
        self.assertEqual(b.getState(), "Charging")
        b._setState("Discharging")
        self.assertEqual(b.getState(), "Discharging")
    # END test_setState

    # unittest for the get_State method
    # the method should return the state of the battery
    # we can assume that the state is "Discharging" by default
    def test_getState(self):
        b = Battery()
        self.assertEqual(b.getState(), "Discharging")
        b._setState("Charging")
        self.assertEqual(b.getState(), "Charging")
    # END test_getState

        
    # unittest for the getTime method
    # the method should return the time of the battery
    def test_getTime(self):
        b = Battery()
        b._setTime(50)
        self.assertEqual(b.getTime(), 50)
    # END test_getTime

    # unittest for the _setTime method
    # the method should set the time of the battery
    def test_setTime(self):
        b = Battery()
        b._setTime(50)
        self.assertEqual(b.getTime(), 50)
        b._setTime(0)
        self.assertEqual(b.getTime(), 0)
    # END test_setTime

    # unnitest for the getPluggedIn method
    # the method should return the pluggedIn of the battery
    # we can assume that the pluggedIn is 0 by default
    def test_getPluggedIn(self):
        b = Battery()
        self.assertEqual(b.getPluggedIn(), 0)
        b.setPluggedIn(1)
        self.assertEqual(b.getPluggedIn(), 1)
    # END test_getPluggedIn

    # unittest for the _setPluggedIn method
    # the method should set the pluggedIn of the battery
    def test_setPluggedIn(self):
        b = Battery()
        b.setPluggedIn(1)
        self.assertEqual(b.getPluggedIn(), 1)
        b.setPluggedIn(0)
        self.assertEqual(b.getPluggedIn(), 0)
    # END test_setPluggedIn

    # unittest for the getWorkload method
    # the method should return the workload of the battery
    # we can assume that the workload is 4 by default
    def test_getWorkload(self):
        b = Battery()
        b.setWorkload(5)
        self.assertEqual(b.getWorkload(), 5)
    # END test_getWorkload

    # unittest for the _setWorkload method
    # the method should set the workload of the battery
    def test_setWorkload(self):
        b = Battery()
        b.setWorkload(3)
        self.assertEqual(b.getWorkload(), 3)
        b.setWorkload(0)
        self.assertEqual(b.getWorkload(), 0)
    # END test_setWorkload

    # unittest for the getUpperThreshold method
    # the method should return the upperThreshold of the battery
    # we can assume that the upperThreshold is 65 by default
    def test_getUpperThreshold(self):
        b = Battery()
        self.assertEqual(b.getUpperThreshold(), 65)
        b.setUpperThreshold(50)
        self.assertEqual(b.getUpperThreshold(), 50)
    # END test_getUpperThreshold

    # unittest for the _setUpperThreshold method
    # the method should set the upperThreshold of the battery
    def test_setUpperThreshold(self):
        b = Battery()
        b.setUpperThreshold(50)
        self.assertEqual(b.getUpperThreshold(), 50)
        b.setUpperThreshold(0)
        self.assertEqual(b.getUpperThreshold(), 0)
    # END test_setUpperThreshold

    # unittest for the getLowerThreshold method
    # the method should return the lowerThreshold of the battery
    # we can assume that the lowerThreshold is 20 by default
    def test_getLowerThreshold(self):
        b = Battery()
        self.assertEqual(b.getLowerThreshold(), 20)
        b.setUpperThreshold(50)
        self.assertEqual(b.getUpperThreshold(), 50)
    # END test_getLowerThreshold

    # unittest for the _setLowerThreshold method
    # the method should set the lowerThreshold of the battery
    def test_setLowerThreshold(self):
        b = Battery()
        b.setLowerThreshold(35)
        self.assertEqual(b.getLowerThreshold(), 35)
        b.setLowerThreshold(2)
        self.assertEqual(b.getLowerThreshold(), 2)
    # END test_setLowerThreshold

    # unittest for the setInfo method
    # the method should set the info of the battery
    def test_setInfo(self):
        b = Battery()
        b.setInfo(50, "Charging")
        self.assertEqual(b.get_info(), (50, "Charging", time.time()))
        b.setInfo(0, "Discharging")
        self.assertEqual(b.get_info(), (0, "Discharging", time.time()))
    # END test_setInfo




    # MAIN METHODS #

    # unnitest for the stop method
    # the method should stop the battery simulation
    # we can assume that the battery is not stopped by default therefore default value is None
    def test_stop(self):
        b = Battery()
        self.assertEqual(b.stop(), None)
        b.stop()
        self.assertEqual(b._stop, 1)
    # END test_stop

if __name__ == '__main__':
    unittest.main(exit=False)
# ENDIF