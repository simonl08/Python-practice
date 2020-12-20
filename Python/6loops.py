# favourite_drinks = ["coke", "fanta", "tonic"]

# for i in favourite_drinks:
#     print(i)


# for i in range(5, 11, 2): #the last number prints the number in increments of 2
#     print(i)

#while loop will run indefinitely until a condition is met

# num = 0

# while num < 10:
#     num += 1
#     print(num)

import random

rand_num = random.randint(0,53)

my_num = 52

while rand_num != my_num:
    print(rand_num)
    rand_num = random.randint(0,53) #needed so it assigns another random number

print(f"You've found {my_num}!")