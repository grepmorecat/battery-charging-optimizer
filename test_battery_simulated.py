import unittest
from battery_simulated import Battery

class TestBattery(unittest.TestCase):
    #testing the getters and setters

    # unittest for the getLevel method
    # the method should return the current level of the battery
    def test_getLevel(self):
        b = Battery()
        b._setLevel(50)
        self.assertEqual(b.getLevel(), 50)
    # END test_getLevel

    # unittest for the _setLevel method
    # the method should set the level of the battery
    def test_setLevel(self):
        b = Battery()
        b._setLevel(50)
        self.assertEqual(b.getLevel(), 50)
        b._setLevel(0)
        self.assertEqual(b.getLevel(), 0)
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
    def test_getState(self):
        b = Battery()
        self.assertEqual(b.getState(), "Discharging")
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




if __name__ == '__main__':
    unittest.main(exit=False)