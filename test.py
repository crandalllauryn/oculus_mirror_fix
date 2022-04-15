import time as t
from datetime import datetime, time
import wmi
import os

# Functions


def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    check_time = datetime.utcnow().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else:  # crosses midnight
        return check_time >= begin_time or check_time <= end_time

# Main code


def main():
    f = wmi.WMI()

    running_windows = 0

    check_time = is_time_between(time(11, 00), time(21, 00))

    while(True):
        t.sleep(600)
        if check_time == True:
            for process in f.Win32_Process():
                if "OculusMirror.exe" == process.Name:
                    running_windows += 1
                    if running_windows > 1:
                        os.system("TASKKILL /F /IM OculusMirror.exe")
                        print('Closed extra OculusMirror.exe windows')
                    elif running_windows == 1:
                        running_windows = 0
                        print('Only one OculusMirror.exe window is open')
                    else:
                        print('No OculusMirror.exe window is open')
        else:
            print("Amped Reality is closed")


# Run
if __name__ == '__main__':
    main()
