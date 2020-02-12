from math import *

# User input is always treated as a stirng. To use tha calculator we must convert the user input to numbers with int(variable_name)
# This is for whole numbers and use float(variable_name) function for decimal numbers. FLOAT SHOULD WORK WITH BOTH NUMBERS
num1 = input("Enter a number: ")
task = input("Please input what you want to do (*, +, -, /")
num2=input("Enter another number: ")
#taks = input("Please input what you want to do (*, +, -, /")
activity = float(num1) * float(num2)
print(activity)
#actiivty =float(num1) + (task) + float(num2) figure out how to leave the task option to be defined by the user.
#activity = float(num1) + float(num2)
# print(floor(activity)) Use this if you want the calculator to not display decimal numbers
#print(activity)




