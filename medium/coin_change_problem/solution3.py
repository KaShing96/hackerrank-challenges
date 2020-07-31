import math

# === Function ===
def getWays(n, c):
    """
    Your code goes here.
    """
    # === Preprocess c ===
    # Filter out values exceeding n
    c = list(filter(lambda x: x <= n, c))

    # Sort in ascending order
    c.sort()

    # === Obtain relations ===
    # Dictionary of relations
    # The key is the target coin to be decomposed, and the value is a list of possible decompositions
    # Interpreted for a key k and a list value of v of length l, where each element is a tuple of length 2, k = v[0][0] + v[0][1], v[1][0] + v[1][1], ... , v[l][0] + v[l][1]
    relations = {}

    # Obtain relations between all coins
    # Loop through each coin
    for i in reversed(c):

        # For each coin, we attempt to find an additive relation. To do so, we need to loop through each coin smaller than i twice, with the first loop identifying the first value and the second loop identifying the second value. If these two values sum up to give i, we add it to our list of relations. 
        for j in reversed(c): 

            if j >= i: 
                continue 

            for k in reversed(c):

                # We want k to be less than or equal to j to preserve the ordering. E.g. in the case of 5 = 3 + 2, we do not want a repeat case of 5 = 2 + 3 recorded.
                if k > j: 
                    continue 

                if j + k == i:

                    # We store the results in a dictionary
                    if i in relations.keys():
                        relations[i].append((j, k))

                    else:
                        relations[i] = [(j, k)]

    # === Relational scores ===
    # We generate scores for each coin based on their relations, i.e. how many cases this coin can be broken up into
    scores = {}

    # For those that cannot be broken down into others, we set their score as 0
    for i in c:
        if i not in relations.keys():
            scores[i] = 0

    # Generate the remainder of the scores
    for i in c: 

        # We only generate if they have relations
        if i not in relations.keys(): 
            continue 

        # If there is more than one relation, we can have more than one score per coin. Thus, we keep a running list of the coin's scores in a list.
        current_coin_scores = []

        # For all other coins, we access the list of relations
        for rel in relations[i]:

            # If a relation exists, there is already an additional case. 
            current_score = 1

            # Obtain the number of unique components
            unique_components = set(rel)

            # For each unique component, obtain its 'additional case' score from scores
            add_cases = []

            for comp in unique_components:
                add_cases.append(scores[comp])

            # Calculate the score from this relation, based off the relational equation in the README
            current_score += sum(add_cases)

            # Add score to total_scores
            current_coin_scores.append(current_score)

        # Total up all the scores and add it to scores
        scores[i] = sum(current_coin_scores)

    # === Obtain top level answers === 
    solutions = []

    # We loop through every coin in c
    # The point of this is to obtain a solution set that, at the very least, has at least one of this coin
    for k in reversed(c):

        # Instantiate s
        s = {}

        # We want to obtain values for which we have the maximum value of k for the given solution set
        for i in reversed(range(1, math.floor(n / k) + 1)):

            # We instantiate the solution set
            s = {i: 0 for i in list(filter(lambda x: x <= k, reversed(c)))}

            # Obtain solution
            s = populate(s, n, (k, i))
            
            # Check if s is None
            # If s is None, we need to continue with the loop
            # Else, we can append s to solutions and break out of the loop
            if s is not None: 
                solutions.append(s)

                break

    # === Finalise total cases ===
    final_score = len(solutions)

    # For each solution, we obtain the additional scores based on the MAX-REST equation in README
    for s in solutions: 

        # Biggest coin
        biggest_coin = max(s.keys())

        # Obtain max-rest score
        # Calculate the max score, which should have a minimum of 0
        max_score = max(0, (s[biggest_coin] - 1) * scores[biggest_coin])

        # Calculate the rest score
        rest_score = 0

        # We calculate the rest score using all other coins in the dictionary
        for i in s.keys():
            if i == biggest_coin:
                continue 

            else: 
                rest_score += s[i] * scores[i]

        max_rest_score = max_score + rest_score

        # Increment total score
        final_score += max_rest_score

        # DEBUG(f"solution: {s}, max-rest score: {max_rest_score}")


    # DEBUG(solutions)

            # DEBUG(f"coin: {i}, uniques: {unique_components}, additionals: {add_cases}, current score: {current_score}")
            

        # DEBUG(f"coin: {i}, relation: {relations[i]}, scores: {scores}")



    # We loop through all relations
    # 
    # 
    # 
    #  except for the first coin, which we set to have a score of +0. 

    
    # DEBUG(f"n: {n}, c: {c}, relations: {relations}, scores: {scores}, solutions: {solutions}, final_score: {final_score}")

    return final_score


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