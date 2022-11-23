import unittest
from graph import Graph
from battery_simulated import Battery
from tracker import Tracker


"""
This class is used to test the graph class
It has 3 methods and none of them can be tested
The only method i thought i could plausibly test was the toggle_mode method
but it is not possible to test because it is a method that is called by a button press event
"""

class TestGraph(unittest.TestCase):

    # unittest for the _toggle_mode method
    """def test_toggle_mode(self):
        g = Graph(Battery(), Tracker(Battery()))
        self.assertEqual(g._toggle_mode(), "Auto")
        g._toggle_mode(button)
        self.assertEqual(g._toggle_mode(), "Bypass")"""



if __name__ == '__main__':
    unittest.main()
# ENDIF