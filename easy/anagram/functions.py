# === Imports ===
import math
import os
import random
import re
import sys

# === Function ===
def anagram(s):
    # Check string length
    length = len(s)

    if length % 2 != 0: 
        return -1

    # Split strings
    s1 = s[:length//2]
    s2 = s[length//2:]

    # Check for differences
    diff = {}

    for substring in [s1, s2]:

        for c in substring: 

            if c not in diff.keys():
                diff[c] = {}

            if substring not in diff[c].keys():
                diff[c] = {
                    s1: 0,
                    s2: 0
                }

            diff[c][substring] += 1

    # Get difference
    change = 0

    for v in diff.values(): 

        print(v)

        a2b = v[s1] - v[s2]
        
        # Ignore a2b if it's negative as it suggests that it is b2a instead
        if a2b > 0: 
            change += a2b

    return change


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

    q = int(input())
 
    for q_itr in range(q):
        s = input()
 
        result = anagram(s)
 
        fptr.write(str(result) + '\n')
 
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