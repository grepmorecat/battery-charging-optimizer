import subprocess
import time

def check_root(func):
    """
    decorator that check if has root privileges before executing function
    :return:
    """
    def inner(*args, **kwargs):
        import os
        if os.getuid() != 0:
            raise Exception("need to run at root privileges")
        func(*args, **kwargs)
    return inner


def _read_battery() -> (int, str, float):
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


@check_root
def _set_stop_threshold(cls, level: float):
    """
    run bash command to set stop charging threshold of the system
    :return:
    """
    # need error handling
    command = "echo %d > /sys/class/power_supply/BAT0/charge_stop_threshold" % (int(level * 100),)
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()
    # p = subprocess.Popen("cat /sys/class/power_supply/BAT0/charge_stop_threshold", shell=True, stdout=subprocess.PIPE)
    # print(p.stdout.readline().decode("utf-8"))


def _get_stop_threshold(cls) -> float:
    p = subprocess.Popen("cat /sys/class/power_supply/BAT0/charge_stop_threshold", shell=True,
                         stdout=subprocess.PIPE)
    return float(p.stdout.readline().decode("utf-8").strip()) / 100


if __name__ == "__main__":
    import sys

    args = sys.argv
    _set_stop_threshold(float(args[1]))
    print(_get_stop_threshold())
