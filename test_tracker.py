import unittest
from tracker import Tracker
from battery_simulated import Battery


class TestTracker(unittest.TestCase):

    # GETTERS & SETTERS #

    #unittest for the set_range method
    def test_set_range(self):
        t = Tracker(Battery())
        t.set_range(36)
        self.assertEqual(t.range, 36)
        t.set_range(65)
        self.assertEqual(t.range, 65)
    # END test_set_range

    # unittest for the get_range method
    def test_get_range(self):
        t = Tracker(Battery())
        self.assertEqual(t.get_range(), 65)
        t.set_range(72)
        self.assertEqual(t.get_range(), 72)
    # END test_get_range

    # unittest for the set_bypass method
    def test_set_bypass(self):
        t = Tracker(Battery())
        self.assertEqual(t.get_mode(), "Auto")
        self.assertEqual(t.flag_bypass, 0)
        t.set_bypass()
        self.assertEqual(t.get_mode(), "Bypass")
        self.assertEqual(t.flag_bypass, 1)
    # END test_set_bypass

    # unittest for the set_auto method
    def test_set_auto(self):
        t = Tracker(Battery())
        t.set_bypass()
        self.assertEqual(t.flag_bypass, 1)
        self.assertEqual(t.get_mode(), "Bypass")
        t.set_auto()
        self.assertEqual(t.get_mode(), "Auto")
        self.assertEqual(t.flag_bypass, 0)
    # END test_set_auto

    # unittest for the get_mode method
    def test_get_mode(self):
        t = Tracker(Battery())
        self.assertEqual(t.get_mode(), "Auto")
        self.assertEqual(t.flag_bypass, 0)
        t.set_bypass()
        self.assertEqual(t.get_mode(), "Bypass")
        self.assertEqual(t.flag_bypass, 1)
        t.set_auto()
        self.assertEqual(t.get_mode(), "Auto")
        self.assertEqual(t.flag_bypass, 0)
    # END test_get_mode



    # MAIN METHODS #

    # unittest for the exit method
    def test_exit(self):
        t = Tracker(Battery())
        self.assertEqual(t.flag_bypass, 0)
        t.exit()
        self.assertEqual(t.flag_bypass, 1)
    # END test_exit

    # unittest for the _reset_discharging_timer method
    def test_reset_discharging_timer(self):
        t = Tracker(Battery())
        t._reset_discharging_timer(100)
        self.assertEqual(t.discharging_time, 0)
    # END test_reset_discharging_timer

if __name__ == '__main__':
    unittest.main()
# ENDIF