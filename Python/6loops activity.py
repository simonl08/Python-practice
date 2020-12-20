# Activity 1
# film_list = ["ghostbusters", "Harry Potter", "Hobbit", "Narnia"]

#  #for i in film_list:
#    #  print(i)
 
# def film_check():
#     global film_list
#     if film_list[2] == "ghostbusters":
#         print("yey it's ghostbusters")
#     else:
#         print("boooo we want ghostbusters")

# film_check()

#Activity 2 
# count= 0

# for count in range(0, 10):
#     count += 1
#     print(count)
#     if count == 9:
#         break

#Activity 3
import random
count = 0

while count < 6:
    count += 1
    rand_num = random.randint(0,30)
    if rand_num % 7 ==0:
        print(f"{rand_num} is divisible by 7")
    else:
        print(f"{rand_num} is not divisible by 7")

