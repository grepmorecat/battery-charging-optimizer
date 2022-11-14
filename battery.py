import subprocess
import json
import time


class Battery:
    def _read_battery(self) -> (int, str, float):
        """
        get the current battery status by reading result of system bash command
        :return: tuple of level:int, state:str, timestamp:float
        """
        p = subprocess.Popen("acpi", stdout=subprocess.PIPE)
        battery_status = p.stdout.readline().decode("utf-8")
        battery_status = battery_status.replace(":", ",", 1).split(",")
        level = int(battery_status[2].strip()[:-1])
        state = battery_status[1].strip()
        timestamp = time.time()
        return (level, state, timestamp)

    def get_info(self) -> (int, str, float):
        """
        :return: tuple of level:int, state:str, timestamp:float
        """
        return self._read_battery()

    def __str__(self):
        _ = self._read_battery()
        return "Time:%s\nLevel:%d\nState:%s\n" % (_[2], _[0], _[1])


if __name__ == "__main__":
    b = Battery()
    while 1:
        time.sleep(1)
        print(b)
