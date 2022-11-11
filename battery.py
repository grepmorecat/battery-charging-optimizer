import subprocess


class Battery:
    def __init__(self):
        self.range = 0.6  # r22.2
        self.lowest_level = 0.1  # t8

    @classmethod
    def _read_battery(cls) -> [float, str]:
        """
        get the current battery status by reading result of system bash command
        :return: [level:float, charging_states:str]
        """
        p = subprocess.Popen("acpi", stdout=subprocess.PIPE)
        battery_status = p.stdout.readline().decode("utf-8")
        battery_status = battery_status.replace(":", ",", 1).split(",")
        level = float(battery_status[2].strip()[:-1])
        state = battery_status[1].strip()
        return [level, state]

    def get_state_str(self) -> str:
        return self._read_battery()[1]

    def get_level(self) -> float:
        return self._read_battery()[0]

    def get_ratioed_level(self) -> float:
        return self.get_level() * self.range + self.lowest_level


if __name__ == "__main__":
    b = Battery()
    print(b.get_level())
    print(b.get_ratioed_level())
    print(b.get_state_str())
