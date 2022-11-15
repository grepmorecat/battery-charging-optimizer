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

        with open("history.json") as history_file:
            history = json.load(history_file)


        if history["previous_discharging_time"]:
            self.previous_discharging_time = history["previous_discharging_time"]
        else:
            self.previous_discharging_time = None

        if (time.time() - history["timestamp"] <= 604800):
            self.range = history["range"]
        else:
            self.range = self.default_range
            # print("range reset to 60, due to timestamp expired")
            # keep range if history is in 7 days, but restart calculating discharging_time
            # otherwise, reset policy to default

        self.range_remain = self.range
        self.discharging_time = 0

    def is_discharging(self) -> bool:
        return True if self.current_state == "Discharging" else False

    def write_history(self):
        """
        write current status into history.json file on disk
        """
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
        """
        sample the current battery status, and do calculation based on condition
        """
        previous_time = self.timestamp
        previous_level = self.current_level
        self.current_level, self.current_state, self.timestamp = self.battery.get_info()
        # update
        if self.is_discharging():
            self.range_remain -= previous_level - self.current_level
            self.discharging_time += self.timestamp - previous_time
        # if remain_range reaches zero, recalculate range
        if self.range_remain <= 0:
            if self.discharging_time < self.previous_discharging_time * 0.9:
                self.range = self.range + 5 if self.range + 5 <= 100 else 100
            elif self.discharging_time > self.previous_discharging_time * 1.1:
                self.range = self.range - 5 if self.range - 5 >= 50 else 50
            # reset discharging_time, range_remain
            self.previous_discharging_time = self.discharging_time
            self.discharging_time = 0
            self.range_remain = self.range

    def _tracking(self, interval: int):
        while 1:
            self.update()
            time.sleep(interval)

    def _saving_history(self, interval: int):
        while 1:
            self.write_history()
            time.sleep(interval)

    def start_tracking(self, interval: int):
        """
        create thread for tracking battery info
        :param: interval:int
        """
        Thread(target=self._tracking, args=(interval,)).start()

    def start_saving_history(self, interval: int):
        """
        create thread for saving history to file
        :param: interval:int
        """
        Thread(target=self._saving_history, args=(interval,)).start()




if __name__ == "__main__":
    t = Tracking(Battery())
    t.write_history()
    t.start_tracking(1)
    t.start_saving_history(10)
