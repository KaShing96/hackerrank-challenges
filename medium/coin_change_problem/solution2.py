import math

# === Function ===
def getWays(n, c):
    """
    Your code goes here.
    """
    # === Preprocessinsg ===
    # We ensure that all values in c are <= n
    c = list(filter(lambda x : x <= n, c))

    # We sort the values in c
    c.sort(reverse=True)

    # === Obtain set of initial solutions ===
    # Variable to hold all initial solutions
    solutions = []

    # We want to obtain a set of solutions. Each solution is focused on a different coin, i.e. a solution set of coin c1 will have at least 1 c1 coin. 
    # We do this to cover all possible bases. 

    # We loop through every coin in c
    # The point of this is to obtain a solution set that, at the very least, has at least one of this coin
    for k in c:

        # Instantiate s
        s = {}

        # We want to obtain values for which we have the maximum value of k for the given solution set
        for i in reversed(range(1, math.floor(n / k) + 1)):

            # We instantiate the solution set
            s = {i: 0 for i in list(filter(lambda x: x <= k, c))}

            # Obtain solution
            s = populate(s, n, (k, i))
            
            # Check if s is None
            # If s is None, we need to continue with the loop
            # Else, we can append s to solutions and break out of the loop
            if s is not None: 
                solutions.append(s)

                break

    # === Obtain dependent solutions ===
    # Each solution set is a dictionary of coins
    # We can decrement the largest number, and attempt to obtain another 'max' dictionary

    DEBUG(f"initial solutions: {len(solutions)}")

    # Loop through solutions
    for s in solutions: 

        # Each solution has a set of coins
        # We attempt to decrement the largest value coin by 1
        # If the largest value coin only has an occurrence of 1, this is covered in the previous case where a particular coin value was excluded, i.e. set to 0
        # Thus, we skip all coins with maximum value == 1

        # Obtain maximum value coin
        biggest_coin = max(s.keys())

        # Skip those with only 1 biggest coin
        if s[biggest_coin] == 1:
            continue 

        # We also skip all dictionaries with only 1 key as those cannot be reduced further
        if len(s) == 1: 
            continue 

        # We attempt to decrement the maximum in s by 1
        # We repeat this until the value of the coin in question is 1

        # To do so, we need to generate a sub-solution
        # The sub-solution contains all but the biggest coin
        sub_solution = {k: v for k, v in s.items() if k < biggest_coin}

        # Populate
        sub_solution = populate(sub_solution, n - biggest_coin)

        # If sub_solution is None, it could not be obtained. Thus, we skip it.
        if sub_solution is None: 
            continue

        # Re-include the biggest coin
        sub_solution[biggest_coin] = s[biggest_coin] - 1

        # Sort
        sub_solution = {k: v for k, v in sorted(sub_solution.items(), reverse=True)}

        # Add this new solution to the list of solutions
        solutions.append(sub_solution)

    return len(solutions)


def populate(d, n, target=(0,0)):
    """
    Given a dictionary of coins, counts up from the largest value. When the sum of all values in the dictionary exceeds n, resets the count of the largest value and increments the next largest value. This continues until either there is no 'next largest' to increment, or until the value n is obtained. 

    Params
    ======
    d: {}
        Dictionary where keys are the coins and values are the number of coins available. 

        The dictionary must be ordered in descending value of coins.
    n: int
        The target number
    target: ()
        Index 0 is the value of the coin, and index 1 is the minimum number of that coin that has to be in the dictionary
    
    Returns
    =======
    d: {}
        The dictionary with the coins and values set to either equal n, or None is returned.
    """
    # Index of key to increment
    index = 0

    # Instantiate the largest value of the dictionary
    d[max(d.keys())] = math.floor(n / max(d.keys()))

    # Loop until n is obtained, or until an error is thrown
    while True:

        # We break the loop if the sum of all values in the dictionary is equal to n
        if dict_sum(d) >= n: 
            break 

        # We begin incrementation
        # If we run into IndexError, the value cannot be made equal to n and thus should be is dropped
        try: 
            d = count_up(d, n, 0, target)
        except IndexError:
            break

    # If the sum is equal to n, return it, else return None
    if dict_sum(d) == n:
        return d 

    else:
        return None


def count_up(d, n, index, target):
    """
    Increments the key at 'index' by 1. If this causes the total to exceed n, sets the current index to 0 and calls count_up with index = index + 1. Else, return d. 

    Params
    ======
    d: {}
        Dictionary of coins
    n: int
        The number that should not be exceeded
    index: int
        The index of the list of keys in d to increment
    target: ()
        Index 0 is the value of the coin and index 1 is the minimum occurrences of that coin

    Returns
    =======
    d: {}
        Dictionary, with the key at index 'index' incremented by 1, without exceeding n

    Raises:
    =======
    IndexError:
        If you cannot get keys[index], because index is out of range
    """
    # List of keys
    keys = list(d.keys())

    # Increment
    d[keys[index]] += 1

    # Check for n
    if dict_sum(d) > n:

        # If it is greater than n, set the current index to 0 and increment the next index
        d[keys[index]] = 0 if keys[index] != target[0] else target[1]

        return count_up(d, n, index + 1, target)

    else:
        return d





def dict_sum(d):
    """
    Returns the sum of values in the dictionary, multiplied by the key. 
    """
    return sum(k*v for k, v in d.items())



# def increment(d, n, kx, forced=None):
#     """
#     This function increments the key at index kx by 1, and checks if the sum exceeds n. 

#     If the sum exceeds n, it sets the key at kx = 0, and calls add on kx = kx + 1. 

#     Else, it returns d. 

#     Params
#     ======
#     d: {}
#         The keys are the coins, and the value is how many coins there are
#     n: int
#         The maximum number
#     kx: int
#         The index of the key to be incremented
#     forced: int
#         forced is an optional argument which, if the key at kx is equal to forced, then instead of setting it to 0, it sets it to 1. 
#     """
#     # Instantiate the list of keyes
#     keys = list(d.keys())

#     # Increment
#     d[keys[kx]] += 1

#     # Check for overflow
#     if dict_total(d) > n:
        
#         # If overflow, set the value of the current key to 0
#         d[keys[kx]] = 0

#         # If the current key is forced, however, we set it to 1 instead
#         if keys[kx] == forced:
#             d[keys[kx]] = 1
        
#         # We increment the next key
#         return increment(d, n, kx + 1)

#     # If there is no overflow, return it
#     else:
#         return d
    

# def max_increment(d, n, forced):
#     """
#     Using the increment() function above, maximises the incrementation possible for d and returns it.
#     """
#     # We have a try-catch loop as the following increment() function can throw an IndexError
#     try:

#         # We run this until the solution is complete or the error is caught
#         while True:
            
#             # We will attempt to identify the initial solution by incrementing the largest value by 1
#             # When this results in an overflow, i.e. the sum is greater than the number n, we increment the next value by 1 and set this value to 0. 
#             # This is inspired by binary counting, only instead of going from 00 to 01 to 10, we set the a 'bit' to 0 when there is an overflow, and we work from the most significant bit inwards.    
#             d = increment(d, n, 0, forced)

#             # We only end the loop properly if the sum of values in the dictionary is greater than or equal to n
#             if dict_total(d) >= n:

#                 break

#     except IndexError:
#         # We do nothing in the case of an IndexError
#         # We catch it and move on
#         pass 

#     # We return d only if it is equal to n
#     # If it isn't we return Non
#     return d if dict_total(d) == n else None


# def dict_total(d):
#     """
#     Returns the sum of the dictionary's values and keys multiplied.
#     """
#     return sum(k*v for k, v in d.items())



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