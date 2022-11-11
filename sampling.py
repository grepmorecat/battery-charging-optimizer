from battery import *
from time import sleep


def sampling(battery:Battery):
    while 1:
        true_level = battery.get_level()
        ratioed_level = battery.get_ratioed_level()
        print(true_level)
        sleep(1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    b = Battery()
    sampling(b)