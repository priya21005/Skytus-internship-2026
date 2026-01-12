#1.0 Take a string input and print it's length.
a = str(input("Enter a Name:"))

print(len(a))

#1.1.Convert sentence to lower case

sentence = str(input("Enter sentence:"))

print(sentence.lower())

1.2Replace spaces with underscore in a string

sentence = input("Enter sentence:")
print(sentence.replace(" ","_"))

# 1.3 Extract the first and last character of string

a = str(input("Enter a Name:"))
print("First character:",a[0])
print("Last character:",a[-1])

#1.4 Reverse string using slicing.
a = "Priya"
print(a[::-1])

1.5 Count how many times a letter in a string

a = "Priya"
print(a.count("a"))

# 1.6 Check if a word is present in a sentence
 
sentence = str(input("Enter sentence:"))
word = input("Enter Word:")

if word in sentence:
    print("word is present")

else:
    print("Word is not present") 

# 1.7 Take name and age and print using F-string formatting

name = "Priya"
Age = 21

print(f"My name is {name}, I am {Age} old.")

# 1.8 Remove extra spaces from the start and end of a string.

s = input("enter the string:")

print(s.strip())

# 1.9 Join a list of words into a single string with between them.
list = ["Banana", "Apple","Mango","Cherry","Grapes"]
result= " ".join(list)
print(result)




#Python String handling.

# 2.1 Create a list of your 5 favorite movie.

Movies = ["Zootopiya","Zootopiya-2","Moaana","Tangle bells","Marvel"]
print(Movies)

# 2.2 Add new movie to the list

Movies = ["Zootopiya","Zootopiya-2","Moaana","Tangle bells","Marvel"]
Movies.append("Inception")

print(Movies)

#2.3 Remove the first movie from the list

Movies = ["Zootopiya","Zootopiya-2","Moaana","Tangle bells","Marvel"]
Movies.remove("Zootopiya")

print(Movies)

#2.4 Sort a list of numbers in ascending order

number = [85,45,2,10]
number.sort()
print("Number in ascending order",number)

#2.5 reverse list

number = [85,45,2,10]
number.reverse()
print("Number in descending order",number)

# 2.6 find largest number in a list

number = [85,45,2,10]
largest = max(number)

print(largest)

# 2.7 merge two list into one

list1 = [24,85,710,52]
list2 = [55,7,8,9,6]

merge = list1 + list2
print(merge)

# 2.8 Access the last element of list without using index number.

list = [24,85,710,52]

last_element = list[-1:]
print("Last element of list",last_element)

# 2.9 Create a nested list  and access the specific inner element

nested_list = [
    [25, 45, 75, 85],
    [2, 4, 8, 6],
    [85, 96, 36, 45]
]

element = nested_list [1][1]
print(nested_list)
print(element)

# 2.10 Count how many times an element appear in a list.

list = [25,45,71,25,5,100]
count_num =list.count(25)

print(count_num)


