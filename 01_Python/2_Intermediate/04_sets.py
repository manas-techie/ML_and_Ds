# 5.4 SETS - Unique elements, fast membership testing
"""
SETS:
- Unordered collection
- Contains only unique elements (no duplicates)
- Mutable (can add/remove elements)
- Very fast membership testing (x in set)
- Used for removing duplicates, set operations
"""

# CREATION

# Empty set (NOTE: {} creates empty dict, not set!)
empty_set = set()  # Correct
# NOT: empty = {}  # This is a dict!

# Set with elements
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "cherry"}

# From other iterables (removes duplicates!)
list_with_dupes = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(list_with_dupes)  # {1, 2, 3, 4}
print(f"Unique: {unique_numbers}")

# From string (unique characters)
unique_chars = set("hello")  # {'h', 'e', 'l', 'o'}
print(f"Unique chars: {unique_chars}")

# Set comprehension
evens = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}
print(f"Evens: {evens}")


# BASIC SET OPERATIONS

fruits = {"apple", "banana", "cherry"}

# Add single element
fruits.add("date")
print(f"After add: {fruits}")

# Add multiple elements
fruits.update(["elderberry", "fig"])  # Can use list, tuple, set
print(f"After update: {fruits}")

# Remove element (raises error if not found)
fruits.remove("banana")
print(f"After remove: {fruits}")

# fruits.remove("grape")  # KeyError!

# Discard element (no error if not found)
fruits.discard("apple")
fruits.discard("grape")  # No error, just does nothing
print(f"After discard: {fruits}")

# Pop random element (since unordered)
random_fruit = fruits.pop()
print(f"Popped: {random_fruit}, Remaining: {fruits}")

# Clear all elements
temp = {1, 2, 3}
temp.clear()
print(f"Cleared: {temp}")  # set()

# Length
numbers = {1, 2, 3, 4, 5}
print(f"Length: {len(numbers)}")  # 5

# Membership testing (VERY FAST!)
print(f"3 in numbers: {3 in numbers}")  # True
print(f"10 in numbers: {10 in numbers}")  # False



# SET OPERATIONS (Mathematical operations)

# Two sets for examples
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# --- Union - All unique elements from both sets ---
# Elements in set_a OR set_b
union = set_a | set_b  # Using operator
# OR
union = set_a.union(set_b)  # Using method
print(f"Union: {union}")  # {1, 2, 3, 4, 5, 6, 7, 8}


# --- Intersection - Common elements in both sets ---
# Elements in set_a AND set_b
intersection = set_a & set_b  # Using operator
# OR
intersection = set_a.intersection(set_b)  # Using method
print(f"Intersection: {intersection}")  # {4, 5}


# --- Difference - Elements in first but not in second ---
# Elements in set_a but NOT in set_b
difference = set_a - set_b  # Using operator
# OR
difference = set_a.difference(set_b)  # Using method
print(f"Difference (a-b): {difference}")  # {1, 2, 3}

difference_b = set_b - set_a
print(f"Difference (b-a): {difference_b}")  # {6, 7, 8}


# --- Symmetric Difference - Elements in either but not both ---
# Elements in set_a OR set_b but NOT in both
sym_diff = set_a ^ set_b  # Using operator
# OR
sym_diff = set_a.symmetric_difference(set_b)  # Using method
print(f"Symmetric difference: {sym_diff}")  # {1, 2, 3, 6, 7, 8}



# SET COMPARISONS

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
set_c = {1, 2, 3}

# Subset - is set_a contained in set_b?
print(f"set_a <= set_b: {set_a <= set_b}")  # True
print(f"set_a.issubset(set_b): {set_a.issubset(set_b)}")  # True

# Superset - does set_b contain set_a?
print(f"set_b >= set_a: {set_b >= set_a}")  # True
print(f"set_b.issuperset(set_a): {set_b.issuperset(set_a)}")  # True

# Disjoint - no common elements?
set_x = {1, 2, 3}
set_y = {4, 5, 6}
print(f"Disjoint: {set_x.isdisjoint(set_y)}")  # True



# PRACTICAL SET EXAMPLES

# Example 1: Remove duplicates from list
numbers_with_dupes = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique = list(set(numbers_with_dupes))  # Convert to set, then back to list
print(f"Remove duplicates: {unique}")


# Example 2: Find common friends
alice_friends = {"Bob", "Charlie", "David", "Eve"}
bob_friends = {"Alice", "Charlie", "Frank", "David"}

mutual_friends = alice_friends & bob_friends
print(f"Mutual friends: {mutual_friends}")  # {'Charlie', 'David'}


# Example 3: Find unique visitors per day
monday_visitors = {"John", "Alice", "Bob", "Charlie"}
tuesday_visitors = {"Alice", "David", "Bob", "Eve"}

# Only Monday
only_monday = monday_visitors - tuesday_visitors
print(f"Only Monday: {only_monday}")

# Only Tuesday
only_tuesday = tuesday_visitors - monday_visitors
print(f"Only Tuesday: {only_tuesday}")

# Both days
both_days = monday_visitors & tuesday_visitors
print(f"Both days: {both_days}")

# Total unique visitors
total_unique = monday_visitors | tuesday_visitors
print(f"Total unique: {total_unique}")


# Example 4: Check valid input
valid_commands = {"start", "stop", "pause", "resume", "quit"}
user_input = "start"

if user_input in valid_commands:  # Fast membership test!
    print(f"Executing: {user_input}")
else:
    print("Invalid command")


# Example 5: Find missing numbers in sequence
complete_set = set(range(1, 11))  # {1, 2, 3, ..., 10}
available = {1, 3, 5, 7, 9}
missing = complete_set - available
print(f"Missing numbers: {missing}")  # {2, 4, 6, 8, 10}