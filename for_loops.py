# cycle
# Loop is a cycle

# For Loops
# While Loops

# For Loops iterate -> Take some actions over a sequence:
# Strings
# List
# Range of numbers

# for variable in sequence:
# Do something

# For loops string
# var1 = "Python"
#
# for letter in var1:
#     print(letter)


# For loops List
# list1 = ["gen", 1, 2, False, True, "danubreed"]
#
# for item in list1:
#     print(item)


# For Loops Range

# for number in range(10, 21):
#     print(number)

# write a for loop to print each animal in uppercase.
# animals = ["lion", "dog", "cat", "fish", "bird", "giraffe",
#            "tiger", "horse", "leopard", "antelope", "donkey", "kangaroo"]
#
# for animal in animals:
#     print(animal.upper())
# print(animal.upper())


# Write a for loop using range() to print all numbers from 1 to 100 with it printing 10, 20, 30, 40, 50, 60, 70.....
# for numbers in range(0, 101, 10):
#     print(numbers)


# Write a Python program that adds all the even numbers from 1 to 100 (inclusive)
# using a for loop and range().

# even_sum = 0
#
# for num in range(2, 101, 2):
#     even_sum += num
# print("The sum of even numbers from 1 to 100 is:", even_sum)
#
# total_even_number = 0
#
# for number in range(1, 101):
#     if number % 2 == 0:
#         total_even_number += number
# print(total_even_number)
#
# Fizz-Buzz Challenge
# Write a program that prints numbers from 1 to 100.
# For multiples of 3, print "Fizz" instead of the number,
# and for multiples of 5, print "Buzz." For numbers that are multiples of both 3 and 5,
# print "FizzBuzz."

# Ese Solution


# for number in range(1, 101):
#     if number % 3 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0:
#         print("Fizz")

#
# for number in range(1, 101):
#     if number % 3 == 0:
#         print("Fizz")
#     if number % 5 == 0:
#         print("Buzz")
#     if number % 3 and number % 5 == 0:
#         print("FizzBuzz")

import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!#$%&'()*+,-.:;<=>?@[]^_`{|}~"

# Use for loop to randomly generate password of length x, base on the user input
# So firstly, ask the user the length of the password,
# use a loop to randomly generate the password from letters, numbers and symbols


# user_input = int(input("Pick a number as the length of your password. \n"))
# pwd_character = letters + numbers + symbols
# password = ""
# for i in range(1, user_input+1):
#     new_char = random.choice(pwd_character)
#     password += new_char
#
# print(password)


# Counting Occurrences of an Element in a List
# Objective: Write a program that counts how many times a specific element appears in a list.
# Instructions:
# Create a list of elements (can be numbers or strings).
# Ask the user to input the element they want to count.
elements = [3, 5, 3, 7, 8, 3, 5, 3]
# Use a for loop to count the occurrences of the element in the list.
# elements = [3, 5, 3, 7, 8, 3, 5, 3]


# user_input = int(input("Input an element to count: "))
#
# count = 0
#
# for element in elements:
#     if element == user_input:
#         count += 1
#
# print(f"The element {user_input} appears {count} times")
