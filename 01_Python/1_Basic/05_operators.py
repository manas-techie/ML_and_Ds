
# 2. OPERATORS

"""
OPERATORS:
- Special symbols that perform operations on operands (values/variables)
- Python has 6 main categories of operators
"""

# 2.1 ARITHMETIC OPERATORS
"""
ARITHMETIC OPERATORS:
Used to perform mathematical operations

┌──────────┬─────────────────┬──────────────────────┐
│ Operator │ Name            │ Example              │
├──────────┼─────────────────┼──────────────────────┤
│ +        │ Addition        │ 5 + 3 = 8            │
│ -        │ Subtraction     │ 5 - 3 = 2            │
│ *        │ Multiplication  │ 5 * 3 = 15           │
│ /        │ Division        │ 5 / 2 = 2.5          │
│ //       │ Floor Division  │ 5 // 2 = 2           │
│ %        │ Modulus         │ 5 % 2 = 1            │
│ **       │ Exponentiation  │ 5 ** 2 = 25          │
└──────────┴─────────────────┴──────────────────────┘
"""

# Addition (+)
sum_result = 10 + 5
print(f"10 + 5 = {sum_result}")                    # 15

string_concat = "Hello" + " " + "World"            # String concatenation
print(f"String concatenation: {string_concat}")    # Hello World

list_concat = [1, 2] + [3, 4]                      # List concatenation
print(f"List concatenation: {list_concat}")        # [1, 2, 3, 4]


# Subtraction (-)
difference = 10 - 5
print(f"10 - 5 = {difference}")                    # 5

negative = -10                                     # Unary minus (negation)
print(f"Negative: {negative}")                     # -10


# Multiplication (*)
product = 10 * 5
print(f"10 * 5 = {product}")                       # 50

string_repeat = "Ha" * 3                           # String repetition
print(f"String repetition: {string_repeat}")       # HaHaHa

list_repeat = [0] * 5                              # List repetition
print(f"List repetition: {list_repeat}")           # [0, 0, 0, 0, 0]


# Division (/) - Always returns float
division = 10 / 3
print(f"10 / 3 = {division}")                      # 3.3333333...

even_division = 10 / 2
print(f"10 / 2 = {even_division}")                 # 5.0 (still float!)


# Floor Division (//) - Returns integer, rounds down
floor_div = 10 // 3
print(f"10 // 3 = {floor_div}")                    # 3 (rounds down)

negative_floor = -10 // 3
print(f"-10 // 3 = {negative_floor}")              # -4 (rounds DOWN to more negative)


# Modulus (%) - Returns remainder
remainder = 10 % 3
print(f"10 % 3 = {remainder}")                     # 1


# Exponentiation (**) - Power operation
power = 2 ** 3
print(f"2 ** 3 = {power}")                         # 8 (2 to the power of 3)


# Square root (using fractional exponent)
sqrt = 16 ** 0.5
print(f"Square root of 16: {sqrt}")                # 4.0

# Order of operations (PEMDAS/BODMAS)
"""
1. Parentheses/Brackets
2. Exponentiation
3. Multiplication, Division, Floor Division, Modulus (left to right)
4. Addition, Subtraction (left to right)
"""



# 2.2 COMPARISON OPERATORS (RELATIONAL OPERATORS

"""
COMPARISON OPERATORS:
Compare two values and return Boolean (True/False)

┌──────────┬──────────────────────┬──────────────────────┐
│ Operator │ Name                 │ Example              │
├──────────┼──────────────────────┼──────────────────────┤
│ ==       │ Equal to             │ 5 == 5 → True        │
│ !=       │ Not equal to         │ 5 != 3 → True        │
│ >        │ Greater than         │ 5 > 3 → True         │
│ <        │ Less than            │ 5 < 3 → False        │
│ >=       │ Greater or equal     │ 5 >= 5 → True        │
│ <=       │ Less or equal        │ 5 <= 3 → False       │
└──────────┴──────────────────────┴──────────────────────┘
"""

# Equal to (==)
print(f"5 == 5: {5 == 5}")                         # True
print(f"5 == 3: {5 == 3}")                         # False
print(f"'hello' == 'hello': {'hello' == 'hello'}")  # True

# IMPORTANT: == vs = 
x = 5           # = is ASSIGNMENT (assigns value)
result = x == 5 # == is COMPARISON (checks equality)
print(f"x == 5: {result}")                         # True


