import math

# === Function ===
# Reduce repeats of getWays()
# A dictinary of dictionaries
cache = {}

def getWays(n, c):
    """
    Your code goes here.
    """
    # Prior to running the function, we check if this value of n is recorded in cache. If it is, we check if the cache code of c is stored. If it is, we return that value. Otherwise, we proceed with the rest of the function, adding the number of cases at the end. 
    code = cache_code(c) 

    if n in cache: 

        if code in cache[n]:

            return cache[n][code]

    # Number of cases possible from the given n and c
    cases = 0

    # === Recursion ===
    # We note that, in the 'else' condition, prior to recursively calling getWays, we will subtract n by a coin in c. This subtraction WILL take into account whether n == 0 following the subtraciton. Thus, if n == 0, it will not be called. 

    # We will be reducing the size of c with every recursive call. Thus, we check if the size is 1. If it is, we will set the number of cases to 1 only if n is perfectly divisible by the value in c. If it is not perfectly divisible, there are no cases possible. 
    if len(c) == 1:

        if n % c[0] == 0:
            cases = 1

    # If there is more than one index in c, we need to recursively call getWays() and return the number of cases for each sub-case. 
    else:

        # We note we want to obtain the different sub-cases. To do so, we identify the coin in position c[0] and loop through every possible amount of this coin, up until the largest number of coins that give us a value smaller than n. 

        for i in range(math.floor(n/c[0]) + 1): 

            # New target number
            new_n = n - i * c[0]

            # If the new target number is 0, we increment cases by 1 and continue to the next loop
            if new_n == 0:
                cases += 1

                continue 

            # Otherwise, we recursively call this function
            cases += getWays(new_n, c[1:])

    # Add the number of cases to the dictionary
    if n not in cache:

        cache[n] = {}

    cache[n][code] = cases

    # Then, we return cases
    return cases


def cache_code(l):
    """
    Returns the cache code of the given list l.
    """
    return str(l)


# === Main ===
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

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'    
    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

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