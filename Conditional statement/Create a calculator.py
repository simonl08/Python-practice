print("Menu")
print("add")
print("subtraction")
print("multiply")
print("divide")

add='+'
subtraction='-'
multiply='*'
divide='/'

calculate = str(input("Enter how you would like to calculate your numbers from the menu: "))
number1=int(input("Enter your first number: "))
number2=int(input("Enter your second number: "))

if calculate == 'add':
    print(number1 + number2)
elif calculate == 'subtraction':
    print(number1 - number2)
elif calculate == 'multiply':
    print(number1 * number2)
elif calculate == 'divide':
    print(number1 / number2)
else:
    print("You have inputted the wrong value please refer to the menu")

