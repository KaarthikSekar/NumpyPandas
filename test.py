# x = 1
# if x > 3:
#     print("case1")
# else:
#     print("case2")


# def add(a, b):
#     result = a + b
#     print(f"result is {result}")


# add(1, 1)

# with return i can pass it to variable and use it elsewhere
# but can't do the same with print; so we're using return inside the function but it is not mandatory


# adding bonus and salary
# def wage(hours):
#     return hours * 20


# def wage_bonus(hours):
#     return wage(hours) + 50


# # 10*20 -> 200
# print(wage(10)),
# # 10*20 + 50 -> 250
# print(wage_bonus(10))


# def plus_five(a):
#     return a + 5


# def m_by_3(a):
#     return plus_five(a) * 3


# print(plus_five(2))
# print(m_by_3(5))


# def saved(m):
#     if m >= 100:
#         print("good job")
#     else:
#         print("save more fucker")


# saved(1000)

# # lists

# name = ["kaarthi", "sai", "vicky", "ranton"]
# print(name[0])

# name[2] = "tarun"
# print(name)

# del name[2]
# print(name)

# #  to add, simply use append method
# # name.append('dwayne');


# # odd or even function


# def oddeve(a):
#     if a % 2 == 0:
#         print("even")
#     else:
#         print("odd")


# oddeve(2)

# numbers = [1, 2, 3, 4, 5, 6]


# def odeve(a):
#     if a % 2 == 0:
#         print("even")
#     else:
#         print("odd")


# odeve(numbers[1])

#  slicing blah[a:b];
# print(name[1:2])
# (age, agee) = "10,12".split(",")
# print(age, agee)


# def square(x):
#     a = x**2
#     p = 4 * x
#     print("area of the perimeter:")
#     return a, p


# print(square(3))

# # dict - always key value pair
# people = {"name": "kaarthik", "favcolor": "green"}
# # print(type(people)) dict type
# print(people["name"], people["favcolor"])

# # empty dict and assigning values
# team = {}
# team["pointguard"] = "dirk"
# print(team)

# # if you want to call, it with keys, then go with get() method
# print(team.get("pointguard"))

# Menu = {
#     "meal_1": "Spaghetti",
#     "meal_2": "Fries",
#     "meal_3": "Hamburger",
#     "meal_4": "Lasagna",
# }
# Menu["meal_3"] = "Cheeseburger"
# print(Menu.get("meal_3"))

# Menu = {
#     "meal_1": "Spaghetti",
#     "meal_2": "Fries",
#     "meal_3": "Cheeseburger",
#     "meal_4": "Lasagna",
#     "meal_5": "Soup",
# }

# Price_list = {}


# # Assigning prices to the corresponding meals from Menu
# Price_list["meal_1"] = 10  # Spaghetti
# Price_list["meal_2"] = 5  # Fries
# Price_list["meal_3"] = 8  # Cheeseburger
# Price_list["meal_4"] = 12  # Lasagna
# Price_list["meal_5"] = 5

# print(Price_list)

# for loop will loop through anything and will print it down below. if you want to print it in single line use end
# even = [0, 2, 4, 6, 8, 10]
# for a in even:
#     # print(a)
#     print(a, end=" ")

# while loop - multiples of 2 x = x+2 or x+=2
# x = 0
# while x <= 20:
#     print(x, end=" ")
#     x = x + 2

# x = 1
# while x <= 30:
#     print(x, end=" ")
#     x = x + 2


# range function - last value will not be added, -1 for countin backwards
# print(list(range(10)))

# b = [1, 2, 3, 4, 5]
# for item in range(len(b)):
#     print(b[item], end=" ")


# for i in range(1, 10, 2):
#     print(i)
# ➡️ Output:
# 1 3 5 7 9 (every 2nd number)

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for item in range(len(list)):
#     print(list[item] * 2, end=" ")


# nums = [1,35,12,24,31,51,70,100]
# def count(number):
#     for items in number:
#         if items <= 20:
#             print(items)


# nums = [1, 35, 12, 24, 31, 51, 70, 100]
# count(nums)


# def countone(number):
#     index = 0
#     counter = 0
#     while index < len(nums):
#         if nums[index] < 20:
#             print("less than 20", counter)
#             counter = counter + 1
#             index = index + 1


# nums = [1, 35, 12, 24, 31, 51, 70, 100]

# countone(nums)

# nums = [10, 25, 5, 30, 15, 40, 18]


# def count():
#     index = 0
#     counter = 0
#     while index < len(nums):
#         if nums[index] < 20:
#             counter += 1
#         index += 1
#     print("Count of numbers lower than 20:", counter)


# count()


# prices = {
#     "lasagna": 4,
#     "burger": 5,
# }
# # print(prices["lasagna"])

# money_spent = 0
# for i in prices:
#     print(prices[i])

# prices = {"box_of_spaghetti": 4, "lasagna": 5, "hamburger": 2}
# quantity = {"box_of_spaghetti": 6, "lasagna": 10, "hamburger": 0}

# money_spent = 0
# for i in prices:
#     if prices[i] >= 5:
#         money_spent = money_spent + (prices[i] * quantity[i])

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = list(areas)
# areas_copy = areas

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)

# Modules and packages
import math
# this is chaning the modules name for our understanding
from math import sqrt as s

print(math.sqrt(16))
print(s(16))

# Numpy - np is conventional

import numpy as np
import pandas as pd

print(np.__version__)
print(pd.__version__)
