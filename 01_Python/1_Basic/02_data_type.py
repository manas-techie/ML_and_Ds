# =================================================================================
# 2. DATA TYPES: INT, FLOAT, STRING, BOOLEAN
# =================================================================================


"""
Python has 6 main built-in data types:

1. Numeric Types (3 types)
int - integers (e.g., 5, -10)
float - decimal numbers (e.g., 3.14, -0.5)
complex - complex numbers (e.g., 3+4j)

2. Sequence Types (4 types)
str - strings (e.g., "hello")
list - ordered, mutable collections (e.g., [1, 2, 3])
tuple - ordered, immutable collections (e.g., (1, 2, 3))
range - sequence of numbers (e.g., range(5))

3. Mapping Type (1 type)
dict - key-value pairs (e.g., {"name": "Manas"})

4. Set Types (2 types)
set - unordered, unique values (e.g., {1, 2, 3})
frozenset - immutable set

5. Boolean Type (1 type)
bool - True or False

6. Special Type (1 type)

NoneType - None (represents absence of value)

Python has several built-in data types. The main primitive types are:
- int: Integer numbers (whole numbers)
- float: Floating-point numbers (decimal numbers)
- str: Strings (text)
- bool: Boolean (True/False)
"""


# 2.1 INTEGER (int)

"""
INTEGERS:
- Whole numbers (positive, negative, or zero)
- No size limit (Python 3+ has arbitrary precision)
- Can use underscores for readability in large numbers
"""

# Basic integers
positive_num = 42
negative_num = -17
zero = 0

# Large numbers with underscores for readability
population = 7_900_000_000        # 7.9 billion
print(f"World population: {population}")

# Different number systems
binary_num = 0b1010               # Binary (prefix: 0b) = 10 in decimal
octal_num = 0o12                  # Octal (prefix: 0o) = 10 in decimal
hex_num = 0xA                     # Hexadecimal (prefix: 0x) = 10 in decimal

print(f"Binary 0b1010 = {binary_num}")      # 10
print(f"Octal 0o12 = {octal_num}")          # 10
print(f"Hex 0xA = {hex_num}")               # 10


# 2.2 FLOAT (float)


"""
FLOATS:
- Numbers with decimal points
- Can be written in decimal or scientific notation
- Subject to floating-point precision limitations
"""

# Basic floats
price = 19.99
temperature = -40.5
gravity = 9.81

# Scientific notation
speed_of_light = 3e8              # 3 * 10^8 = 300,000,000
small_number = 1.5e-3             # 1.5 * 10^-3 = 0.0015

print(f"Scientific notation 3e8 = {speed_of_light}")

# Float operations
float_sum = 3.14 + 2.86           # 6.0
float_div = 10 / 3                # 3.3333... (regular division gives float)
mixed = 5 + 2.5                   # 7.5 (int + float = float)

print(f"10 / 3 = {float_div}")    # Regular division always returns float

# Floating-point precision issues (important to know!)
result = 0.1 + 0.2
print(f"0.1 + 0.2 = {result}")    # 0.30000000000000004 (not exactly 0.3!)

# Solution: Use round() or decimal module for precision
from decimal import Decimal
precise_result = Decimal('0.1') + Decimal('0.2')
print(f"Using Decimal: {precise_result}")  # Exactly 0.3


# 2.3 STRING (str)

"""
STRINGS:
- Sequence of characters
- Immutable (cannot be changed after creation)
- Can use single quotes, double quotes, or triple quotes
- Triple quotes for multi-line strings
"""

# Different ways to create strings
single_quote = 'Hello'
double_quote = "World"
triple_quote = '''This is a
multi-line
string'''

# Quotes inside strings
message1 = "It's a beautiful day"           # Single quote inside double quotes
message2 = 'He said "Hello"'                # Double quotes inside single quotes
message3 = "She said \"Hi\""                # Escaped double quote

# String concatenation
first_name = "Manas"
last_name = "Techie"
full_name = first_name + " " + last_name    # "Manas Techie"
print(full_name)

# String repetition
laugh = "ha" * 3                            # "hahaha"
print(laugh)

# String indexing (0-based, negative indexing from end)
text = "Python"
print(f"First character: {text[0]}")        # 'P'
print(f"Last character: {text[-1]}")        # 'n'
print(f"Second to last: {text[-2]}")        # 'o'

# String slicing [start:end:step]
word = "Programming"
print(f"word[0:4] = {word[0:4]}")          # 'Prog' (index 0 to 3)
print(f"word[:4] = {word[:4]}")            # 'Prog' (start from beginning)
print(f"word[4:] = {word[4:]}")            # 'ramming' (to the end)
print(f"word[::2] = {word[::2]}")          # 'Pormmn' (every 2nd character)
print(f"word[::-1] = {word[::-1]}")        # 'gnimmargorP' (reverse)

# String methods (strings have many built-in methods)
sample = "  Hello World  "
print(f"upper(): {sample.upper()}")         # '  HELLO WORLD  '
print(f"lower(): {sample.lower()}")         # '  hello world  '
print(f"strip(): '{sample.strip()}'")       # 'Hello World' (removes whitespace)
print(f"replace(): {sample.replace('World', 'Python')}")  # '  Hello Python  '
# split() splits the string into a list of words (default separator is whitespace)
print(f"split(): {sample.strip().split()}")              # ['Hello', 'World']

# String formatting (3 main ways)
name = "Manas"
age = 25

# 1. Old style (% formatting)
old_style = "My name is %s and I am %d years old" % (name, age)

# 2. str.format() method
format_method = "My name is {} and I am {} years old".format(name, age)

# 3. f-strings (Python 3.6+) - RECOMMENDED
f_string = f"My name is {name} and I am {age} years old"
print(f_string)

# f-strings can include expressions
x = 10
y = 20
print(f"The sum of {x} and {y} is {x + y}")  # Can evaluate expressions

# Raw strings (ignore escape characters)
normal_path = "C:\\Users\\Manas\\Documents"   # Need to escape backslashes
raw_path = r"C:\Users\Manas\Documents"        # r prefix = raw string
print(raw_path)


# 2.4 BOOLEAN (bool)

"""
BOOLEANS:
- Only two values: True or False (capitalized!)
- Result of comparison and logical operations
- Used in conditional statements and loops
"""

# Boolean values
is_active = True
is_deleted = False


# Logical operators
a = True
b = False

# Truthy and Falsy values
"""
Falsy values (evaluate to False):
- False, None, 0, 0.0, '' (empty string), [], {}, () (empty collections)

Truthy values (evaluate to True):
- Everything else!
"""

# Examples of truthy/falsy
print(f"bool(''): {bool('')}")              # False (empty string)
print(f"bool('text'): {bool('text')}")      # True (non-empty string)
print(f"bool(0): {bool(0)}")                # False
print(f"bool(42): {bool(42)}")              # True
print(f"bool([]): {bool([])}")              # False (empty list)
print(f"bool([1,2]): {bool([1,2])}")        # True (non-empty list)
