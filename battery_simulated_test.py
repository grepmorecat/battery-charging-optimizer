import unittest
from battery import Battery

class simulatedBatteryTest(unittest.TestCase):

    def test_print(self):
        result = Battery()
        printStatment = result.__str__()
        self.assertEqual(print(printStatment), "Battery Level: %i, Battery State: %s, Time: %f" % (76, "Discharging", result.getTime()))

if __name__ == "__main__":
    unittest.main()