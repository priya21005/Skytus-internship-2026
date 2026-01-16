#OOP

# 1.Create a car class with attribute like brand,model,and speed, and methods to accelerate/brake.

# Creating class

class Car:

    def __init__(self,brand,model,speed):
        self.brand = brand
        self.model = model
        self.speed = speed
    def accelerate(self,increase):
        self.speed += increase
        print("Speed after accelerating:", self.speed, "km/h")
    def brake(self,decrease):
        self.speed -= decrease
        print("Speed after break:",self.speed,"km/h") 

# creating object

car = Car("BMW", "M5", 250)

car.accelerate(30)
car.accelerate(40)

# 2. Creating a Bankaccount class 
class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Current Balance:", self.balance)
        else:
            print("Insufficient balance")


acc1 = BankAccount("Priya", 5000)

acc1.deposit(2000)
acc1.withdraw(3000)

# 3.Create a student class with method to calculate average marks.

# creating student class
class Student:
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def Average_marks(self):
        total = sum(self.marks)
        average_marks = total / len(self.marks)
        print("Average marks:",average_marks)
    
student1 = Student("Priya",[85, 90, 78])
student1.Average_marks()

# 4.Create a rectangle class with method to find area and parameter

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of rectangle:", self.length * self.width)
    
    def perimeter(self):
        print("Perimeter of rectangle:", 2 * (self.length + self.width))


rect = Rectangle(20, 5)

rect.area()
rect.perimeter()

# 5.Create an employee class that displays salary details

# creating employees class

class Employees:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def emp_salary(self):
        print("Employee name",self.name)
        print("Employee salary:",self.salary)


emp1 = Employees("Priya",25000)

emp1.emp_salary()

# 6.Create a book class to store title,author and price and display detail
# Create Book class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_detail(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


# Object creation
book1 = Book("Atomic Habits", "James Clear", 611)

book1.display_detail()

# 7.Create a circle class to find area and circumference

class Circle:

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        print("Area of circle:",3.14*self.radius*self.radius)
    
    def circumference(self):
        print("Circumference of circle:",2*3.14*self.radius)

cir1 = Circle(8)

cir1.area()
cir1.circumference()

# 8.Creating a laptop class
class Laptop:
    def __init__(self, price, discount):
        self.price = price          
        self.discount = discount    

    def show_price(self):
        print("Price of laptop:", self.price)

    def apply_discount(self):
        discount_amount = self.price * self.discount / 100
        final_price = self.price - discount_amount
        print("Discount Amount:", discount_amount)
        print("Final Price after discount:", final_price)


lap1 = Laptop(75000, 25)

lap1.show_price()
lap1.apply_discount()

# 9.Create a flight class with seat booking functionality

class Flight:
    def __init__(self, flight_name, total_seat):
        self.flight_name = flight_name
        self.total_seat = total_seat   # fixed typo
        self.booked_seat = 0
    
    def book_seat(self, seats):       # renamed method
        if seats <= (self.total_seat - self.booked_seat):
            self.booked_seat += seats
            print(seats, "seat successfully booked.")
            print("Seats remaining:", self.total_seat - self.booked_seat)
        else:
            print("Booking failed! Seats are not available.")

    def flight_details(self):
        print("Flight name:", self.flight_name)
        print("Total seats:", self.total_seat)
        print("Booked seats:", self.booked_seat)
        print("Available seats:", self.total_seat - self.booked_seat)


f1 = Flight("Indigo 101", 50)

f1.flight_details()
f1.book_seat(5)
f1.book_seat(48)
f1.flight_details()

# 10.Create a shop class with  a method to add and list products

class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        print(self.products)

shop1 = Shop("XYZ's Store")

shop1.add_product("Laptop")
shop1.add_product("Phone")
shop1.list_products()


