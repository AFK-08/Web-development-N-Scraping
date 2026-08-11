## Python Decorators Functions Structure:

import time

def decorator_function(function):
    def wrapper_function():
        time.sleep(3)     ### do something before
        function()
        function()        ## do something after basically
    
    return wrapper_function

## A decorator Function is a function that wraps another function inside it and gives it additional functionality or modifys functionality...for ex:

@decorator_function
def say_hello():
    print("say hello to the world")

say_hello()

## or 

# modified_function = decorator_function(say_hello)
# modified_function()


