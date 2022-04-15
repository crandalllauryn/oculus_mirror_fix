# OculusMirror.exe
# if hours = open hours
# run script every min
# if hours = closed hours
# stop script
# count how many oculus mirror windows are open
# if oculus mirrow open > 1
# for i in range number of windows open
# os.close file OculusMirror.exe
#print("Closed extra OculusMirror.exe windows")
# else
#print("Only one OculusMirror.exe window is open")

import wmi
import os

f = wmi.WMI()
running_windows = 0

for process in f.Win32_Process():
    if "OculusMirror.exe" == process.Name:
        running_windows += 1

        if running_windows > 1:
            os.system("TASKKILL /F /IM OculusMirror.exe")
            print('Closed extra OculusMirror.exe windows')
        elif running_windows == 1:
            print('Only one OculusMirror.exe window is open')
