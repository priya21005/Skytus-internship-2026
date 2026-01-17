# 2.create a module to perform string operation
def to_upper(text):
    return text.upper()

def to_lower(text):
    return text.lower()

def reverse_string(text):
    return text[::-1]

def count_char(text, char):
    return text.count(char)

def replace_space(text):
    return text.replace(" ", "_")
