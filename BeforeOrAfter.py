import math


def divide_numbers(a, b):
    """this function divide two numbers and return the result with handling errors"""
    try:
        result = a / b
    except ZeroDivisionError:
        result = math.inf
    except TypeError:
        result = None
    except Exception as e:
        print(f"An error occurred: {e}")
        result = None
    return result


print(divide_numbers(1, 0))
