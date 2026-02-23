## why we use multithreading
## I/O bound tasks: tasks that spend most of their time waiting for input/output operations to complete, such as reading/writing files, making network requests, or interacting with databases. Multithreading can help improve the performance of I/O-bound tasks by allowing other threads to run while one thread is waiting for I/O operations to complete.

## concurrency: the ability of a system to handle multiple tasks at the same time, allowing them to make progress without necessarily executing simultaneously. Concurrency can be achieved through various mechanisms, including multithreading, multiprocessing, and asynchronous programming.

import threading
import time


## without threading, the tasks will be executed sequentially, meaning that one task will have to wait for the other to complete before it can start. This can lead to inefficient use of resources and longer execution times, especially if one of the tasks is time-consuming.
def print_numbers():
    for i in range(1, 6):
        time.sleep(1)  # Simulate a time-consuming task
        print(f"Number: {i} - Thread: {threading.current_thread().name}")

def print_letters():    
    for letter in ['A', 'B', 'C', 'D', 'E']:
        time.sleep(1)  # Simulate a time-consuming task
        print(f"Letter: {letter} - Thread: {threading.current_thread().name}")


# t=time.time()
# print_numbers()
# print_letters()
# finish_time = time.time()

# print(f"Execution time without threading: {finish_time - t} seconds")


### create threads for each task

t1 = threading.Thread(target=print_numbers, name = "Thread-1")
t2 = threading.Thread(target=print_letters, name = "Thread-2")
     
t = time.time()
t1.start()
t2.start()

t1.join()  # Wait for thread 1 to finish
t2.join()  # Wait for thread 2 to finish
finish_time = time.time()

print(f"Execution time with threading: {finish_time - t} seconds")
