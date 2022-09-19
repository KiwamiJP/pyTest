#!/usr/bin/python3
# hotspot enabler
import os

os.system("cls")
print("\n")
command = ''
while command != "exit":
    print('\n\n\n')
    print("Type this commands : ")
    print("==> start <== for starting hotspot")
    print("==> stop  <== for stopping hotspot")
    print("==> exit  <== for exiting from programme")
    command = input("Enter yor cmd here: ")
    if command == 'start':
        print("*****Starting hotspot******")
        ssid = input("Enter your hotspot ssid: ")
        key = input("Enter your hotspot password: ")
        os.system('netsh wlan set hostednetwork mode=allow ssid='+ssid+' key='+key)
        os.system('netsh wlan start hostednetwork')
    elif command == 'stop':
        print("*****Stopping hotspot*****")
        os.system('netsh wlan stop hostednetwork')
    elif command == 'exit':
        print("*****Exiting from programme*****")
        exit()
    else:
        print("Wrong input please try again")
        os.system('pause')