# Not equal to (!=)
print(f"5 != 3: {5 != 3}")                         # True
print(f"5 != 5: {5 != 5}")                         # False


# Greater than (>)
print(f"10 > 5: {10 > 5}")                         # True
print(f"5 > 10: {5 > 10}")                         # False
print(f"5 > 5: {5 > 5}")                           # False


# Less than (<)
print(f"3 < 5: {3 < 5}")                           # True
print(f"5 < 3: {5 < 3}")                           # False


# Greater than or equal to (>=)
print(f"5 >= 5: {5 >= 5}")                         # True
print(f"6 >= 5: {6 >= 5}")                         # True
print(f"4 >= 5: {4 >= 5}")                         # False


# Less than or equal to (<=)
print(f"5 <= 5: {5 <= 5}")                         # True
print(f"4 <= 5: {4 <= 5}")                         # True
print(f"6 <= 5: {6 <= 5}")                         # False


# Chaining comparisons (Python feature!)
age = 25
print(f"18 <= age <= 65: {18 <= age <= 65}")       # True
# Same as: (18 <= age) and (age <= 65)

score = 85
print(f"0 <= score <= 100: {0 <= score <= 100}")   # True


# Comparing strings (lexicographic order - alphabetical)
print(f"'apple' < 'banana': {'apple' < 'banana'}") # True (a comes before b)
print(f"'Apple' < 'apple': {'Apple' < 'apple'}")   # True (uppercase < lowercase in ASCII)


# Comparing different types
print(f"5 == 5.0: {5 == 5.0}")                     # True (value comparison)
print(f"5 == '5': {5 == '5'}")                     # False (different types)



# 2.3 LOGICAL OPERATORS

"""
LOGICAL OPERATORS:
Combine conditional statements

┌──────────┬────────────────────────────────────────────┐
│ Operator │ Description                                │
├──────────┼────────────────────────────────────────────┤
│ and      │ Returns True if BOTH are True              │
│ or       │ Returns True if AT LEAST ONE is True       │
│ not      │ Reverses the boolean value                 │
└──────────┴────────────────────────────────────────────┘

TRUTH TABLES:
and:  True and True = True    |  or:  True or True = True
      True and False = False  |       True or False = True
      False and True = False  |       False or True = True
      False and False = False |       False or False = False

not:  not True = False
      not False = True
"""

# AND operator - Both conditions must be True
age = 25
has_license = True

can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")                   # True

print(f"True and True: {True and True}")           # True
print(f"True and False: {True and False}")         # False
print(f"False and True: {False and True}")         # False
print(f"False and False: {False and False}")       # False


# OR operator - At least one condition must be True
is_weekend = False
is_holiday = True

can_relax = is_weekend or is_holiday
print(f"Can relax: {can_relax}")                   # True

print(f"True or True: {True or True}")             # True
print(f"True or False: {True or False}")           # True
print(f"False or True: {False or True}")           # True
print(f"False or False: {False or False}")         # False


# NOT operator - Reverses the boolean value
is_raining = False
print(f"Is sunny: {not is_raining}")               # True

print(f"not True: {not True}")                     # False
print(f"not False: {not False}")                   # True


# Combining logical operators
age = 20
has_ticket = True
has_id = True

# Complex condition
can_enter = (age >= 18 and has_ticket) and has_id
print(f"Can enter: {can_enter}")                   # True

# Order of precedence: not > and > or
result = True or False and False                   # True or (False and False) = True
print(f"True or False and False: {result}")        # True

# Use parentheses for clarity
result_clear = (True or False) and False           # True and False = False
print(f"(True or False) and False: {result_clear}")# False


# Short-circuit evaluation
"""
Python stops evaluating as soon as result is determined
- 'and': If first is False, doesn't check second
- 'or': If first is True, doesn't check second
"""

# This won't cause error because second part isn't evaluated
x = 0
result = x != 0 and 10 / x > 1  # False and ... = False (doesn't evaluate 10/x)
print(f"Short-circuit and: {result}")              # False


# 2.4 ASSIGNMENT OPERATORS

