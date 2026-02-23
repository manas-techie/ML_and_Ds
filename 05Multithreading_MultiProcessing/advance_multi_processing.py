## multiprocesssing with the ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def print_numbers(num):
    time.sleep(1)  # Simulate a time-consuming task
    return (f"Number: {num}")   



if __name__ == "__main__":  
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    t = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(print_numbers, number)
     
    for result in results:
        print(result)
        
    print(f"Time taken: {time.time() - t}") 