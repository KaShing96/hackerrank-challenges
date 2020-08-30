# === Imports ===
import math
import os
import random
import re
import sys

# === Function ===
def getTotalX(a, b):
    # Obtain LCM of elements in a
    divisor = [2]
    lcm = 1

    while True: 
        
        # If any can be divided by 'divisor'
        if any([x % divisor[-1] == 0 for x in a]):
            
            # Divide
            a = [x / divisor[-1] if x % divisor[-1] == 0 else x for x in a]

            # Increment LCM
            lcm *= divisor[-1]

        # Else, we increment the divisor
        else: 

            new_divisor = divisor[-1] + 1
            divisors_length = len(divisor)
            
            while True:
                # Check if new_divisor is directly divisible by any other element in divisor
                for d in divisor: 

                    if new_divisor % d == 0: 
                        
                        new_divisor += 1

                        continue 

                    else: 

                        divisor.append(new_divisor)

                        break

                # Only break out of the while loop if we've appended a new divisor
                if divisors_length != len(divisor): 
                    break 

        # Break the entire while loop if we have the LCM
        if all([x == 1 for x in a]):
            
            break 

    # Obtain the HCF of 'lcm' and all elements in b
    divisor = [lcm]
    multiple = 1
    smallest_in_b = min(b)
    answer = 0

    while True: 
        # Divide all in b by divisor
        if all([x % divisor[-1] == 0 for x in b]):

            # Increment answer
            answer += 1

        # We increment divisor
        # We note that all possible divisors must be multiples of lcm to comply with rule 1
        # Thus, we only multiple LCM

        multiple += 1
        new_divisor = lcm * multiple

        divisor.append(new_divisor)

        # Break if the divisor exceeds the smallest in b
        if divisor[-1] > smallest_in_b:
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
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

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