# 5.1 LISTS - Most versatile, used for ordered collections

"""
LISTS:
- Ordered collection (maintains insertion order)
- Mutable (can be changed after creation)
- Allows duplicate elements
- Can contain mixed data types
- Most commonly used data structure
"""

# CREATION


# Empty list
empty_list = []
also_empty = list()

# List with elements
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]  # Mixed types (possible but not common)

# List from other iterables
chars = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']
print(f"Characters: {chars}")

# List with range
nums = list(range(5))  # [0, 1, 2, 3, 4]
print(f"Range list: {nums}")

# List comprehension (create lists quickly)
squares = [x**2 for x in range(1,5)]  # [1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
print(f"Squares: {squares}")
print(f"Evens: {evens}")



# INDEXING & SLICING

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Indexing (access single element)
print(f"First: {fruits[0]}")        # apple (index 0)
print(f"Second: {fruits[1]}")       # banana
print(f"Last: {fruits[-1]}")        # elderberry (negative = from end)
print(f"Second last: {fruits[-2]}") # date

# Slicing [start:stop:step]
print(f"First 3: {fruits[0:3]}")    # ['apple', 'banana', 'cherry']
print(f"First 3: {fruits[:3]}")     # Same (0 is default start)
print(f"From index 2: {fruits[2:]}")# ['cherry', 'date', 'elderberry']
print(f"Last 2: {fruits[-2:]}")     # ['date', 'elderberry']
print(f"Every 2nd: {fruits[::2]}")  # ['apple', 'cherry', 'elderberry']
print(f"Reversed: {fruits[::-1]}")  # Reverse the list

# Modify via index
fruits[1] = "blueberry"  # Replace banana with blueberry
print(f"Modified: {fruits}")

# Modify via slicing
fruits[0:2] = ["apricot", "avocado"]  # Replace first two
print(f"Sliced modify: {fruits}")


# ESSENTIAL LIST METHODS

# --- append() - Add single element to end (MOST USED) ---
numbers = [1, 2, 3]
numbers.append(4)           # [1, 2, 3, 4]
numbers.append(5)           # [1, 2, 3, 4, 5]
print(f"After append: {numbers}")

# Common use: Building lists dynamically
scores = []
scores.append(85)
scores.append(92)
scores.append(78)
print(f"Scores: {scores}")


# --- extend() - Add multiple elements (merge lists) ---
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)         # [1, 2, 3, 4, 5, 6]
print(f"After extend: {list1}")

# Alternative: Using + operator
combined = [1, 2] + [3, 4]  # [1, 2, 3, 4]
print(f"Combined: {combined}")


# --- insert() - Add element at specific position ---
fruits = ["apple", "cherry"]
fruits.insert(1, "banana")  # Insert at index 1
print(f"After insert: {fruits}")  # ['apple', 'banana', 'cherry']

# Insert at beginning
fruits.insert(0, "apricot")
print(f"Insert at start: {fruits}")


# --- remove() - Remove first occurrence of value ---
numbers = [1, 2, 3, 2, 4]
numbers.remove(2)           # Removes first 2
print(f"After remove: {numbers}")  # [1, 3, 2, 4]

# Warning: Raises error if value not found
# numbers.remove(10)  # ValueError!

# Safe removal
if 3 in numbers:
    numbers.remove(3)


# --- pop() - Remove and return element (VERY USEFUL) ---
numbers = [1, 2, 3, 4, 5]

# pop() without argument - removes last element
last = numbers.pop()        # Returns 5, list becomes [1, 2, 3, 4]
print(f"Popped: {last}, List: {numbers}")

# pop(index) - removes element at index
second = numbers.pop(1)     # Returns 2, list becomes [1, 3, 4]
print(f"Popped at index 1: {second}, List: {numbers}")

# Use case: Stack operations (LIFO - Last In First Out)
stack = []
stack.append(1)  # Push
stack.append(2)
stack.append(3)
top = stack.pop()  # Pop - returns 3
print(f"Stack: {stack}, Popped: {top}")


# --- sort() - Sort list in place (modifies original) ---
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()              # Ascending order
print(f"Sorted: {numbers}")  # [1, 1, 2, 3, 4, 5, 9]

# Descending order
numbers.sort(reverse=True)
print(f"Descending: {numbers}")

# Sort strings (alphabetical)
fruits = ["cherry", "apple", "banana"]
fruits.sort()
print(f"Sorted fruits: {fruits}")

# sorted() function - returns new sorted list (doesn't modify original)
original = [3, 1, 4]
sorted_copy = sorted(original)
print(f"Original: {original}, Sorted copy: {sorted_copy}")


# --- reverse() - Reverse list in place ---
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(f"Reversed: {numbers}")  # [5, 4, 3, 2, 1]

# Alternative: Slicing (creates new list)
reversed_copy = numbers[::-1]



# OTHER USEFUL LIST OPERATIONS

# Length
fruits = ["apple", "banana", "cherry"]
print(f"Length: {len(fruits)}")  # 3

# Count occurrences
numbers = [1, 2, 2, 3, 2, 4]
print(f"Count of 2: {numbers.count(2)}")  # 3

# Find index of element
print(f"Index of 3: {numbers.index(3)}")  # 3
# numbers.index(10)  # ValueError if not found

# Check membership
print(f"2 in list: {2 in numbers}")  # True
print(f"10 in list: {10 in numbers}")  # False

# Clear list (remove all elements)
temp = [1, 2, 3]
temp.clear()
print(f"Cleared: {temp}")  # []

# Copy list (important!)
original = [1, 2, 3]
shallow_copy = original.copy()  # Creates new list
reference = original            # Same list!

original.append(4)
print(f"Original: {original}")       # [1, 2, 3, 4]
print(f"Copy: {shallow_copy}")       # [1, 2, 3]
print(f"Reference: {reference}")     # [1, 2, 3, 4] (same as original!)

# Min, max, sum (for numeric lists)
numbers = [5, 2, 8, 1, 9]
print(f"Min: {min(numbers)}, Max: {max(numbers)}, Sum: {sum(numbers)}")



# PRACTICAL LIST EXAMPLES

# Example 1: Shopping cart
cart = []
cart.append("Apple")
cart.append("Bread")
cart.append("Milk")
print(f"Cart: {cart}")
cart.remove("Bread") 
print(f"Final cart: {cart}")

# Example 2: To-do list with priorities
tasks = []
tasks.insert(0, "Urgent: Pay bills")      # High priority at top
tasks.append("Buy groceries")
tasks.append("Clean room")
print(f"Tasks: {tasks}")
completed = tasks.pop(0)  # Complete first task
print(f"Completed: {completed}")

# Example 3: Finding top 3 scores
scores = [85, 92, 78, 95, 88, 91]
sorted_scores = sorted(scores, reverse=True)
top_3 = sorted_scores[:3]
print(f"Top 3 scores: {top_3}") 