## Python comes with "batteries included" - a massive standard libaries of pre written modules , we can use right out of the box

## math
import math

print(math.pi)
print(math.floor(4.9))
print(math.ceil(4.1))
print(math.sqrt(25))
print(math.exp(2))


## random 
import random

print(random.randint(1, 10))
print(random.choice(['red','blue','yellow']))
list = ['red','blue','yellow']
random.shuffle(list) ## suffle the list in place
print(list)

##datetime

from datetime import datetime, timedelta

now = datetime.now()
print(now)

formated_date = now.strftime("%Y-%m-%d %H:%M")
print(formated_date)


# Calculating past or future dates
tomorrow = now + timedelta(days=1)
print(tomorrow)

## os

import os

##return current working dirctory
current_folder = os.getcwd()
print(current_folder)


## return all file and folders under current working directory
contents = os.listdir('.')
print(contents)


# sys

import sys

# sys.argv is a list of arguments passed to the script from the terminal
# e.g., if you run: python script.py data.csv
print(f"Script name: {sys.argv[0]}")

# Exiting a program prematurely
if len(sys.argv) < 2:
    print("Error: Not enough arguments provided.")
    sys.exit(1) # Stops the script immediately with an error code


print(sys.platform) ## which os we are using
print(sys.version) ## which version of python we are using


## sys.path
print("Python is currently looking for modules in these folders:")
for folder in sys.path:
    print(folder)

# You can also add your own folders to this list!
# sys.path.append("C:/Users/MyName/CustomFolder")