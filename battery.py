import subprocess


def _read_battery():
    """
    function that get the current battery status
    Parameters:
    Returns:
        list:[charging_states, level]

   """
    p = subprocess.Popen("acpi", stdout=subprocess.PIPE)
    battery_status = p.stdout.readline().decode("utf-8").strip()
    battery_status = battery_status.replace(":", ",", 1).split(",")
    return [i.strip() for i in battery_status][1:3]


class Battery:
    def __init__(self):
        self.range = 0.6;  # r22.2
        self.lowest_level = 0.1;  # t8

    def get_level(self) -> float:
        return int(_read_battery()[1][:-1])

    def get_ratioed_level(self) -> float:
        return self.get_level() * self.range + self.lowest_level




if __name__ == "__main__":
    b = Battery()
    print(b.get_level())
    print(b.get_ratioed_level())
