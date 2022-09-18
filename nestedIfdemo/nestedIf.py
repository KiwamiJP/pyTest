#!/usr/bin/python3
# demo of nested if else
# programmer: HZA
num1 = int(input("Enter a number: "))
if num1 % 2 == 0:
    if num1 % 3 == 0:
        print(num1, "is divisible by 2 and 3")
    else:
        print(num1, "is divisible by 2 not by 3")
else:
    if num1 % 3 == 0:
        print(num1, "is divisible by 3 not by 2")
    else:
        print(num1, "is not divisible by 2 and 3")
