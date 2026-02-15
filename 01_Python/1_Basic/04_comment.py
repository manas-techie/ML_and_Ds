"""
COMMENTS:
- Used to explain code, make it more readable
- Ignored by Python interpreter
- Essential for documentation and collaboration
"""

# 4.1 SINGLE-LINE COMMENTS


# This is a single-line comment
# It starts with a hash symbol (#)
# Everything after # on that line is ignored


# 4.2 MULTI-LINE COMMENTS

"""
This is a multi-line comment (actually a multi-line string).
Python doesn't have true multi-line comment syntax.
We use triple quotes (''' or \"\"\") for multi-line strings.
When not assigned to a variable, they act like comments.

You can write multiple lines here.
Useful for:
- Long explanations
- Documentation
- Commenting out large blocks of code
"""

'''
This also works with single triple quotes.
Triple quotes can span multiple lines.
'''


# Docstrings (special type of multi-line comment)
def calculate_area(radius):
    """
    Calculate the area of a circle.
    
    Args:
        radius (float): The radius of the circle
        
    Returns:
        float: The area of the circle
        
    Example:
        >>> calculate_area(5)
        78.53975
    """
    return 3.14159 * radius ** 2

# Docstrings are used for function/class/module documentation
# They can be accessed using __doc__ attribute
print(calculate_area.__doc__)