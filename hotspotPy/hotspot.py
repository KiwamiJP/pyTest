#!/usr/bin/python3
#hotspot enabler
import os
os.system("cls")
print("\n\n\n")
print("\n\n\n\n\n")
os.system('netsh wlan set hostednetwork mode=allow')
os.system('netsh wlan set hostednetwork ssid=testpy key=12345678 KeyUsage=Persistent')
os.system('netsh wlan start hostednetwork')