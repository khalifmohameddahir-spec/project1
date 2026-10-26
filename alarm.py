import time


def set_alarm():
    hours = int(input("Enter the hours: "))
    minutes = int(input("Enter the minutes: "))
    if not 0 <= hours <= 23:
        raise ValueError("Hours must be between 0 and 23.")
    if not 0 <= minutes <= 59:
        raise ValueError("Minutes must be between 0 and 59.")
    return hours, minutes


def check_time(alarm_time):
    while True:
        current_time = time.localtime()
        if (current_time.tm_hour, current_time.tm_min) == alarm_time:
            print("It's time to wake up!")
            return
        time.sleep(1)


def alarm_clock():
    print("Welcome to alarm clock")
    alarm_time = set_alarm()
    print(f"Alarm set for {alarm_time[0]:02d}:{alarm_time[1]:02d}")
    check_time(alarm_time)


if __name__ == "__main__":
    alarm_clock()
