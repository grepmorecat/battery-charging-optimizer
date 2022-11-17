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


if __name__ == "__main__":
    import sys
    args = sys.argv
