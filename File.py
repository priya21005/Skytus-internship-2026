#FILE HANDLING

# 1.WAP to read file and  display it"s content

try:
    file = open("errors.txt", "r")  
    content = file.read()            
    print("File Content:\n")
    print(content)
    file.close()                     

except FileNotFoundError:
    print("Error: The file does not exist.")

# 2.WAP to count the no of lines in file.

try:
    file = open("errors.txt", "r")
    
    lines = file.readlines()
    
    num_lines = len(lines)
    
    print("Number of lines in the file:", num_lines)
    
    file.close()

except FileNotFoundError:
    print("Error: The file does not exist.")

# 3.WAP to count how many times each word appear in file.
try:
    with open("errors.txt", "r") as file:
        text = file.read()  # Read entire content
    
    words = text.lower().split()
    
    word_count = {}
    
    for word in words:
        # Remove punctuation from word
        word = word.strip(".,!?;:()[]{}\"'")
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1  # <-- This was missing

    print("Word Frequencies:")
    for word, count in word_count.items():
        print(word, ":", count)

except FileNotFoundError:
    print("Error: The file 'errors.txt' does not exist.")

# 4.WAP to write 5 user sentence enterd in file

Open your file in append mode
file_name = "errors.txt"  

with open(file_name, "a") as file:
    for i in range(5):
        sentence = input(f"Enter sentence {i+1}: ")
        file.write(sentence + "\n")  # Write each sentence on a new line

print("5 sentences have been added to", file_name)

# 5.WAP to append a list of string in existing file.

strings_to_append = [
    "This is the first line.",
    "Python is fun.",
    "File handling is easy.",
    "We can append data.",
    "End of list."
]

file_name = "errors.txt" 

with open(file_name, "a") as file:
    for line in strings_to_append:
        file.write(line + "\n")  

print("List of strings has been appended to", file_name)

6.WAP to read file and print onlylines containing a specific word

word_to_search = input("Enter the word to search in file: ").lower()

try:
    
    with open("errors.txt", "r") as file:
        lines = file.readlines()  # Read all lines
    
    print(f"\nLines containing '{word_to_search}':")
    
    for line in lines:
       
        if word_to_search in line.lower():
            print(line.strip())  

except FileNotFoundError:
    print("Error: The file 'errors.txt' does not exist.")

# 7.WAP to replace a specific word in a file and save changes

word_to_replace = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

file_name = "errors.txt"  

try:
    
    with open(file_name, "r") as file:
        content = file.read() 

    new_content = content.replace(word_to_replace, new_word)

    with open(file_name, "w") as file:
        file.write(new_content)

    print(f"All occurrences of '{word_to_replace}' have been replaced with '{new_word}' in {file_name}.")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")

# 8 WAP to merge the context of two text files into a third file.

file1 = "Day-4 Loops/file1.txt"  
file2 = "Day-4 Loops/file2.txt"   
file3 = "Day-4 Loops/file3.txt"  

try:
    
    with open(file1, "r") as f1:
        content1 = f1.read()

    with open(file2, "r") as f2:
        content2 = f2.read()

    with open(file3, "w") as f3:
        f3.write(content1 + "\n" + content2)  

    print(f"Contents of '{file1}' and '{file2}' have been merged into '{file3}'.")

except FileNotFoundError as e:
    print("Error: File not found -", e)

# 9 WAP to read csv file and display it"s content
import csv
try:
    with open("Day-4 Loops/data.csv", "r") as file:
        csv_reader = csv.reader(file)
        
        print("CSV File Content:\n")
        for row in csv_reader:
            print(row)

except FileNotFoundError:
    print("Error: CSV file not found.")

# 10.WAP to backup a file by copying it's content into another file
try:
   
    with open("Day-4 Loops/original.txt", "r") as source_file:
        content = source_file.read()

    with open("Day-4 Loops/backup.txt", "w") as backup_file:
        backup_file.write(content)

    print("File backup created successfully.")

except FileNotFoundError:
    print("Error: Original file not found.")




