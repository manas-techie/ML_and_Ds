# 5.3 DICTIONARIES - Key-value pairs (most powerful!)

"""
DICTIONARIES:
- Key-value pairs (like a real dictionary: word -> definition)
- Unordered (but maintains insertion order in Python 3.7+)
- Mutable (can be changed)
- Keys must be unique and immutable (strings, numbers, tuples)
- Values can be anything
- VERY fast lookups
"""


# CREATION

# Empty dictionary
empty_dict = {}
also_empty = dict()

# Dictionary with data
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(f"Person: {person}")

# Different value types
student = {
    "name": "Alice",
    "age": 20,
    "grades": [85, 90, 92],  # List as value
    "is_active": True
}

# Using dict() constructor
user = dict(name="Bob", age=25, email="bob@email.com")
print(f"User: {user}")

# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_from_pairs = dict(pairs)
print(f"From pairs: {dict_from_pairs}")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(f"Squares dict: {squares}")



# ACCESSING VALUES

person = {"name": "John", "age": 30, "city": "New York"}

# Using square brackets
print(f"Name: {person['name']}")  # John
print(f"Age: {person['age']}")    # 30

# KeyError if key doesn't exist
# print(person['job'])  # KeyError!

# get() method - SAFER (returns None if key doesn't exist)
print(f"Job: {person.get('job')}")  # None (no error!)
print(f"Name: {person.get('name')}")  # John

# get() with default value
job = person.get('job', 'Unemployed')  # Returns 'Unemployed' if key missing
print(f"Job with default: {job}")

# Check if key exists
if "age" in person:
    print(f"Age is {person['age']}")

print(f"'email' in person: {'email' in person}")  # False



# MODIFYING DICTIONARIES

person = {"name": "John", "age": 30}

# Add new key-value pair
person["city"] = "New York"
person["job"] = "Developer"
print(f"Added: {person}")

# Update existing value
person["age"] = 31
print(f"Updated age: {person}")

# Delete key-value pair
del person["job"]
print(f"Deleted job: {person}")



# ESSENTIAL DICTIONARY METHODS

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "job": "Developer"
}

# --- keys() - Get all keys ---
keys = person.keys()
print(f"Keys: {keys}")  # dict_keys(['name', 'age', 'city', 'job'])
print(f"Keys as list: {list(keys)}")  # Convert to list

# Iterate over keys
for key in person.keys():
    print(f"Key: {key}")

# Or simply (same thing)
for key in person:
    print(f"Key: {key}")


# --- values() - Get all values ---
values = person.values()
print(f"Values: {values}")

# Iterate over values
for value in person.values():
    print(f"Value: {value}")


# --- items() - Get key-value pairs (MOST USED!) ---
items = person.items()
print(f"Items: {items}")

# Iterate over key-value pairs (very common!)
for key, value in person.items():
    print(f"{key}: {value}")


# --- update() - Merge dictionaries ---
person = {"name": "John", "age": 30}
additional_info = {"city": "NYC", "job": "Developer"}

person.update(additional_info)  # Merges additional_info into person
print(f"Updated: {person}")

# Can also update single values
person.update({"age": 31})
print(f"Age updated: {person}")

# Python 3.9+ merge operator
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2  # {a: 1, b: 2, c: 3, d: 4}
print(f"Merged: {merged}")


# --- pop() - Remove and return value ---
person = {"name": "John", "age": 30, "city": "NYC"}

age = person.pop("age")  # Removes 'age' and returns value
print(f"Popped age: {age}, Person: {person}")

# pop() with default (if key doesn't exist)
job = person.pop("job", "Unknown")  # Returns "Unknown" since 'job' not in dict
print(f"Popped job: {job}")


# --- popitem() - Remove and return last inserted pair (Python 3.7+) ---
person = {"name": "John", "age": 30, "city": "NYC"}
last_item = person.popitem()
print(f"Popped item: {last_item}, Remaining: {person}")


# --- clear() - Remove all items ---
temp = {"a": 1, "b": 2}
temp.clear()
print(f"Cleared: {temp}")  # {}


# --- setdefault() - Get value, set if doesn't exist ---
person = {"name": "John"}

# Get existing key
name = person.setdefault("name", "Unknown")  # Returns "John"
print(f"Name: {name}")

# Get non-existing key (sets it with default value)
age = person.setdefault("age", 25)  # Adds "age": 25 and returns 25
print(f"Age: {age}, Person: {person}")



# NESTED DICTIONARIES

# Dictionary of dictionaries
users = {
    "user1": {
        "name": "Alice",
        "age": 25,
        "city": "NYC"
    },
    "user2": {
        "name": "Bob",
        "age": 30,
        "city": "LA"
    }
}

# Access nested values
print(f"User1 name: {users['user1']['name']}")

# Iterate nested dict
for user_id, user_info in users.items():
    print(f"{user_id}:")
    for key, value in user_info.items():
        print(f"  {key}: {value}")



# PRACTICAL DICTIONARY EXAMPLES

# Example 1: Word counter
text = "hello world hello python world"
word_count = {}

for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1

print(f"Word count: {word_count}")  # {'hello': 2, 'world': 2, 'python': 1}


# Example 2: Student grades
students = {
    "Alice": [85, 90, 92],
    "Bob": [78, 82, 88],
    "Charlie": [95, 97, 93]
}

# Calculate averages
for student, grades in students.items():
    average = sum(grades) / len(grades)
    print(f"{student}: {average:.2f}")


# Example 3: Configuration settings
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "username": "admin"
    },
    "debug": True,
    "max_connections": 100
}

print(f"DB Host: {config['database']['host']}")
print(f"Debug mode: {config['debug']}")
