from battery import Battery


class Tracking():
    def __init__(self, b: Battery):
        self.discharging_time = 0
        self.charging_time = 0
        self.range_remain = b.range
