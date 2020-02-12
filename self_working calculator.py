#Define things to do

def add(x, y):
    return x + y
def substract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

#Ask for user input

user_choise = input("Select 1/2/3/4: ")
num1 = float (input("Please enter the first number: "))
num2 = float (input("Please enter the second number: "))

#Do the math
if user_choise == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif user_choise == '2':
   print(num1,"-",num2,"=", substract(num1,num2))
elif user_choise == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif user_choise == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")

#Profit
