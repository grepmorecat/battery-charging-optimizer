from battery import Battery
import json
import time
from threading import Thread

class Tracker:
    """
    A tracker that keeps sampling the status of a battery object,
    and continuously stores date to history.json file for future use
    """
    default_range = 60

    def __init__(self, battery: Battery):
        """
        Initiate a tracker by providing a battery object which it will track on.
        :param battery: a battery object
        :rtype: a tracker object
        """
        self.battery = battery
        self.current_level, self.current_state, self.timestamp = self.battery.get_info()
        self.range = None
        self.range_remain = None
        self.discharging_time = None
        self.previous_discharging_time = None

        self.flag_exit = 0
        self.flag_bypass = 0

        with open("history.json") as history_file:
            history = json.load(history_file)

        if history["previous_discharging_time"]:
            self.previous_discharging_time = history["previous_discharging_time"]
        else:
            self.previous_discharging_time = None

        if time.time() - history["timestamp"] <= 604800:
            self.range = history["range"]
        else:
            self.range = self.default_range
            # print("range reset to 60, due to timestamp expired")
            # keep range if history is in 7 days, but restart calculating discharging_time
            # otherwise, reset policy to default

        self.range_remain = self.range
        self.discharging_time = 0
        self.set_auto()

    def get_range(self):
        """
        Get the current range set by the tracker.
        :return: integer range.
        """
        return int(self.range) if self.flag_bypass == 0 else 100

    def get_mode(self) -> str:
        """
        Get the current mode of the service.
        :return: string "Bypass" or "Auto"
        """
        return "Bypass" if self.flag_bypass else "Auto"

    def set_bypass(self):
        """
        Set the service mode to bypass mode
        will set the battery threshold to 100%, and stop all the sampling
        :return:
        """
        self.flag_bypass = 1
        self.battery.set_threshold(100)

    def set_auto(self):
        """
        Set the service mode to auto mode.
        will reset the timer used for tracking purpose, and restart the sampling
        :return:
        """
        self._reset_discharging_timer(self.previous_discharging_time)
        self.flag_bypass = 0
        self.battery.set_threshold(self.range)
        self._start_tracking(1)
        self._start_saving(10)

    def exit(self):
        """
        Safely exit the tracker. will set the service mode to bypass mode for ending all sampling and resetting the
        threshold settings back to before.
        :return:
        """
        self.set_bypass()

    def _reset_discharging_timer(self, new_previous_discharging_time: float):
        self.previous_discharging_time = new_previous_discharging_time
        self.discharging_time = 0
        self.range_remain = self.range

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
        Collect the current status of the battery,
        and determine if range change need based of the collected data.
        """
        previous_time = self.timestamp
        previous_level = self.current_level
        self.current_level, self.current_state, self.timestamp = self.battery.get_info()
        # update
        if self.current_state == "Discharging":
            self.range_remain -= previous_level - self.current_level
            self.discharging_time += self.timestamp - previous_time
        # if remain_range reaches zero, recalculate range
        if self.range_remain <= 0:
            if self.discharging_time < self.previous_discharging_time * 0.9:
                self.range = self.range + 5 if self.range + 5 <= 100 else 100
            elif self.discharging_time > self.previous_discharging_time * 1.1:
                self.range = self.range - 5 if self.range - 5 >= 50 else 50
            # reset discharging timer, range remain
            self._reset_discharging_timer(self.discharging_time)

    def _track(self, interval: int):
        while self.flag_bypass == 0:
            self.update()
            time.sleep(interval)

    def _save(self, interval: int):
        while self.flag_bypass == 0:
            self.write_history()
            time.sleep(interval)

    def _start_tracking(self, interval: int):
        """
        create thread for tracking battery info
        :param: interval:int
        """
        Thread(target=self._track, args=(interval,)).start()

    def _start_saving(self, interval: int):
        """
        create thread for saving history to file
        :param: interval:int
        """
        Thread(target=self._save, args=(interval,)).start()


if __name__ == "__main__":
    t = Tracker(Battery())
    print(t.get_range())
    time.sleep(2)
    t.set_bypass()
    time.sleep(1)
    print(t.get_range())
    t.set_auto()
    time.sleep(1)
    print(t.get_range())
