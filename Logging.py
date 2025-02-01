import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%m/%d/%Y %I:%M:%S %p',
    handlers = [
        logging.FileHandler("app.py"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmaticApp")

def add(a,b):
    result = a+b
    logger.debug(f"Adding: {a} + {b} = {result}")
    return result

def subtract(a,b):
    result = a-b
    logger.debug(f"Subtracting: {a} - {b} = {result}")
    return result

def multiply(a,b):
    result = a*b
    logger.debug(f"Multiplying: {a} * {b} = {result}")
    return result

def divide(a,b):
    try:
        result = a/b
        logger.debug(f"Dividing: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero")
        return None

add(29,23)
subtract(29,23)
multiply(29,23)
divide(29,0)

