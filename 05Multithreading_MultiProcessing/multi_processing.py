### its allow you to run multiple processes at the same time, each process can run on a different CPU core, which can significantly improve performance for CPU-bound tasks.

## CPU-bound tasks: tasks that require a lot of CPU processing power, such as complex calculations, data processing, or machine learning algorithms. Multiprocessing can help improve the performance of CPU-bound tasks by allowing them to run in parallel on multiple CPU cores.

## Parallelism: the ability of a system to execute multiple tasks simultaneously, typically by utilizing multiple CPU cores. Parallelism can be achieved through multiprocessing, where each process runs independently and can take advantage of multiple CPU cores to perform tasks concurrently.

import multiprocessing
import time


def print_numbers():
    for i in range(1, 6):
        time.sleep(1)  # Simulate a time-consuming task
        print(f"Number: {i} - Process: {multiprocessing.current_process().name}")
        
def print_letters():    
    for letter in ['A', 'B', 'C', 'D', 'E']:
        time.sleep(1)  # Simulate a time-consuming task
        print(f"Letter: {letter} - Process: {multiprocessing.current_process().name}")


if __name__ == "__main__":

    p1 = multiprocessing.Process(target=print_numbers, name = "Process-1")
    p2 = multiprocessing.Process(target=print_letters, name = "Process-2")
    
    t = time.time()
    p1.start()  
    p2.start()
    p1.join()  # Wait for process 1 to finish
    p2.join()  # Wait for process 2 to finish
    finish_time = time.time()
    print(f"Execution time with multiprocessing: {finish_time - t} seconds")    