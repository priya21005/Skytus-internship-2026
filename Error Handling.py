#Error handling

# 1. WAP to handle division by zero

try:
    a = int(input("Enter a number:"))
    b = int(input("Enter a number:"))
    print(a/b)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

# 2.WAP to handle invalid integer input:
try :
    num = int(input("Enter an integer:"))
    print("You enterd input",num)
except ValueError:
    print("Error: invalid integer value")

# 3. WAP to open a file and handle the "file is not found" error

try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Error: File not found")

# 4. WAP to demonstrate multiple exception blocks

try :
    a = int(input("Enter a number:"))
    b = int(input("Enter a number:"))

    print(a/b)
except ZeroDivisionError :
    print("Error : ZeroDivisorErro is occured:")

except ValueError :
    print("Error: invalid integer is entered:")

# 5.WAP TO USE FINALLY FOR RESOURCE CLEAN-UP
file = None
try:
    file = open("file.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("Error: File not found")

finally:
    if file:
        file.close()
        print("File closed")

# 6.WAP to create a custon exception for invalid age(<18)

class InvalidAgeError(Exception):
    pass

age = int(input("Enter age: "))

try:
    if age < 18:
        raise InvalidAgeError
    print("Age is valid")

except InvalidAgeError:
    print("Invalid age")

# 7.write a programme to handle index error while accessing a list
numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter the index to access: "))
    print("Value at index", index, "is", numbers[index])

except IndexError:
    print("Error: Index out of range. Please enter a valid index.")

except ValueError:
    print("Error: Invalid input. Please enter an integer index.")



# 8.WAP a programme to take two numbers and handle all possible error.


try :
    
  num1= int(input("Enter num1:"))
  num2 = int(input("Enter a num2:"))

  print(num1/num2)

except ZeroDivisionError :

    print("Error: zero divisor erro is occured:")
except ValueError :

    print("Error: Invaliid integer is entered:")

# 9. WAP to log errors to file instead of printing them

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)

except Exception as e:
    # Log the error to a file instead of printing
    with open("errors.txt", "a") as f:
        f.write(f"Error occurred: {e}\n")

# 10.WAP that validates an email for invalid errors

class InvalidEmailError(Exception):
    pass

try:
    email = input("Enter your email: ")

    if "@" not in email or "." not in email:
        raise InvalidEmailError("Invalid email format")

    print("Email is valid")

except InvalidEmailError as e:
    print(e)
