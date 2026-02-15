

# STRING INDEXING AND SLICING

text = "Python"
# Indexing: P=0, y=1, t=2, h=3, o=4, n=5 (or -6 to -1 from right)
print(f"First: {text[0]}, Last: {text[-1]}")        # P, n

# Slicing: [start:stop:step]
word = "Hello World"
print(f"{word[0:5]}")           # Hello (0-4)
print(f"{word[:5]}")            # Hello (start from 0)
print(f"{word[6:]}")            # World (to end)
print(f"{word[::2]}")           # HloWrd (every 2nd char)
print(f"{word[::-1]}")          # dlroW olleH (reverse)

# ESSENTIAL STRING METHODS


# --- Case conversion ---
text = "Hello World"
print(f"{text.upper()}")        # HELLO WORLD
print(f"{text.lower()}")        # hello world
print(f"{text.title()}")        # Hello World

# --- Whitespace removal (VERY IMPORTANT!) ---
messy = "  hello  "
print(f"'{messy.strip()}'")     # 'hello' (both ends)
print(f"'{messy.lstrip()}'")    # 'hello  ' (left)
print(f"'{messy.rstrip()}'")    # '  hello' (right)

# --- split() - string to list ---
sentence = "Python is awesome"
words = sentence.split()        # ['Python', 'is', 'awesome']
print(words)

csv = "apple,banana,cherry"
fruits = csv.split(",")         # ['apple', 'banana', 'cherry']
print(fruits)

# --- join() - list to string ---
words = ["Python", "is", "great"]
sentence = " ".join(words)      # Python is great
print(sentence)

csv = ",".join(["a", "b", "c"]) # a,b,c
print(csv)

# --- replace() - find and replace ---
text = "Hello World"
new_text = text.replace("World", "Python")  # Hello Python
print(new_text)

# Remove characters
phone = "(123) 456-7890"
clean = phone.replace("(", "").replace(")", "").replace(" ", "").replace("-", "")
print(clean)                    # 1234567890

# --- find() - search substring ---
text = "Hello World"
index = text.find("World")      # 6 (index where found)
print(index)
print(text.find("xyz"))         # -1 (not found)

# --- startswith() / endswith() ---
filename = "document.pdf"
print(filename.startswith("doc"))           # True
print(filename.endswith(".pdf"))            # True
print(filename.endswith((".pdf", ".doc")))  # True (multiple)

# --- count() - count occurrences ---
text = "banana"
print(text.count("a"))          # 3

# --- Validation methods ---
print("123".isdigit())          # True (all digits)
print("abc".isalpha())          # True (all letters)
print("abc123".isalnum())       # True (letters or digits)
print("   ".isspace())          # True (all whitespace)


# STRING FORMATTING

# --- F-STRINGS (RECOMMENDED - Python 3.6+) ---
name = "John"
age = 30

# Basic
print(f"My name is {name}, I'm {age}")

# Expressions
x, y = 10, 20
print(f"Sum: {x + y}")          # Sum: 30

# Method calls
text = "hello"
print(f"{text.upper()}")        # HELLO

# Number formatting
pi = 3.14159
print(f"{pi:.2f}")              # 3.14 (2 decimals)

price = 1234.5
print(f"${price:,.2f}")         # $1,234.50 (comma separator)

# Alignment
print(f"|{name:10}|")           # |John      | (left, width 10)
print(f"|{name:>10}|")          # |      John| (right)
print(f"|{name:^10}|")          # |   John   | (center)

# Padding
num = 7
print(f"{num:03}")              # 007 (pad with zeros)

# --- .format() METHOD (OLDER) ---
print("Name: {}, Age: {}".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))  # Named
print("{:.2f}".format(pi))      # 3.14

# --- % FORMATTING (LEGACY - AVOID) ---
print("Name: %s, Age: %d" % (name, age))
print("Pi: %.2f" % pi)


# STRING CONCATENATION AND REPETITION

# --- Concatenation with + ---
first = "John"
last = "Doe"
full = first + " " + last       # John Doe
print(full)

# Must convert non-strings
age = 30
msg = "Age: " + str(age)        # Age: 30
# OR better: use f-string
msg = f"Age: {age}"

# --- join() for multiple strings (BETTER THAN +) ---
parts = ["home", "user", "file.txt"]
path = "/".join(parts)          # home/user/file.txt
print(path)

# --- Repetition with * ---
print("=" * 50)                 # 50 equal signs
print("ha" * 3)                 # hahaha


# PRACTICAL EXAMPLES

# Example 1: Clean user input
user_input = "  JoHn@EmAiL.CoM  "
clean_email = user_input.strip().lower()
print(clean_email)              # john@email.com

# Example 2: Parse CSV
csv_line = "John,30,NYC,Engineer"
name, age, city, job = csv_line.split(",")
print(f"{name} is {age} from {city}")

# Example 3: Create slug from title
title = "Hello World! Python Guide."
slug = title.lower().replace(" ", "-").replace("!", "").replace(".", "")
print(slug)                     # hello-world-python-guide

# Example 4: Extract domain from email
email = "user@example.com"
domain = email.split("@")[1]
print(domain)                   # example.com

# Example 5: Mask credit card
card = "1234567890123456"
masked = "*" * 12 + card[-4:]
print(masked)                   # ************3456

# Example 6: Build URL
base = "https://api.example.com"
endpoint = "users"
user_id = "123"
url = f"{base}/{endpoint}/{user_id}"
print(url)

# Example 7: Format table
print(f"{'Name':10} {'Age':5} {'City':10}")
print("-" * 30)
print(f"{'Alice':10} {'25':5} {'NYC':10}")
print(f"{'Bob':10} {'30':5} {'LA':10}")

# Example 8: Remove extra spaces
messy = "  Hello    World   "
clean = " ".join(messy.split())
print(clean)                    # Hello World

# Example 9: Word counter
text = "hello world hello python"
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)               # {'hello': 2, 'world': 1, 'python': 1}

# Example 10: Create progress bar
def progress_bar(percent):
    filled = int(percent / 10)
    return f"|{'█' * filled}{'░' * (10 - filled)}| {percent}%"

print(progress_bar(30))         # |███░░░░░░░| 30%
print(progress_bar(70))         # |███████░░░| 70%


# QUICK REFERENCE
"""
INDEXING/SLICING:
text[0]         First char      text[-1]        Last char
text[1:4]       Slice 1-3       text[:5]        First 5
text[5:]        From 5 to end   text[::-1]      Reverse

METHODS:
.upper()        UPPERCASE       .lower()        lowercase
.strip()        Remove spaces   .split()        String → List
.join(list)     List → String   .replace(old,new) Find/Replace
.find(sub)      Find index      .startswith()   Check start
.endswith()     Check end       .count()        Count occurrences
.isdigit()      All digits?     .isalpha()      All letters?

FORMATTING (USE F-STRINGS!):
f"{var}"        Insert          f"{num:.2f}"    2 decimals
f"{num:,}"      Comma sep       f"{text:10}"    Width 10

CONCATENATION:
+ operator      Join 2 strings  .join(list)     Join multiple (BEST)
* operator      Repeat string
"""
