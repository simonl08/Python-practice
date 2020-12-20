# coffee_is_grinding = False

# # global means looking for variable outside of function

# def press_grind_beans():
#     global coffee_is_grinding
#     if coffee_is_grinding: 
#         print("Stopping the grind")
#         coffee_is_grinding = False
#     else:
#         print("Grinding is about to begin")
#         coffee_is_grinding = True

# press_grind_beans()
# press_grind_beans()
#=================================================================
# def cash_withdrawal(amount, accnum):
#     print("Withdrawing {} from account {}".format(amount, accnum))

# cash_withdrawal(300, 50449921)
# cash_withdrawal(30, 50449921)
# cash_withdrawal(200, 20441121)
#==============================================================
# def coffee_order(size, drinktype):
#     print("You ordered a {} cup of {}.".format(size, drinktype))

# coffee_order("large", "cappuccino")
# coffee_order("small", "latte")
#=============================================================
# f_name = input("Enter your name: ")
# my_age = input("Enter your age: ")

# def greetings(f_name, my_age):
#     print("Hi my name is {} and I am {} years old.".format(f_name, my_age))

# greetings(f_name, my_age)
#============================================
# def add_up(num1, num2):
#     return num1 + num2

# print(add_up(40, 60))

#=============================================
# def multiply_by_nine_fifths(celsius):
#     return celsius * (9/5) # 9/5 = 1.8

# def get_fahrenheit(celsius):
#     return multiply_by_nine_fifths(celsius) +32

# print("The temperature is {} oF".format(get_fahrenheit(15))) # 1.8 * 15 = 27

#========================================

def minus_32(fah):
    return fah - 32
def multiply(fah):
    return minus_32(fah) * 5/9

print("it is {} degrees celsius".format(multiply(20)))