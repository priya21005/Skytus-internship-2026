# FUNCTIONS:

# 1.FUNCTION TO CHECK IF NO IS PRIME.

def is_prime(n) :
    if n < 1:
        return False
    for i in range(2,n) :
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number:"))
if is_prime(num):
    print(num, "is prime nember")
else:
    print(num,"is not a prime number")

# 2. Function to reverse string
def reverse_string(s):
    return s[::-1]

text = input("Enter a strings:")
reversed_text = reverse_string(text)
print("Reversed string:",reversed_text)

# 3.Function to find factorial
def factorial(n):
    fact = 1

    for i in range(1,n+1):
        fact*= i
        return fact
    
num = int(input("Enter a number:"))
print("Factorial od number is",num,"is",factorial(num))

#4. Function to calculate simple interest
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (%): "))
time = float(input("Enter the time in years: "))
si = simple_interest(principal, rate, time)
print("Simple Interest is:", si)


# 5.Check if word is palindrome

def word_palindrome(word):

    if word == word[::-1]:
        return True
    else :
        return False

text = input("Enter a text:")
if word_palindrome(text):
    print("Text is palindrome")
else:
#     print("Text is not palindrome")

# 6.count wovels in string
   
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

text = input("Enter a string: ")
# print("Number of vowels:", count_vowels(text))

# 7.Function to merge to list
def merge_lists(list1, list2):
    return list1 + list2  

list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list = merge_lists(list1, list2)
print("Merged List:", merged_list)

# 8.Find GCD of two numbers

def gcd(a, b):
    while b != 0:
        a, b = b, a % b  
    return a  

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

print("GCD of", num1, "and", num2, "is", gcd(num1, num2))

# 9.find area of rectangle

def rectangle_area(length, width):
    return length * width

length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))

area = rectangle_area(length, width)
print("Area of the rectangle is:", area)

# 10.Function to check Armstrong number
def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    total = 0
    
    for digit in num_str:
        total += int(digit) ** num_digits
    
    return total == number

# Input from user
num = int(input("Enter a number: "))

if is_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


