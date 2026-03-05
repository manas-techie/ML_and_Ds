## Module: is a single python file(ending with .py ) that contains functions, class,and varibals related to specific task
## Package: a folder that contain multiple python files or modules , along with a spaceific file called __init_.py that tell the python treat the directory as package

### Importing Module

#To use code from a module, you have to bring it into your current script. This is called importing

# Method A - Standart import
import math

result = math.sqrt(25)
print(result)

# Method B - Importing as an alias

import datetime as dt 

current_time = dt.datetime.now()
print(current_time)

# Method C - from ... import 

## Brings the functions and  class direct into the script , we dont have to use the module prefix anymore

from random import randint, choice

random_number = randint(1,10)
random_color = choice(['red','purple','blue'])
print(random_number)
print(random_color)


### Creatig my own module
# Step 1: Create the module file
# Step 2: Use the module in another file - make sure both file are in same directory

import my_math


sum_result = my_math.add(2,10)
print(sum_result)



## Note: In older versions of Python, you had to put an empty file named __init__.py inside the math_tools folder for this to work. Python 3.3+ handles this automatically, but you will still see __init__.py files in a lot of professional code
from my_package import my_math

mult = my_math.multiply(2, 10)
print(mult)


### understanding of __name__ == "__main__"
# This is a very common idiom in Python, and it solves a specific problem: How do you stop code from running automatically when you import a module?

# Whenever Python runs a file, it assigns a special hidden variable called __name__ to it.

# If you run the file directly (e.g., python script.py), Python sets __name__ = "__main__".

# If you import the file into another script, Python sets __name__ to the file's actual name (e.g., __name__ = "script").

import greeting

greeting.greeting("Alice")