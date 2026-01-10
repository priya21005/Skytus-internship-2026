#1. Calculate the reminder of two numbers.

# num1 = int(input("Print num1:"))
# num2 = int(input("Print num2:"))

# reminder = num1 % num2

# print("reminder of two numbers is:", reminder)


#2. Check if a number  is even or not.

# num = int(input("Enter a Number:"))

# if num % 2 == 0 :
#     print("number is even")
# else:
#     print("number is odd")


#3. Compare two numbers and print larger one.

# num1 = int(input("Enter num1:"))
# num2 = int(input("Enter num2:"))

# if num1 > num2:
#     print("num1 is greater than num")

# elif num2 > num1:
#     print("num2 is greater than num2")

# else:
#         print("both num are equal")

#4. WAP to calculate the square abd cube of number 

# num = int(input("Enter the number:"))

# square = num ** num
# cube = num * num * num

# print("Square of number:",square)
# print("Cube of number:",cube)

#5. Check if two numbers enterd are equal.

# num1 = int(input("Enter the num1:"))
# num2 = int(input("Enter the num2:"))

# if num1 == num2:
#     print("Both number are equal")

# else :
#     print("Both numbers are not equal")

#6. Take two numbers and print true if both are positive  else false.

# num1 = int(input("Enter the num1:"))
# num2 = int(input("Enter the num2:"))

# if num1 > 0 and num2 > 0:
#     print ("True")

# else :
#     print("False")  

#7.WAP to convert float to integer

# num = float(input("Enter the number:"))

# num_integer = int(num)

# print("Integer number:", num_integer)


#8.Take numbers as string convert to int and multiply by 10

# num = input("Enter a number: ")

# num_integer = int(num) * 10
# print("number is:", num_integer)

#9.WAP that uses and (& ) or operator to check multiple conditions.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#  AND operator
if num1 > 0 and num2 > 0:
    print("Both numbers are positive")
else:
    print("At least one number is not positive")

# OR operator
if num1 > 0 or num2 > 0:
    print("At least one number is positive")
else:
    print("Both numbers are not positive")

#10.Divide two numbers and print the quotient and reminder separate

num1 = int(input("Enter dividend: "))
num2 = int(input("Enter divisor: "))

quotient = num1 // num2
remainder = num1 % num2

print("Quotient is:", quotient)
print("Remainder is:", remainder)
