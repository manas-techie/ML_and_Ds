# 5.2 TUPLES - Immutable lists (can't be changed)
"""
TUPLES:
- Ordered collection
- Immutable (cannot be changed after creation)
- Allows duplicates
- Faster than lists
- Used for fixed data that shouldn't change
"""


# CREATION

# Empty tuple
empty_tuple = ()
also_empty = tuple()

# Tuple with elements
coordinates = (10, 20)
rgb = (255, 128, 0)
person = ("John", 30, "New York")

# Single element tuple (need comma!)
single = (42,)      # Tuple with one element
not_tuple = (42)    # This is just an integer!
print(f"Single tuple: {single}, type: {type(single)}")
print(f"Not tuple: {not_tuple}, type: {type(not_tuple)}")

# Without parentheses (tuple packing)
point = 10, 20, 30  # Also a tuple
print(f"Point: {point}, type: {type(point)}")

# From other iterables
tuple_from_list = tuple([1, 2, 3])
tuple_from_string = tuple("abc")  # ('a', 'b', 'c')


# INDEXING & SLICING (same as lists)

colors = ("red", "green", "blue", "yellow")

print(f"First: {colors[0]}")      # red
print(f"Last: {colors[-1]}")      # yellow
print(f"Slice: {colors[1:3]}")    # ('green', 'blue')

# Cannot modify (immutable!)
# colors[0] = "purple"  # TypeError: 'tuple' object does not support item assignment



# TUPLE METHODS (only 2!)

numbers = (1, 2, 2, 3, 2, 4)

# count() - count occurrences
print(f"Count of 2: {numbers.count(2)}")  # 3

# index() - find first occurrence
print(f"Index of 3: {numbers.index(3)}")  # 3



# PACKING & UNPACKING (VERY IMPORTANT!)

# Tuple packing - combine values into tuple
person = "John", 30, "Developer"  # Packing
print(f"Packed: {person}")

# Tuple unpacking - extract values from tuple
name, age, job = person  # Unpacking
print(f"Name: {name}, Age: {age}, Job: {job}")

# Unpacking with lists too
coordinates = [10, 20]
x, y = coordinates
print(f"x={x}, y={y}")

# Swapping values (elegant Python trick!)
a, b = 5, 10
print(f"Before: a={a}, b={b}")
a, b = b, a  # Swap without temporary variable
print(f"After: a={a}, b={b}")

# Partial unpacking with * (rest operator)
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")
# first=1, middle=[2, 3, 4], last=5

# Ignore values with _
x, _, z = (10, 20, 30)  # Ignore middle value
print(f"x={x}, z={z}")

# Unpacking in loops
points = [(1, 2), (3, 4), (5, 6)]
for x, y in points:
    print(f"Point: ({x}, {y})")


# WHEN TO USE TUPLES

# 1. Return multiple values from function
def get_user():
    return "John", 30, "john@email.com"  # Returns tuple

name, age, email = get_user()  # Unpack

# 2. Fixed data that shouldn't change
DAYS_OF_WEEK = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

# 3. Dictionary keys (lists can't be keys, tuples can)
locations = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles"
}
print(f"NYC: {locations[(40.7128, -74.0060)]}")

# 4. Faster than lists (slight performance benefit)
# 5. Safer - prevents accidental modification
