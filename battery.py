import subprocess
import time
import control


class Battery:
    def get_info(self) -> (int, str, float):
        """
        :return: tuple of level:int, state:str, timestamp:float
        """
        return control._read_battery()

    def __str__(self):
        _ = self.get_info()
        return "Time:%s\nLevel:%d\nState:%s\n" % (_[2], _[0], _[1])


if __name__ == "__main__":
    b = Battery()
    while 1:
        time.sleep(1)
        print(b)
