# 1 Check if persion is eligible to vote

age = int(input("Enter the age:"))

if age >= 18:
    print("person is eligible for vote")

else:
    print("person is not eligible for vote")

# 2.Grade calculate based on marks. 90+ A,80+ B,else C

marks = int(input("Enter the marks:"))

if marks >= 90 :
    print("Grade is A")
elif marks >= 80:
    print("Grade is B")
else:
    print("Grade is C")

# 3.Simulate traffic light Red=Stop, Yello= Wait, Green = GO

light = input("Enter the light color:")

if light == "red" :
    print("STOP")
elif light == "yellow":
    print("WAIT")
elif light == "green":
    print("GO")
else :
    print("Invalid color")

# 4. ATM Withdrwal check:sufficient balance or not
balance = 25000
amount = float(input("Enter the Amount:"))

if amount <= balance:
    print("Sufficient balance")

else :
    print("amount is not sufficient")

# 5.Check if number is positive or negative or zero

num = int(input("Enter the number:"))

if num > 0 :
    print("Number is positive")
elif num < 0:
    print("Number is negative:")
else :
    print("Number is zero")

6.check if number is lies in given range:
n = 100
num = int(input("Enter the Number:"))

if num > n:
    print("Number is not in range:")
else :
    print("Number in range")

# 7.user name and password varification

correct_username = "Priya"
correct_password = "Priya@123"

username = input("Enter the user name: ")
password = input("Enter the password: ")

if username == correct_username and password == correct_password:
    print("Login successful!")
elif username != correct_username and password != correct_password:
    print("Invalid username and password")
elif username != correct_username:
    print("Invalid username")
else:
    print("Invalid password")

# 8.Electricity bill calculator based on unit cossumes

unit = float(input("Enter the no of unit cossummed:"))

bill = 0

if unit < 100:
    bill = unit * 5
elif unit <200:
    bill = unit * 7
else: 
    bill = (100 * 5) + (100 * 7) + (unit - 200) * 10

print(f"Total electricity bill {bill}" )

# 9.Simple calculator

num1 = int(input("Enter the num1:"))
num2 = int(input("Enter the num2:"))

print("Select operation:")
print("1.Addition(+)")
print("2.Subtraction(-)")
print("3.Multiplication(*)")
print("4.Division(/)")

choice = input("Enter the operation 1/2/3/4:")

if choice == "1":
    print(f"Addition {num1+num2}")
elif choice == "2":
    print(f"Subtraction {num1-num2}")
elif choice == "3":
    print(f"Multiplication {num1*num2}")
elif choice == "4":
    print(f"Division {num1/num2}")
else:
    print("invalid operation")

# 10. Check type of triangle( equilateral,isoscale,scalene)

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Not a valid triangle")
