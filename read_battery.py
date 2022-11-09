import subprocess


def read_battery():
    """
    function that get the current battery status
    Parameters:
    Returns:
        list:[battery_name, charging_states, level]

   """
    p = subprocess.Popen("acpi", stdout=subprocess.PIPE)
    battery_status = p.stdout.readline().decode("utf-8").strip()
    battery_status = battery_status.replace(":", ",").split(",")
    return [i.strip() for i in battery_status]

if __name__ == "__main__":
    print(read_battery())
    print(read_battery.__doc__)