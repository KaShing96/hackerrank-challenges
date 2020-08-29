# === Imports ===
import math
import os
import random
import re
import sys

# === Function ===
def kangaroo(x1, v1, x2, v2):
    
    # Catch division by zero
    if v2 == v1: 
        if x2 == x1: 
            return "YES"

        else: 
            return "NO"

    # Obtain t
    t = (x1 - x2) / (v2 - v1)

    # Assert conditions
    if t >= 1 and t // 1 == t:
        return "YES"
    
    else:
        return "NO"


# Function to be called
def main(args):
    """
    This is the main function to be called in test_functions.py.
    This should emulate the logic in HackerRank's if __name__ == '__main__' logic block and process #args# accordingly. 

    Params
    ======
    args: str
        A single line string
    """

    x1V1X2V2 = input().split()
 
    x1 = int(x1V1X2V2[0])
 
    v1 = int(x1V1X2V2[1])
 
    x2 = int(x1V1X2V2[2])
 
    v2 = int(x1V1X2V2[3])
 
    result = kangaroo(x1, v1, x2, v2)
 
    fptr.write(result + '\n')

    fptr.close()


# === Debug ===
def DEBUG(*args, **kwargs):
    """
    If this function is not run directly, i.e. it is under test, this will take on the print statement. Otherwise, nothing happens. 
    """
    if __name__ != "__main__":
        print(*args, **kwargs)


# === Mock ===
# Mock fptr.write()
class Writer():
    def __init__(self):
        """Initialises the list of answers."""
        self.answers = []


    def write(self, string):
        """Appends the string to a list, which is then accessed by the parent test function to check for equality of arguments.
        
        Params
        ======
        string: str
            The string to be appended to the list of answers.
        """
        # Process the string to be appended, to remove the final newline character as added in main()
        li = string.rsplit('\n', 1)

        self.answers.append(''.join(li))

    
    def get_answers(self): 
        """
        Returns the answers and resets it.

        Returns
        =======
        result: list of strings
            The answers to be returned.
        """
        result = self.answers 

        self.answers = []

        return result


    def close(self):
        pass
        

fptr = Writer()

# List of inputs
list_of_inputs = []

# Sets inputs
def set_inputs(string):
    """
    This function sets the inputs to be mocked by the input() function. 
    The #string# passed is split by the newline character. Each element then makes up the argument called sequentially by input().
    """
    global list_of_inputs

    list_of_inputs = string.split("\n")


# Mocks the inputs
def input():
    """
    Mocks the 'input()' function. 
    If arguments is not None, it resets the arguments used. 
    """
    return list_of_inputs.pop(0)