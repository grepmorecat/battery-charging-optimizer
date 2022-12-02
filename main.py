from battery_simulated import Battery
from tracker import Tracker
from interface import Interface

if __name__ == "__main__":
    battery = Battery()
    tracker = Tracker(battery)
    interface = Interface(battery, tracker)
    battery.stop()
    tracker.exit()