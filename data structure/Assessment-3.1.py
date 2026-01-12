#3 Tupple AND List
3.1 create a tupple with 5 num

num = (5,10,20,30,25)
print(num)

3.2 Access third element in tuple
num = (5,10,20,30,25)

print(num[2])

#3.3 Unpack tuple in separate variable.
num = (5,10,20,30,25)
a,b,c,d,e = num
print(a,b,c,d,e)

# 3.4 Create a set of 5 fruits

fruits = {"apple","mango","banana","grapes","cherry"}
print(fruits)

3.5 Remove element from set
fruits = {"apple","mango","banana","grapes","cherry"}
element_remove = fruits.remove("apple")
print(fruits)

# 3.6 Find union of two sets

set1 = {1,2,6,7}
set2 = {2,4,6,8}

set_union = set1.union(set2)
print(set_union)

3.7 Find an intersection of two 
set1 = {1,2,6,7}
set2 = {2,4,6,8}

set_intersection= set1.intersection(set2)
print(set_intersection)

# 3.8 Check one set is subset of another
set1 = {1,2}
set2 = {1,2,6,8}

print(set1.issubset(set2))
print(set2.issubset(set1))

3.9 Convert a list with duplicate values into set to remove duplicates.

list = [1,2,2,7.4,5]
unique_set = set(list)
print(unique_set)



#Dictionaries

# 4.1 Create a dictionary storing student name ,marks.

Create a dictionary storing student name and marks
dict1 = {
    "name": "Priya",
    "marks": 95
}

print(dict1)

# 4.2 Add new key-value pair from dictionary Existing dictionary
student = {
    "name": "Priya",
    "marks": 95
}


student["age"] = 21

print(student)


#4.3 Delete a key value pair from a dictionary 
student = {
     "name": "Priya",
     "marks": "95",
     "age" : "21"
 }


del student["age"]

print(student)

4.4 Merge two dictionary into one
dict1 = {"name": "Priya", "marks": 95}
dict2 = {"age": 21, "grade": "A"}

dict1.update(dict2)
print(dict1)

# 4.5 Check if a key exists in a dictionary

student = {
    "name" : "Priya",
    "marks" : 95,
    "age" : 21
}

if "age" in student:
    print("Age exist in dict")
else:
    print("not exists") 

#4.6 count word frequency in a given string using a dictionary 

sentence = "python is easy and python is powerful"

word_count = {}


for word in sentence.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


print(word_count)

# 4.7 find the key with the maximum value in dictionary

marks = {
    "Maths": 85,
    "Science": 92,
    "English": 78
}

max_key = max(marks, key=marks.get)

print(max_key)

# 4.8 Reverse keys and value in a dictionary.

student = {
    "Maths": 85,
    "Science": 92,
    "English": 78
}

reversed_dict = {}

for key, value in student.items():
    reversed_dict[value] = key

print(reversed_dict)


# 4.9 update value for a specific key

student = {
     "name" : "Priya",
     "marks" : 95,
     "age" : 21
 }
student["marks"] = 85
print(student)

# 4.10 Convert a list  of tuple into dictionaries

num = [("priya",52),("meghna", 60),("Darshan" , 45)]

result = dict(num)
print(result)