# Importing necessary libraries
import time
import random

# Defining a constant
CONSTANT = "This is a constant"

# Defining a decorator function
def timing_decorator(func):
    """This decorator prints the execution time of the decorated function"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to run.")
        return result
    return wrapper

# Defining a class
class ExampleClass:
    """This is an example class"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @timing_decorator
    def say_hello(self):
        """This function prints a greeting message"""
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def random_number(self):
        """This function returns a random integer"""
        return random.randint(1, 100)

# Defining a function
@timing_decorator
def example_function(name: str, age: int) -> None:
    """This is an example function"""
    print(f"Hello, my name is {name} and I am {age} years old.")

if __name__ == "__main__":
    # Creating an object of the class
    person = ExampleClass("John Doe", 25)

    # Calling class methods
    person.say_hello()
    print(f"My favorite number is {person.random_number()}")

    # Creating a list
    numbers = [1, 2, 3, 4, 5]

    # Creating a tuple
    tuple_numbers = (1, 2, 3, 4, 5)

    # Using the function
    example_function("Jane Doe", 30)
