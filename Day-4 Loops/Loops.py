         #LOOPS
#1.Print numbers from 1 to 10

for i in range(1,10):
    print (i)

# 2.Display multiplication table for a given .
 
num = int(input("Enter the number:"))

for i in range(1,11) :
    print(num,"x",i, "=", num*i)


# 3.Find factorial of number

num = int(input("Enter the number: "))

fact = 1
for i in range(1, num + 1):
    fact = fact * i

print("Factorial:", fact)


# 4 Generate the first fibonnacci number

num = int(input("Enter the number for fibonacci series:"))

a,b = 0,1

print(a,b, end = " ")

for i in range(2,num):
    c = a + b
    print(c)

    a = b
    b = c

# 5.Check if number is prime

num = int(input("Enter a number:"))

count = 0
for i in range(1,num+1):

    if num % i == 0:
        count+=1


if count == 2:
    print("num is prime:")

else:
    print("not a prime:")


# 6.Reverse number

num = int(input("Enter a number: "))

rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number:", rev)

# 7.Count digit in number

num = int(input("Enter the number:"))

initialization

count = 0

while num > 0:
   count += 1
   num = num //10  #remove one digit each time

print ("Number of digit:",count) 

# 8.find the sum of even number between 1-100

sum_even = 0

for i in range(2,101,2):
    sum_even = sum_even + i

print("sum of evem numbers between 1 and 100:", sum_even)


# 9.print pyramid pattern
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):

    print(" " * (rows - i), end="")
    
    print("*" * (2 * i - 1))

# 10. find all divisior of number:

num = int(input("enter the number:"))

print("Divisors of",num , "are:")

for i in range(1,num+1):
    if num % i == 0:

        print(i,end = " ")