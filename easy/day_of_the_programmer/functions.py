# === Imports ===
import math
import os
import random
import re
import sys

# === Function ===
def dayOfProgrammer(year):
    # Check for calendar type 
    if year < 1918:
        cal_type = "julian"
    elif year == 1918: 
        cal_type = "change"
    else:
        cal_type = "gregorian"

    # Check leap year
    leap_year = False 

    if cal_type == "julian": 
        if year % 4 == 0: 
            leap_year = True

    else: 
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):  
            leap_year = True 

    # The 256th day of a leap year is 12th September. 
    # Thus, the 256th day of a non-leap year in the Gregorian calendar is 13th September, i.e. you add one day.

    dmy = [13, 9, year]

    if cal_type == "change": 
        dmy[0] += 13 # You lose thirteen days, so you increment by this much

    if leap_year:
        dmy[0] -= 1 # Go back one day for a leap year

    # Correct the dates
    if dmy[0] < 1: 
        dmy[0] += 31
        dmy[1] -= 1

    # Set the dates to string
    dmy = [str(t) for t in dmy]

    # Prepend with zeros
    for ix, _ in enumerate(dmy): 
        while len(dmy[ix]) < 2: 
            dmy[ix] = "0" + dmy[ix]


    return ".".join([str(t) for t in dmy])


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

 
    year = int(input().strip())
 
    result = dayOfProgrammer(year)
 
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