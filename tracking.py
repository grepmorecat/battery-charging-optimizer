from battery import Battery
import json
import time
from threading import Thread

# TODO how to exit elegantly?
class Tracking:
    """
    for tracking sampled data, calculating range,
    storing data to history.json file
    """
    default_range = 60

    def __init__(self, battery: Battery):
        self.battery = battery
        self.current_level, self.current_state, self.timestamp = self.battery.get_info()
        self.range = None
        self.range_remain = None
        self.discharging_time = None
        self.previous_discharging_time = None

        with open("history_demo.json") as history_file:
            history = json.load(history_file)

        self.previous_discharging_time = history["previous_discharging_time"] if history[
            "previous_discharging_time"] else None  # if no valid previous discharging time, will be None

        self.range = history["range"] if time.time() - history["timestamp"] <= 604800 else self.default_range
        # keep range if history is in 7 days, but restart calculating discharging_time
        # otherwise, reset policy to default
        self.range_remain = self.range
        self.discharging_time = 0

    def write_history(self):
        # TODO check validate?
        d = {
            "timestamp": self.timestamp,
            "range": self.range,
            "previous_discharging_time": self.previous_discharging_time
        }
        j = json.dumps(d, indent=2)
        with open("history.json", "w") as outfile:
            outfile.write(j)
    def update(self):
        self.current_level, self.current_state, self.timestamp = self.battery.get_info()
        # TODO calc

    def _tracking(self, interval:int):
        while 1:
            self.update()
            # TODO calc

            time.sleep(interval)

    def _saving_history(self, interval:int):
        while 1:
            self.write_history()
            time.sleep(interval)

    def start_tracking(self, interval:int):
        """
        create thread for tracking battery info
        :param: interval:int
        """
        Thread(target=self._tracking, args=(interval,)).start()

    def start_saving_history(self, interval:int):
        """
        create thread for saving history to file
        :param: interval:int
        """
        Thread(target=self._saving_history, args=(interval,)).start()

    #
    # def track(self):
    #     if self.battery.get_state_str() == "Discharging":
    #         self.discharging_time += 1
    #         self.range_remain -= 0.01
    #     elif self.battery.get_state_str() == "Charging":
    #         self.charging_time += 1
    #         self.range_remain += 0.01
    #     else:
    #         pass
    #
    #     print("Discharging time: ", self.discharging_time)
    #     print("Charging time: ", self.charging_time)
    #     print("Range remain: ", self.range_remain)
    #     print("Battery level: ", self.battery.get_level())
    #     print("Battery ratioed level: ", self.battery.get_ratioed_level())
    #     print("Battery state: ", self.battery.get_state_str())
    #     print("Battery state code: ", self.battery.get_state_code())

    # def get_discharging_time(self):
    #     return self.discharging_time
    #
    # def get_charging_time(self):
    #     return self.charging_time
    #
    # def get_range_remain(self):
    #     return self.range_remain
    #
    # def get_battery_level(self):
    #     return self.battery.get_level()
    #
    # def get_battery_ratioed_level(self):
    #     return self.battery.get_ratioed_level()
    #
    # def get_battery_state_str(self):
    #     return self.battery.get_state_str()
    #
    # def get_battery_state_code(self):
    #     return self.battery.get_state_code()
    #
    # def reset(self):
    #     self.discharging_time = 0
    #     self.charging_time = 0
    #     self.range_remain = self.battery.range


if __name__ == "__main__":
    t = Tracking(Battery())
    t.write_history()
    t.start_tracking(1)
    t.start_saving_history(2)