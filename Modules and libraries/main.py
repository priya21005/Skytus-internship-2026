# 1.

# import mymath

# print("Addition:", mymath.add(10, 5))
# print("Subtraction:", mymath.subtract(10, 5))
# print("Multiplication:", mymath.multiply(10, 5))
# print("Division:", mymath.divide(10, 5))


# 2.create a module to perform string operation
# import string_ops

# s = "Hello World"

# print("Upper case:", string_ops.to_upper(s))
# print("Lower case:", string_ops.to_lower(s))
# print("Reversed:", string_ops.reverse_string(s))
# print("Count of 'o':", string_ops.count_char(s, 'o'))
# print("After replace:", string_ops.replace_space(s))


# 3.Use random module to generate 5 random integer

# import random

# for i in range(5):
#     print(random.randint(1,100))

# 4.use datetime module to display current date and time

# from datetime import datetime

# now = datetime.now()
# print("Current Date and Time:",now)

# 5.use math module to find factorial of number

# import math

# num = int(input("Enter a number:"))

# fact = math.factorial(num)
# print("Factorial:",fact) 

# 6.create a package shape with modules for circle and 

# from shape import circle, rectangle

# print("Circle Area:", circle.area(5))
# print("Circle Perimeter:", circle.perimeter(5))

# print("Rectangle Area:", rectangle.area(4, 6))
# print("Rectangle Perimeter:", rectangle.perimeter(4, 6))

# 7.import multiple function from one module and use them
# Import multiple functions from math_ops
# from math_ops import add, subtract, multiply, divide

# x = 10
# y = 5

# print("Add:", add(x, y))
# print("Subtract:", subtract(x, y))
# print("Multiply:", multiply(x, y))
# print("Divide:", divide(x, y))

# 8.WAP to suffle list using random module

# import random

# # Original list
# my_list = [10, 20, 30, 40, 50, 60, 70]

# print("Original List:", my_list)

# # Shuffle the list
# random.shuffle(my_list)

# print("Shuffled List:", my_list)


# 9.WAP to calculate the difference between two date.
# from datetime import datetime

# # Input two dates
# date1_str = input("Enter the first date (YYYY-MM-DD): ")
# date2_str = input("Enter the second date (YYYY-MM-DD): ")

# # Convert strings to datetime objects
# date1 = datetime.strptime(date1_str, "%Y-%m-%d")
# date2 = datetime.strptime(date2_str, "%Y-%m-%d")

# # Calculate difference
# diff = abs(date1 - date2)

# print("Difference between two dates is:", diff.days, "days")


# 10.use os module to list files in a dictionary
import os

# Specify the directory (use '.' for current folder)
directory = input("Enter directory path (or '.' for current folder): ")

# Creating  dictionary to store files
files_dict = {}

# List all items in the directory
for index, filename in enumerate(os.listdir(directory), start=1):
    # Check if it's a file
    if os.path.isfile(os.path.join(directory, filename)):
        files_dict[index] = filename

# Print the dictionary
print("Files in the directory:", files_dict)
