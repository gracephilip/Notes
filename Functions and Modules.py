from math import *     # * is a wildcard
from random import randrange
import my_import

square = 1


# Functions
def my_function(name = "Mr. Lee"):
    '''
    Says hellp
    :param name:
    :return:
    '''
    print("Hello", name)

# my_function("Mr. Lee") # this will always run on execution or import

def square_cube(n):
    '''
    returns square and cube of the number
    :param n:
    :return: square, cube
    '''
    square = n ** 2  # this is a local variable, not global like one at the top
    cube = n ** 3
    print("Square =", square)
    my_import.product_sum(square, cube)
    return square, cube



if __name__ == "__main__":
    # this is the file that you executed/ran
    my_function("Mr. Lee")
    my_import.product_sum(10, 20)
    print(randrange(100))
    print(e)
    # have to be careful with variables
    print(pi)
    print(square_cube(7))
    sqr_cube = square_cube(7)
    print(sqr_cube[0], sqr_cube[1])
    sqr, cube = square_cube(8)
    print(sqr, cube)

    # Scope rules
    # Python  (__main__), global (far left), local (inside functions)
    # you can see a global variable anywhere, but cannot change it locally.
    # you can ONLY see a local variable locally. Local variables do not exist outside namespace

    my_function(name = "Aaron")
    my_function()

    print("Hello", "World", end = " ", sep = "")
    print("World")


print("Francis".lower())

