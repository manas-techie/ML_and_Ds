import sys

# List comprehension: Generates 1 million squares in memory
squared_list = [x * x for x in range(1000000)]
print(f"List size: {sys.getsizeof(squared_list)} bytes") 
# Output: List size: ~8448728 bytes (8.4 MB)

# Generator expression: Generates a lazy iterator
squared_gen = (x * x for x in range(1000000))
print(f"Generator size: {sys.getsizeof(squared_gen)} bytes") 
# Output: Generator size: ~208 bytes