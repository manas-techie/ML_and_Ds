import logging

## logging settings

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app.log', mode='w'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")



def add(a, b):   
    logger.debug(f"Adding {a} and {b}")
    return a + b

def subtract(a, b):   
    logger.debug(f"Subtracting {b} from {a}")
    return a - b

def multiply(a, b):   
    logger.debug(f"Multiplying {a} and {b}")
    return a * b

def divide(a, b):   
    if b == 0:
        logger.error("Division by zero attempted")
        return None
    logger.debug(f"Dividing {a} by {b}")
    return a / b


logger.debug("Starting the program")
add(5, 3)
subtract(10, 4)
multiply(6, 7)
divide(20, 5)