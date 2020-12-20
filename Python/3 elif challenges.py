# Challenge 1
# password = input("Enter your password here")

# if len(password) >= 8:
#     print("Your password is saved")
# else:
#     print("please enter a password containing at least 8 or more characters")

# Challenge 2
# num = 8

# if num %3 and num %5 == 0:
#     print("is divisible by 3 and 5")
# else:
#     print("The number entered is not divisible by 3 or 5")

# Challenge 3
# num = 4

# if num %3 == 0 and num %7 == 0:
#      print("fizz buzz")
# elif num %3 == 0:
#     print("fizz")
# elif num %7 == 0:
#     print("buzz")
# else:
#     print(num)

# Challenge 4
# word = "heyh"

# if word[0] == word[-1]:
#     print("The first letter and last is the same")
# else:
#     print("the first letter and last letter is not the same")

# Challenge 5
# time = 10
# place_of_work = "work"
# town_of_home = "home"

# if time >= 9 and time <= 17:
#     print(f"I am currently at {place_of_work}")
# elif time >= 19 and time <= 24:
#     print(f"I am current at {town_of_home}")
# else:
#     print("I am most likely elsewhere")

# Challenge 6
# num1=4
# num2=5
# answer=(num1+num2)

# if answer % 2 ==0:
#     print("Sum is even")
# else:
#     print("the sum is not even")

# Challenge 7
num = input("Write in a number ")
if num == num[::-1]:
    print("This number is a palindrome")
else:
    print("This number is not a palindrome")