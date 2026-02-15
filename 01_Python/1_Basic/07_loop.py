# 4. LOOPS

"""
LOOPS:
Execute a block of code repeatedly
Two main types: for loops and while loops
"""

# 4.1 FOR LOOPS

"""
FOR LOOPS:
Iterate over a sequence (list, tuple, string, range, etc.)

Syntax:
    for variable in sequence:
        # code block
"""

# Iterate over a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry


# Iterate over a string
word = "Python"

for letter in word:
    print(letter, end=" ")  # end=" " keeps output on same line
print()  # New line
# Output: P y t h o n


# Iterate over a tuple
coordinates = (10, 20, 30)

for coord in coordinates:
    print(f"Coordinate: {coord}")


# Using range() - most common for loop pattern
"""
range(stop) - from 0 to stop-1
range(start, stop) - from start to stop-1
range(start, stop, step) - from start to stop-1, incrementing by step
"""

# range(stop)
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()


# range(start, stop)
for i in range(2, 7):
    print(i, end=" ")  # 2 3 4 5 6
print()


# range(start, stop, step)
for i in range(0, 10, 2):  # Even numbers
    print(i, end=" ")  # 0 2 4 6 8
print()


# Counting backwards
for i in range(10, 0, -1):
    print(i, end=" ")  # 10 9 8 7 6 5 4 3 2 1
print()


# Using enumerate() - get index and value
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry


# enumerate() with custom start index
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
# Output:
# 1. apple
# 2. banana
# 3. cherry


# Iterating over dictionaries
person = {"name": "John", "age": 30, "city": "New York"}

# Iterate over keys (default)
for key in person:
    print(key)

# Iterate over values
for value in person.values():
    print(value)

# Iterate over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
# Output:
# name: John
# age: 30
# city: New York


# Using zip() - iterate over multiple sequences
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")
# Output:
# Alice is 25 years old and lives in NYC
# Bob is 30 years old and lives in LA
# Charlie is 35 years old and lives in Chicago


# List comprehension (advanced for loop)
# Create a new list from existing list
numbers = [1, 2, 3, 4, 5]
squared = [num ** 2 for num in numbers]
print(f"Squared: {squared}")  # [1, 4, 9, 16, 25]

# With condition
evens = [num for num in numbers if num % 2 == 0]
print(f"Evens: {evens}")  # [2, 4]

# 4.2 WHILE LOOPS

"""
WHILE LOOPS:
Repeat as long as a condition is True
Use when you don't know how many iterations in advance

Syntax:
    while condition:
        # code block
        
WARNING: Make sure the condition eventually becomes False, or you'll have an infinite loop!
"""

# Basic while loop
count = 0

while count < 5:
    print(f"Count: {count}")
    count += 1  # IMPORTANT: Update condition variable
# Output: Count: 0, 1, 2, 3, 4


# Countdown
countdown = 5

while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blast off!")


# User input validation (common use case)
"""
password = ""
while len(password) < 8:
    password = input("Enter password (min 8 characters): ")
print("Password accepted")
"""


# While with condition check
number = 1

while number <= 100:
    if number > 10:  # Stop when reaches 11
        break
    print(number)
    number += 1


# While True with break (common pattern)
"""
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input.lower() == 'quit':
        break
    print(f"You entered: {user_input}")
"""


# Summing numbers until threshold
total = 0
number = 1

while total < 100:
    total += number
    number += 1

print(f"Total: {total}, Numbers added: {number - 1}")


# While with multiple conditions
balance = 100
withdrawals = 0

while balance > 0 and withdrawals < 5:
    balance -= 20
    withdrawals += 1
    print(f"Withdrawal {withdrawals}: Balance = ${balance}")



# 4.3 LOOP CONTROL STATEMENTS (break, continue, pass)

"""
LOOP CONTROL STATEMENTS:
Modify the normal flow of loops

┌──────────┬─────────────────────────────────────────┐
│ Statement│ Description                             │
├──────────┼─────────────────────────────────────────┤
│ break    │ Exit the loop completely                │
│ continue │ Skip rest of current iteration          │
│ pass     │ Do nothing (placeholder)                │
└──────────┴─────────────────────────────────────────┘
"""


# BREAK - Exit loop immediately

print("\n--- BREAK examples ---")

# Find first even number
numbers = [1, 3, 5, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break  # Exit loop
# Output: First even number: 8


# Search in list
names = ["Alice", "Bob", "Charlie", "David"]
search_name = "Charlie"

for name in names:
    if name == search_name:
        print(f"Found {search_name}!")
        break
else:  # This executes only if loop completes without break
    print(f"{search_name} not found")


# Break from while loop
count = 0
while True:  # Infinite loop
    print(count)
    count += 1
    if count >= 5:
        break  # Exit when count reaches 5


# Multiple conditions for break
for i in range(1, 100):
    if i % 7 == 0 and i % 5 == 0:  # First number divisible by both
        print(f"First number divisible by 7 and 5: {i}")
        break



# CONTINUE - Skip to next iteration

print("\n--- CONTINUE examples ---")

# Skip even numbers
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip rest of loop body for even numbers
    print(i, end=" ")  # Only odd numbers print
print()  # Output: 1 3 5 7 9


# Skip specific values
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num == 5 or num == 7:
        continue  # Skip 5 and 7
    print(num, end=" ")  # Output: 1 2 3 4 6 8 9 10
print()


# Process valid data only
data = [10, -5, 20, 0, 30, -3, 40]

for value in data:
    if value <= 0:
        continue  # Skip non-positive values
    print(f"Processing {value}")


# Continue with while
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count, end=" ")  # Only odd: 1 3 5 7 9
print()



