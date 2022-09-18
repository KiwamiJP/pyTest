#!/usr/bin/python3
#simple calculator
#programmer: Hein Zin Aung
while 1:
    num_1 = float(input("Enter first num: "))
    num_2 = float(input("Enter second num: "))
    operator = input("Enter operator: ")
    if operator == "+":
        result = num_1 + num_2
    elif operator == "-":
        result = num_1 - num_2
    elif operator == "*":
        result = num_1*num_2
    elif operator == "/":
        result = num_1 / num_2
    elif operator == "%":
        result = num_1 % num_2
    else:
        print("Wrong operator")
    print("result is ", result)