"""
ASSIGNMENT OPERATORS:
Assign values to variables

┌──────────┬─────────────────┬────────────────────────┐
│ Operator │ Example         │ Equivalent to          │
├──────────┼─────────────────┼────────────────────────┤
│ =        │ x = 5           │ x = 5                  │
│ +=       │ x += 3          │ x = x + 3              │
│ -=       │ x -= 3          │ x = x - 3              │
│ *=       │ x *= 3          │ x = x * 3              │
│ /=       │ x /= 3          │ x = x / 3              │
│ //=      │ x //= 3         │ x = x // 3             │
│ %=       │ x %= 3          │ x = x % 3              │
│ **=      │ x **= 3         │ x = x ** 3             │
└──────────┴─────────────────┴────────────────────────┘
"""


# 2.5 IDENTITY OPERATORS

"""
IDENTITY OPERATORS:
Check if two variables refer to the SAME OBJECT in memory (not just equal values)

┌──────────┬─────────────────────────────────────────┐
│ Operator │ Description                             │
├──────────┼─────────────────────────────────────────┤
│ is       │ Returns True if same object             │
│ is not   │ Returns True if different objects       │
└──────────┴─────────────────────────────────────────┘

IMPORTANT: 'is' checks IDENTITY (same object), '==' checks EQUALITY (same value)
"""

# is operator
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(f"x == y: {x == y}")                         # True (same values)
print(f"x is y: {x is y}")                         # False (different objects)
print(f"x is z: {x is z}")                         # True (same object)

# Visualizing with id() - shows memory address
print(f"id(x): {id(x)}")
print(f"id(y): {id(y)}")                           # Different from x
print(f"id(z): {id(z)}")                           # Same as x


# is not operator
print(f"x is not y: {x is not y}")                 # True (different objects)


# Special case: Small integers and strings (Python optimization)
a = 256
b = 256
print(f"a is b (256): {a is b}")                   # True (cached by Python)

a = 257
b = 257
print(f"a is b (257): {a is b}")                   # May be False (not always cached)

# String interning
s1 = "hello"
s2 = "hello"
print(f"s1 is s2: {s1 is s2}")                     # True (interned)


# Common use case: Checking for None
value = None
print(f"value is None: {value is None}")           # True (RECOMMENDED way)
print(f"value == None: {value == None}")           # True (but 'is' is preferred)

# Why 'is' for None?
# None is a singleton - only one None object exists
# Using 'is None' is faster and more Pythonic


# 2.6 MEMBERSHIP OPERATORS

"""
MEMBERSHIP OPERATORS:
Check if a value exists in a sequence (string, list, tuple, set, dict)

┌──────────┬─────────────────────────────────────────┐
│ Operator │ Description                             │
├──────────┼─────────────────────────────────────────┤
│ in       │ Returns True if value is in sequence   │
│ not in   │ Returns True if value is NOT in sequence│
└──────────┴─────────────────────────────────────────┘
"""

# in operator with lists
fruits = ["apple", "banana", "cherry"]
print(f"'apple' in fruits: {'apple' in fruits}")       # True
print(f"'orange' in fruits: {'orange' in fruits}")     # False


# in operator with strings
text = "Hello World"
print(f"'Hello' in text: {'Hello' in text}")           # True
print(f"'hello' in text: {'hello' in text}")           # False (case-sensitive)
print(f"'o W' in text: {'o W' in text}")               # True (substring)


# in operator with tuples
numbers = (1, 2, 3, 4, 5)
print(f"3 in numbers: {3 in numbers}")                 # True
print(f"6 in numbers: {6 in numbers}")                 # False


# in operator with dictionaries (checks KEYS)
person = {"name": "John", "age": 30, "city": "New York"}
print(f"'name' in person: {'name' in person}")         # True (key exists)
print(f"'John' in person: {'John' in person}")         # False (value, not key)

# Check if value exists in dictionary
print(f"'John' in person.values(): {'John' in person.values()}")  # True


# not in operator
print(f"'grape' not in fruits: {'grape' not in fruits}")  # True
print(f"'apple' not in fruits: {'apple' not in fruits}")  # False


# Practical use case: Validation
username = input("Enter username: ") if False else "admin123"  # Simulated
forbidden_chars = ["!", "@", "#", "$", "%"]

has_forbidden = any(char in username for char in forbidden_chars)
if has_forbidden:
    print("Username contains forbidden characters")
else:
    print("Username is valid")


# Use case: Menu selection
valid_choices = ['1', '2', '3', '4', '5']
user_choice = '3'

if user_choice in valid_choices:
    print(f"You selected option {user_choice}")
else:
    print("Invalid choice")