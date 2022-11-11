from battery import Battery


class Tracking:
    def __init__(self, battery: Battery):
        self.battery = battery
        self.discharging_time = 0
        self.charging_time = 0
        self.range_remain = battery.range

    def track(self):
        if self.battery.get_state_str() == "Discharging":
            self.discharging_time += 1
            self.range_remain -= 0.01
        elif self.battery.get_state_str() == "Charging":
            self.charging_time += 1
            self.range_remain += 0.01
        else:
            pass

        print("Discharging time: ", self.discharging_time)
        print("Charging time: ", self.charging_time)
        print("Range remain: ", self.range_remain)
        print("Battery level: ", self.battery.get_level())
        print("Battery ratioed level: ", self.battery.get_ratioed_level())
        print("Battery state: ", self.battery.get_state_str())
        print("Battery state code: ", self.battery.get_state_code())

    def get_discharging_time(self):
        return self.discharging_time

    def get_charging_time(self):
        return self.charging_time

    def get_range_remain(self):
        return self.range_remain

    def get_battery_level(self):
        return self.battery.get_level()

    def get_battery_ratioed_level(self):
        return self.battery.get_ratioed_level()

    def get_battery_state_str(self):
        return self.battery.get_state_str()

    def get_battery_state_code(self):
        return self.battery.get_state_code()

    def reset(self):
        self.discharging_time = 0
        self.charging_time = 0
        self.range_remain = self.battery.range


if __name__ == "__main__":
    b = Battery()
    t = Tracking(b)
    t.track()


