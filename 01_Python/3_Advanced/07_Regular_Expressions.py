# Regular expressions are essentially a mini-programming language embedded inside Python (and most other programming languages). You use them to define a search pattern, which can then be used to validate input, extract data, or replace text.


# using regular expressions(regex) in Python 
from importlib import abc
import re

#metacharacters
# . ^ $ * + ? { } [ ] \ | ( )

# . -> matches any character except a newline e.g "c.t" would match "cat", "cot", "cut", etc. but not "ct" or "c\nt".
# ^ -> matches the start of the string e.g "^Hello" would match "Hello world" but not "Say Hello".
# $ -> matches the end of the string e.g "world$" would match "Hello world" but not "worldwide".
# * -> matches 0 or more repetitions of the preceding element e.g "ca*t" would match "ct", "cat", "caat", "caaat", etc. but not "catt" or "ccaat".
# + -> matches 1 or more repetitions of the preceding element e.g "ca+t" would match "cat", "caat", "caaat", etc. but not "ct" or "catt".
# ? -> matches 0 or 1 repetition of the preceding element e.g "ca?t" would match "ct", "cat", but not "caat" or "catt".
# {n} -> matches exactly n repetitions of the preceding element e.g "ca{2}t" would match "caat" but not "ct", "cat", or "caaat".
# {n,} -> matches n or more repetitions of the preceding element e.g "ca{2,}t" would match "caat", "caaat", etc. but not "ct" or "cat".
# {n,m} -> matches between n and m repetitions of the preceding element e.g "ca{2,3}t" would match "caat" and "caaat" but not "ct", "cat", or "caaaat".
# [abc] -> matches any one of the characters a, b, or c e.g "[cb]at" would match "cat" and "bat" but not "rat".
# [^abc] -> matches any character that is not a, b, or c e.g "[^cb]at" would match "rat" but not "cat" or "bat".
# \ -> is used to escape a metacharacter e.g "c\*t" would match "c*t" but not "cat" or "cot".   
# | -> matches either the pattern before or the pattern after the | e.g "cat|dog" would match "cat" and "dog" but not "cot" or "dat".
# ( ) -> is used to group patterns e.g "c(a|o)t" would match "cat" and "cot" but not "ct" or "catt".


#special sequences
# \d -> matches any digit character e.g "\d" would match "0", "1", "2", etc.
# \D -> matches any non-digit character e.g "\D" would match "a", "b", "c", etc.
# \s -> matches any whitespace character e.g "\s" would match " ", "\t", "\n", etc.
# \S -> matches any non-whitespace character e.g "\S" would match "a", "b", "c", etc.
# \w -> matches any alphanumeric character (letters, digits, and underscores) e.g "\w" would match "a", "b", "c", "1", "2", "3", etc.
# \W -> matches any non-alphanumeric character e.g "\W" would match " ", "!", "@", etc.
# \b -> matches a word boundary e.g "\bcat\b" would match "cat" but not "catapult" or "concatenate".
# \B -> matches a non-word boundary e.g "\Bcat\B" would match "concatenate" but not "cat" or "catapult".    



#email validation using regex
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

#core functions of re module

# re.search
# Scans through the entire string looking for the first location where the regular expression pattern produces a match. It returns a match object if found, or None if no match is found

text = "The rain in Spain stays mainly in the plain."
pattern = r"main"

match = re.search(pattern, text)

if match:
    print(f"Match found: {match.group()} at position {match.start()}-{match.end()}")
else:   
    print("No match found.")


#re.match()

# Checks for a match only at the beginning of the string. It returns a match object if the pattern matches at the start of the string, or None if it does not.

pattern = r"The"

match = re.match(pattern, text)

if match:
    print(f"Match found: {match.group()} at position {match.start()}-{match.end()}")
else:
    print("No match found.")


#re.findall()
# Returns a list of all non-overlapping matches of the pattern in the string. If no matches are found, it returns an empty list.

pattern = r"ain"

matches = re.findall(pattern, text) 

if matches:
    print(f"Matches found: {matches}")
else:
    print("No matches found.")

#re.sub()
# Replaces occurrences of the pattern in the string with a specified replacement string. It returns the modified string.

pattern = r"ain"
replacement = "XYZ"

modified_text = re.sub(pattern, replacement, text)
print(f"Modified text: {modified_text}")