## multithreading with Thread Pool Executor
## ThreadPoolExecutor is a high-level interface for asynchronously executing callables using threads. It provides a convenient way to manage a pool of threads and execute tasks concurrently without having to manually create and manage individual threads.  


from concurrent.futures import ThreadPoolExecutor
import time



def print_numbers(num):
    time.sleep(1)  # Simulate a time-consuming task
    return (f"Number: {num}")

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_numbers, number)

for result in results:
    print(result)  
    

