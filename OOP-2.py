#ADVANCE OOP
# 1.create a base class animal and subclass dog and cat.
# creating a base class
# class Animal :
#     def speak(self):
#         print("Animal make sound:")

# # creating a subclass
# class Dog(Animal):
#     def speak(self):
#         print("Dog is bark")

# class Cat(Animal):
#     def speak(self):
#         print("Cat is meow")

# # creating a objecta
# dog = Dog()
# cat = Cat()

# dog.speak()
# cat.speak()


# 2.Create a class hierarchy for vehicle ->car->electriccar

# class Vehicle:
#     def info(self):
#         print("This is a vehicle")
    
# class Car(Vehicle):
#     def car_info(self):
#         print("This is a car")
    
# class ElectricCar(Car):
#     def electric_info(self):
#         print("This is an electric car")


# ecar = ElectricCar()

# ecar.info()
# ecar.car_info()
# ecar.electric_info()

# 3.Implement a method overriding in a base and derived class
# Base class
# class Animal :
#     def speak(self):
#         print("Animal make sound:")

# creating a subclass/Derived class
# class Dog(Animal):
#     def speak(self):
#         print("Dog is bark")

# class Cat(Animal):
#     def speak(self):
#         print("Cat is meow")

# # creating a objecta
# dog = Dog()
# cat = Cat()

# dog.speak()
# cat.speak()

# 4.Demonstrate multiple inheritance with two parent class

# parent class

# class Engine:
#     def engine_type(self):
#         print("Has a engine")
    
# class Battery:
#     def battery_type(self):
#         print("Has a battery")
    

# # multiple inheritance

# class ElectricVehicle(Engine,Battery):
#     def vehicle_info(self):
#         print("This is an electric vehicle")

# # object

# ev = ElectricVehicle()

# ev.engine_type()
# ev.battery_type()
# ev.vehicle_info()

# 5.create a polymorphic function that works with different shape

# class Shape:
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def area(self):
#         print("Area of rectangle: length * width")

# class Circle(Shape):
#     def area(self):
#         print("Area of circle: 3.14 * r * r")

# # Polymorphic function
# def calculate_area(shape):
#     shape.area()

# # Objects
# rect = Rectangle()
# circle = Circle()

# calculate_area(rect)
# calculate_area(circle)

# 6.Create a bank system with saving accounts and current accounts classes.
# Base class
# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance

#     def display_balance(self):
#         print("Balance:", self.balance)


# # Saving Account class
# class SavingAccount(BankAccount):
#     def add_interest(self):
#         interest = self.balance * 0.05
#         self.balance += interest
#         print("Interest added")


# # Current Account class
# class CurrentAccount(BankAccount):
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Amount withdrawn:", amount)
#         else:
#             print("Insufficient balance")


# # Object creation
# saving = SavingAccount("Priya", 10000)
# current = CurrentAccount("Rahul", 8000)

# saving.display_balance()
# saving.add_interest()
# saving.display_balance()

# current.display_balance()
# current.withdraw(3000)
# current.display_balance()

# 7. create a class with private attribute and getter/setter method

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         # private attribute
#         self.__marks = marks 
#     def get_marks(self):
#         return self.__marks
       

#     def set_marks(self,marks):
#          if marks >=0:
#             self.__marks = marks
#          else:
#             print("Invalid marks:")


# stu = Student("Priya",89)

# print("Marks:",stu.get_marks())

# stu.set_marks(90)

# print("Updated marks:",stu.get_marks())

# 8.create a teacher and student class to show ingeritance

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# class Student(Person):
#     def __init__(self, name, age, roll_no):
#         super().__init__(name, age)
#         self.roll_no = roll_no
    
#     def display_student(self):
#         self.display()   # corrected
#         print("Roll no:", self.roll_no)


# class Teacher(Person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject

#     def display_teacher(self):
#         self.display()   # corrected
#         print("Subject:", self.subject)


# student = Student("Priya", 21, 101)
# teacher = Teacher("Mr. Patel", 40, "Python")

# student.display_student()
# print()
# teacher.display_teacher()
   
# 9.Create a musicplayer class and sub class spotify to override paly method

# Base class
# class MusicPlayer:
#     def __init__(self, song):
#         self.song = song

#     def play(self):
#         print(f"Playing song: {self.song} on default music player")


# # Subclass
# class Spotify(MusicPlayer):
#     def play(self):   # Method overriding
#         print(f"Playing song: {self.song} on Spotify")


# # Objects
# player = MusicPlayer("Shape of You")
# spotify_player = Spotify("Unstopable")

# player.play()
# spotify_player.play()

# 10.Demonstrate the user of super() in inheritance

# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Derived class
class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)   # Call parent constructor
        self.roll_no = roll_no

    def display_student(self):
        super().display()            # Call parent method
        print("Roll No:", self.roll_no)


# Object creation
student = Student("Priya", 21, 101)
student.display_student()
