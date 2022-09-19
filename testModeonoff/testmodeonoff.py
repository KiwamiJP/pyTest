#!/usr/bin/python3
import os
print("Python script for  driver signature turning on or off")
cmd =''
print('\n\n\n')
print("Please select an option: ")
print("Option 1: on")
print("Option 2: off")
print("Option 3: exit")
cmd = input("Enter option : ")
while cmd !='exit':
    if cmd == 'on':
        print('-----------Turning off the checking of integrity----------------')
        os.system('bcdedit.exe /set nointegritychecks on')
        print("-----------Turning on the test sign----------------")
        os.system('bcdedit /set testsigning on')
        print("-----------Waiting for restart---------------")
        os.system('shutdown -r')
        exit()
    elif cmd == 'off':
        print('------------Turning off the test sign---------------')
        os.system('bcdedit /set testsigning off')
        print("-----------Waiting for restart---------------")
        os.system('shutdown -r')
        quit()
    elif cmd == 'exit':
        quit()
    else:
        print("Please select a valid input....")
