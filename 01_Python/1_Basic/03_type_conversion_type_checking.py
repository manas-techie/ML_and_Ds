# 3. TYPE CONVERSION AND TYPE CHECKING

"""
TYPE CONVERSION (Type Casting):
- Converting one data type to another
- Two types: Implicit (automatic) and Explicit (manual)
"""


# 3.1 IMPLICIT TYPE CONVERSION (Automatic)

"""
Python automatically converts smaller data type to larger to avoid data loss
"""

# Integer + Float = Float (automatic conversion)
num_int = 10
num_float = 3.5
result = num_int + num_float      # int is automatically converted to float
print(f"Type of result: {type(result)}")    # <class 'float'>
print(f"Result: {result}")                  # 13.5


# 3.2 EXPLICIT TYPE CONVERSION (Manual Type Casting)

"""
Manually convert using constructor functions:
- int() - Convert to integer
- float() - Convert to float
- str() - Convert to string
- bool() - Convert to boolean
"""

# String to Integer
age_str = "25"
age_int = int(age_str)
print(f"{age_int}, type: {type(age_int)}")

# String to Float
price_str = "19.99"
price_float = float(price_str)
print(f"{price_float}, type: {type(price_float)}")

# Integer/Float to String
number = 42
number_str = str(number)
print(f"'{number_str}', type: {type(number_str)}")

# Float to Integer (truncates decimal part)
pi = 3.14159
pi_int = int(pi)
print(f"{pi} converted to int: {pi_int}")   # 3 (decimal part is removed)

# Integer to Float
count = 10
count_float = float(count)
print(f"{count} converted to float: {count_float}")  # 10.0

# String to Boolean
bool1 = bool("Hello")              # True (non-empty string)
bool2 = bool("")                   # False (empty string)

# Integer to Boolean
bool3 = bool(0)                    # False
bool4 = bool(1)                    # True
bool5 = bool(-5)                   # True (any non-zero number)

# Boolean to Integer
true_int = int(True)               # 1
false_int = int(False)             # 0

# Conversion errors
try:
    invalid = int("hello")         # ValueError: invalid literal for int()
except ValueError as e:
    print(f"Error: {e}")

try:
    invalid2 = int("3.14")         # ValueError: can't convert directly
except ValueError as e:
    print(f"Error: {e}")
    # Solution: convert to float first
    correct = int(float("3.14"))   # Works! Result: 3
    print(f"Correct conversion: {correct}")


# 3.3 TYPE CHECKING

"""
Check the data type of a variable using:
- type() - Returns the type of object
- isinstance() - Checks if object is of specified type (recommended)
"""

# Using type()
x = 42
print(f"type(42): {type(x)}")              # <class 'int'>
print(f"type(3.14): {type(3.14)}")         # <class 'float'>
print(f"type('hello'): {type('hello')}")   # <class 'str'>
print(f"type(True): {type(True)}")         # <class 'bool'>


# Using isinstance() - RECOMMENDED way
y = 10
print(f"isinstance(10, int): {isinstance(y, int)}")          # True
print(f"isinstance(10, float): {isinstance(y, float)}")      # False
print(f"isinstance(10, (int, float)): {isinstance(y, (int, float))}")  # True (check multiple types)

# Why isinstance() is better than type()
# isinstance() handles inheritance properly and can check multiple types

z = 3.14
if isinstance(z, (int, float)):
    print("z is a number")

# Check before conversion (defensive programming)
user_input = "25"
if isinstance(user_input, str) and user_input.isdigit():
    converted = int(user_input)
    print(f"Safely converted: {converted}")

# isdigit() is a Python string method that checks if all characters in a string are digits (0-9).    
