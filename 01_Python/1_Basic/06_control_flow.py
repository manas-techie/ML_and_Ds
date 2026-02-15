# 3.1 IF, ELIF, ELSE STATEMENT

"""
CONDITIONAL STATEMENTS:
Execute code based on conditions

Syntax:
    if condition:
        # code block
    elif another_condition:
        # code block
    else:
        # code block

IMPORTANT: Python uses INDENTATION (4 spaces) to define code blocks
"""

# Simple if statement
age = 20

if age >= 18:
    print("You are an adult")                      # This executes


# if-else statement
temperature = 15

if temperature > 25:
    print("It's hot outside")
else:
    print("It's cool outside")                     # This executes


# if-elif-else statement (multiple conditions)
score = 85

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'                                     # This executes
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Score: {score}, Grade: {grade}")           # Grade: B


# Using 'in' operator in conditions
user_role = "admin"
admin_roles = ["admin", "superuser", "root"]

if user_role in admin_roles:
    print("Access granted to admin panel")         # This executes


# Truthy and Falsy in conditions
name = ""  # Empty string is Falsy

if name:
    print(f"Hello, {name}")
else:
    print("Name is empty")                         # This executes

# Better way to check for empty string
if not name:
    print("Please enter your name")                # This executes


# 3.2 NESTED CONDITIONALS

"""
NESTED CONDITIONALS:
if statements inside other if statements
Allows for more complex decision-making
"""

# Basic nested if
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("You can enter the concert")         # This executes
    else:
        print("You need a ticket")
else:
    print("You must be 18 or older")


# Multiple levels of nesting
score = 85
attendance = 95

if score >= 60:  # Passing score
    if attendance >= 75:  # Good attendance
        if score >= 90:
            print("Excellent! Grade: A")
        elif score >= 80:
            print("Great! Grade: B")               # This executes
        else:
            print("Good! Grade: C")
    else:
        print("Warning: Low attendance")
else:
    print("Failed")


# Real-world example: Shopping discount calculator
total_amount = 150
is_member = True
has_coupon = True

discount = 0

if total_amount >= 100:
    discount = 10  # Base discount for orders over $100
    
    if is_member:
        discount += 5  # Extra 5% for members
        
        if has_coupon:
            discount += 5  # Extra 5% for coupon
            print(f"Total discount: {discount}%")   # 20% total

final_price = total_amount * (1 - discount/100)
print(f"Final price: ${final_price:.2f}")


# 3.3 TERNARY OPERATOR (CONDITIONAL EXPRESSIONS)

"""
TERNARY OPERATOR:
Shorthand for simple if-else statements
Syntax: value_if_true if condition else value_if_false

Also called: Conditional Expression
"""

# Traditional if-else
age = 20
if age >= 18:
    status = "adult"
else:
    status = "minor"
print(f"Status: {status}")


# Ternary operator (one line)
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Status (ternary): {status}")               # adult


# More examples
number = 10
result = "even" if number % 2 == 0 else "odd"
print(f"{number} is {result}")                     # 10 is even

score = 85
grade = "Pass" if score >= 60 else "Fail"
print(f"Grade: {grade}")                           # Pass

temperature = 30
weather = "hot" if temperature > 25 else "cool"
print(f"Weather: {weather}")                       # hot


# Nested ternary (not recommended - hard to read)
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(f"Grade: {grade}")                           # B

# Better: Use regular if-elif-else for multiple conditions


# Ternary in function calls
def process_data(value):
    return value * 2

number = 5
result = process_data(number) if number > 0 else 0
print(f"Result: {result}")                         # 10


# Ternary with multiple operations (using parentheses)
x = 10
result = (x * 2, print("Doubled")) if x > 5 else (x, print("Not doubled"))


# Practical use: Default values
username = ""
display_name = username if username else "Guest"
print(f"Welcome, {display_name}")                  # Welcome, Guest

# Or even simpler (using 'or' operator)
display_name = username or "Guest"
print(f"Welcome, {display_name}")                  # Welcome, Guest



#Switch case

choice = 2

match choice:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case _:
        print("Invalid choice")
# Output: Two
