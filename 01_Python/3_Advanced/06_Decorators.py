#Function Decorators
# A function decorator is a function that takes another function as an argument, adds some logic, and returns a new function. In Python, we use the @decorator_name syntax above the target function.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# We can use the decorator to modify the behavior of the say_hello function without changing its code.
@my_decorator
def say_hello():
    print("Hello!") 

say_hello()


# Creating a decorator that takes arguments
# To make a decorator truly reusable, it needs to handle functions that take arguments. We use *args and **kwargs to ensure the decorator can wrap any function, regardless of its signature.

# It is also best practice to use functools.wraps so the decorated function keeps its original metadata (like its name and docstrings).

from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Logging: Called function '{func.__name__}' with args: {args} and kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a+b

result = add(5, 3)
print(f"Result: {result}")

# Decoder with arguments
# sometimes we want our decorator to accept its own arguments. To achieve this, we need to create a decorator factory, which is a function that returns a decorator.

def repeat(num_times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet (name):
    print(f"Hello, {name}!")

greet("Manas Sidh")


# class decorators
# Class decorators are a way to modify or enhance the behavior of classes. They work similarly to function decorators but are applied to classes instead of functions. These are greate for adding methods, modifying attributes, or even changing the class's behavior.

from datetime import datetime

def add_created_at(cls):
    cls.created_at = datetime.now()
    return cls

@add_created_at
class MyClass: 
    def __init__(self, value):
        self.value = value

my_class = MyClass(20)
print(my_class.value)
print(my_class.created_at)