# PASS - Do nothing (placeholder)


print("\n--- PASS examples ---")

# Placeholder for future code
for i in range(5):
    if i == 3:
        pass  # TODO: Add special handling for 3
    else:
        print(i)


# Empty function placeholder
def future_function():
    pass  # Will implement later


# Empty class placeholder
class MyClass:
    pass  # Will add methods later


# Conditional placeholder
age = 25
if age < 18:
    pass  # Will add restriction logic later
elif age >= 18:
    print("Access granted")


# Pass vs continue difference
print("With pass:")
for i in range(5):
    if i == 2:
        pass  # Does nothing, continues normally
    print(i)  # Prints all: 0 1 2 3 4

print("With continue:")
for i in range(5):
    if i == 2:
        continue  # Skips rest of iteration
    print(i)  # Prints: 0 1 3 4



# 4.4 NESTED LOOPS

"""
NESTED LOOPS:
Loops inside other loops
Inner loop completes all iterations for each iteration of outer loop
"""

# Basic nested for loop
print("\n--- NESTED LOOPS examples ---")

for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"i={i}, j={j}")


# Multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j:2d}", end="  ")
    print()  # New line after each row


# 2D pattern (rectangle of stars)
rows = 4
cols = 6

for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()  # New line after each row


# Triangle pattern
size = 5

for i in range(1, size + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# Iterating over 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()


# With index
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")


# Nested loop with break (breaks inner loop only)
for i in range(3):
    print(f"Outer loop: {i}")
    for j in range(5):
        if j == 2:
            break  # Only breaks inner loop
        print(f"  Inner loop: {j}")


# Finding pairs
numbers = [1, 2, 3]
for i in numbers:
    for j in numbers:
        if i != j:  # Don't pair with itself
            print(f"Pair: ({i}, {j})")


# Nested while loops
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"({i},{j})", end=" ")
        j += 1
    print()
    i += 1


# 4.5 ELSE CLAUSE WITH LOOPS

"""
ELSE CLAUSE WITH LOOPS:
Python feature: Loops can have an 'else' clause
- Executes when loop completes normally (not interrupted by break)
- Does NOT execute if loop is exited with break
"""

# For loop with else
print("\n--- ELSE with loops ---")

numbers = [1, 3, 5, 7, 9]

for num in numbers:
    if num % 2 == 0:
        print(f"Found even number: {num}")
        break
else:
    print("No even numbers found")  # This executes (no break occurred)


# While loop with else
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop completed normally")  # This executes


# With break - else doesn't execute
for i in range(10):
    if i == 5:
        print("Breaking at 5")
        break
else:
    print("This won't print")  # Doesn't execute (break occurred)


# Practical use: Search with validation
def find_item(items, target):
    for item in items:
        if item == target:
            print(f"Found {target}")
            break
    else:
        print(f"{target} not found in list")

find_item([1, 2, 3, 4], 3)  # Found 3
find_item([1, 2, 3, 4], 5)  # 5 not found in list


# Prime number checker using loop-else
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # Found divisor, not prime
    else:
        return True  # No divisors found, is prime

print(f"7 is prime: {is_prime(7)}")    # True
print(f"10 is prime: {is_prime(10)}")  # False



# 5. PRACTICAL EXAMPLES & PATTERNS


print("\n--- PRACTICAL EXAMPLES ---")

# Example 1: FizzBuzz (classic programming problem)
for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# Example 2: Sum of numbers in a range
total = 0
for i in range(1, 101):
    total += i
print(f"Sum of 1 to 100: {total}")  # 5050

# Or using formula: n * (n + 1) / 2


# Example 3: Factorial
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")  # 120


# Example 4: Reverse a string
text = "Python"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(f"Reversed: {reversed_text}")  # nohtyP

# Or simply: text[::-1]


# Example 5: Count vowels
text = "Hello World"
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1
print(f"Vowels in '{text}': {count}")  # 3


# Example 6: Find maximum in list
numbers = [23, 45, 12, 67, 34, 89, 10]
maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
print(f"Maximum: {maximum}")  # 89

# Or simply: max(numbers)


# Example 7: Grade calculator
scores = [85, 92, 78, 90, 88]
total_score = 0

for score in scores:
    total_score += score

average = total_score / len(scores)
print(f"Average score: {average:.2f}")  # 86.60

if average >= 90:
    final_grade = 'A'
elif average >= 80:
    final_grade = 'B'
elif average >= 70:
    final_grade = 'C'
else:
    final_grade = 'F'

print(f"Final grade: {final_grade}")


# Example 8: Password strength checker
def check_password_strength(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in "!@#$%^&*":
            has_special = True
    
    strength = 0
    if has_upper: strength += 1
    if has_lower: strength += 1
    if has_digit: strength += 1
    if has_special: strength += 1
    
    if len(password) >= 8 and strength >= 3:
        return "Strong"
    elif len(password) >= 6 and strength >= 2:
        return "Medium"
    else:
        return "Weak"

print(check_password_strength("Pass123!"))  # Strong