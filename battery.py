import subprocess
import time


class Battery:
    def get_info(self) -> (int, str, float):
        """
        :return: tuple of level:int, state:str, timestamp:float
        """
        return self._read_battery()

    def set_threshold(self, level: int):
        self._set_stop_threshold(level)

    def get_threshold(self):
        return self._get_stop_threshold()

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

    def _set_stop_threshold(self, level: int):
        """
        run bash command to set stop charging threshold of the system
        :return:
        """
        import os
        if os.getuid() != 0:
            raise Exception("need to run at root privileges")
        # check root privileges
        command = "echo %d > /sys/class/power_supply/BAT0/charge_stop_threshold" % (int(level),)
        subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()
        # p = subprocess.Popen("cat /sys/class/power_supply/BAT0/charge_stop_threshold", shell=True, stdout=subprocess.PIPE)
        # print(p.stdout.readline().decode("utf-8"))

    def _get_stop_threshold(self) -> float:
        p = subprocess.Popen("cat /sys/class/power_supply/BAT0/charge_stop_threshold", shell=True,
                             stdout=subprocess.PIPE)
        return float(p.stdout.readline().decode("utf-8").strip())

    def __str__(self):
        _ = self.get_info()
        return "Time:%s\nLevel:%d\nState:%s\n" % (_[2], _[0], _[1])


if __name__ == "__main__":
    b = Battery()
    b.set_threshold(85)
    print(b.get_threshold())
    while 1:
        time.sleep(1)
        print(b)
        b.get_info()
        print(b.get_threshold())
