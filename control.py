import subprocess


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


class Controller:

    @classmethod
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

    @classmethod
    def _get_stop_threshold(cls) -> float:
        p = subprocess.Popen("cat /sys/class/power_supply/BAT0/charge_stop_threshold", shell=True,
                             stdout=subprocess.PIPE)
        return float(p.stdout.readline().decode("utf-8").strip()) / 100


if __name__ == "__main__":
    import sys

    args = sys.argv
    Controller._set_stop_threshold(float(args[1]))
    print(Controller._get_stop_threshold())
