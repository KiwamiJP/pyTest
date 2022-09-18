#!/usr/bin/python3
#hotspot enabler
import os
os.system("cls")
print("\n")
command = ''
while command != "exit":
    print("Type this commands : ")
    print("start for starting hotspot")
    print("stop for stopping hotspot")
    print("exit for exiting from programme")
    command = input("Enter yor cmd here: ")
    if command == 'start':
        print("Starting hotspot******")
        os.system('netsh wlan set hostednetwork mode=allow ssid=testpy key=12345678 KeyUsage=Persistent')
        os.system('netsh wlan start hostednetwork')
    elif command == 'stop':
        print("Stopping hotspot*****")
        os.system('netsh wlan stop hostednetwork')
    else:
        exit()

