from math import sqrt

# help(sqrt)

def greet(name):
    """
    Return friendly greeting for the provided name
    """
    print(f"Hello {name}")

greet("Adam")
# help(greet)

def add_numbers(a,b):
    """
    Add two numbers together.

    Parameters
    ------------
    a : int or float
        the first number
    b : int or float
        the second number

    Returns
    ------------
    int or float
        The sum of a and b
    """
    return a + b

help(add_numbers)
