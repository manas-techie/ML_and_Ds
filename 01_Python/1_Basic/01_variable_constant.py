"""
VARIABLES:
- Variables are containers that store data values
- Python is dynamically typed (no need to declare type explicitly)
- Variable names are case-sensitive
- Must start with a letter or underscore, can contain letters, numbers, underscores
"""

# Basic variable assignment
name = "Manas"                    # String variable
age = 25                          # Integer variable
height = 5.9                      # Float variable
is_student = True                 # Boolean variable

# Multiple assignment (assign multiple variables in one line)
x, y, z = 10, 20, 30
print(f"x={x}, y={y}, z={z}")     # Output: x=10, y=20, z=30

# Same value to multiple variables
a = b = c = 100
print(f"a={a}, b={b}, c={c}")     # Output: a=100, b=100, c=100

# Variable naming conventions
user_name = "John"                # snake_case (recommended for Python)
userName = "Jane"                 # camelCase (not common in Python)
UserName = "Bob"                  # PascalCase (used for class names)
_private_var = "hidden"           # Leading underscore (convention for private)
__special__ = "magic"             # Double underscore (special/magic methods)

# Variable re-assignment (Python is dynamically typed)
count = 5                         # count is an integer
print(f"count is {type(count)}")  # <class 'int'>
count = "five"                    # Now count is a string
print(f"count is {type(count)}")  # <class 'str'>


"""
CONSTANTS:
- Python doesn't have built-in constant types
- Convention: Use UPPERCASE names for constants (developer agreement)
- These can still be changed, but shouldn't be by convention
"""

# Constants (by convention - UPPERCASE)
PI = 3.14159
MAX_SIZE = 100
DATABASE_URL = "localhost:5432"
API_KEY = "your-api-key-here"

# Good practice: Define constants at the top of your file or in a separate config file
SPEED_OF_LIGHT = 299792458        # meters per second
GRAVITATIONAL_CONSTANT = 6.674e-11

