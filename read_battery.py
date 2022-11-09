import subprocess


def read_battery():
    p = subprocess.Popen("acpi", stdout=subprocess.PIPE)
    battery_status = p.stdout.readline().decode("utf-8").strip()
    battery_status = battery_status.replace(":", ",").split(",")
    return [i.strip() for i in battery_status]

if __name__ == "__main__":
    print(read_battery())