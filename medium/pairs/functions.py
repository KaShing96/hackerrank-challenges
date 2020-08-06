# === Imports ===
import math
import os
import random
import re
import sys

# === Function ===
def pairs(k, arr):
    # === Preprocessing ===
    # Sort `arr`
    arr.sort()

    # === Obtain answer ===
    answer = 0

    # Hold the previous successful value of j. This is instantiated at 1 because we want j to begin counting from the first element of `arr` rather than the zeroth.
    previous_j = 0

    # Loop through `arr`
    for i in arr:

        for jx in range(previous_j, len(arr)): 
            j = arr[jx]

            # We only run for which j > i, which translates to jx > ix due to `arr.sort()`. Thus, we skip all occurrences where `j <= i`.
            if j <= i:
                continue 

            # We then run the subtraction, noting that j > i
            if j - i == k:
                answer += 1 

                # When this is incremented, we note that all i after this will require at least the next j. Thus, we let previous_j = jx + 1
                previous_j = jx + 1

                # We break the loop as there is only one unique answer per i
                break 

            # We also note that if j - i > k, no other value of j will satisfy j - i == k
            if j - i > k:
                break

    return answer


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

    nk = input().split()
 
    n = int(nk[0])
 
    k = int(nk[1])
 
    arr = list(map(int, input().rstrip().split()))
 
    result = pairs(k, arr)
 
    fptr.write(str(result) + '\n')
 


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