# Iterable: Any Python object capable of returning its members one at a time. Lists, tuples, strings, and dictionaries are all iterables. An iterable is something you can iterate over, but it doesn't keep track of its own state (it doesn't know "where" you are in the sequence).

# Iterator: An object representing a stream of data. It remembers its current state during iteration. It does the actual work of fetching the next value from an iterable.

# Every iterator is an iterable, but not every iterable is an iterator. For example, a list is an iterable, but it is not an iterator.


## iter() and next() 

##Behind the scenes , python's for loop use two built-in-function to make interation work: iter() and next()

my_list = ["apple","Banana","cherry"]

my_iterator = iter(my_list)

print(next(my_iterator)) # apple
print(next(my_iterator)) # Banana
print(next(my_iterator)) # cherry

# print(next(my_iterator)) # no item left it would raise a StopIteration exception



##creating custom iterators

# we can create your own iterables and iterators by using object-oriented programming. To build a custom iterator, your class must implement the Iterator Protocol, which consists of two dunder (double underscore) methods:

# __iter__(self): Must return the iterator object itself.

# __next__(self): Must return the next value in the sequence. When there are no more items, it must raise a StopIteration exception.


class Counter: 
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            value = self.current
            self.current += 1
            return value
        
my_counter = Counter(1,3)

for num in my_counter:
    print(num)



## Generator Function (yield Keyword)
# Generators are a much simpler way to create iterators. A generator is simply a function that uses the yield keyword instead of return.

def count_up_to(low, high):
    current = low
    while current <= high:
        yield current ## pause here and returns 'current'
        current += 1 ## Resumes here on the next call

counter_gen = count_up_to(1,3)


print(next(counter_gen))
print(next(counter_gen))
print(next(counter_gen))



## Generator Expressions
import sys

# List comprehension: Generates 1 million squares in memory
squared_list = [x * x for x in range(1000000)]
print(f"List size: {sys.getsizeof(squared_list)} bytes") 
# Output: List size: ~8448728 bytes (8.4 MB)

# Generator expression: Generates a lazy iterator
squared_gen = (x * x for x in range(1000000))
print(f"Generator size: {sys.getsizeof(squared_gen)} bytes") 
# Output: Generator size: ~208 bytes