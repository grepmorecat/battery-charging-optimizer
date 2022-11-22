import unittest
from graph import Graph
from battery_simulated import Battery
from tracker import Tracker

class TestGraph(unittest.TestCase):

    # unittest for the _toggle_mode method
    # the method should change the mode of the tracker
    # we can assume that the tracker is in auto mode by default
    # if the tracker is in auto mode, the mode should change to bypass
    def test_toggle_mode(self):
        g = Graph(Battery(), Tracker(Battery()))
        g._toggle_mode(None)
        self.assertEqual(g.tracker.get_mode(), "Bypass")
        g._toggle_mode(None)
        self.assertEqual(g.tracker.get_mode(), "Auto")



if __name__ == '__main__':
    unittest.main()
# ENDIF