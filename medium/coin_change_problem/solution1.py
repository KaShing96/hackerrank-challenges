import math

# === Function ===
def getWays(n, c):
    """
    Your code goes here.
    """
    # === Preprocessing ===
    # We filter out all values of c that are greater than n
    c = list(filter(lambda x: x <= n, c))

    # We reorder c
    c.sort()

    # === Obtaining relations ===
    # --- Obtaining multiplicative relations ---
    # An array of tuples of 3
    # Given a tuple of (C1, C2, k2), it is interpreted as C1 = C2 * k2, where C1 and C2 are members of C
    mul_rels = []

    # Outer loop to loop through each letter in c, going backwards, to identify which letter we want to find the factors of
    for i in reversed(c): 

        # Inner loop to identify which other number in c can be a factor
        for j in reversed(c):

            # We only continue if j < i, because we do not want to compare the same number, and we only want to compare for when j is smaller than i
            if j < i: 

                # Determine if i is perfectly divisibly by j
                if i % j == 0:
                    
                    # Obtain the factor to divide by
                    # Factor
                    factor = 1

                    while i - factor * j > 0:
                        factor += 1

                    # Add the result to mul_rels
                    mul_rels.append((i, j, factor))

    # --- Obtaining additive relations ---
    # An array of tuples of 5
    # Given a tuple of (C1, C2, k2, C3, k3), it is interpreted as C1 = C2 * k2 + C3 * k3, where C1, C2 and C3 are memmbers of C
    add_rels = []

    # Outer loop to loop through C1
    for i in reversed(c):

        # Inner loop to loop through C2
        for j in reversed(c):

            # Proceed only if j < i
            # Else, skip
            if j >= i:
                continue

            # Inner loop to loop through C3
            for k in reversed(c):
                
                # Proceed only if k < j
                if k >= j:
                    continue 

                # When obtaining addition, we note that it can be generalised into the case of i = aj + bk, where a and b are constants
                # We obtain an upper bound for a and b
                a_max = math.ceil(i / j)
                b_max = math.ceil(i / k)

                # Obtain relations
                # Loop through a
                for a in range(1, a_max + 1):

                    # Loop through b
                    for b in range(1, b_max + 1):

                        # Check for equality
                        if i == a * j + b * k:
                            add_rels.append((i, j, a, k, b))

    # --- Generalise relations ---
    # Generalise mul_rels into add_rels
    for mul in mul_rels:
        add_rels.append((mul[0], mul[1], mul[2], 0, 0))

    # Obtain a list of relations
    related = []

    # Add all elements of C that can be added into a relation
    for add in add_rels:
        # We keep in mind add is a tuple of: (C1, C2, k2, C3, k3) and we want to obtain the idea that C1, C2 and C3 can eb related to each other
        related.append(add[0])
        related.append(add[1])

        # We do not add C3 if it is a 0, i.e. it was initially in mul_rels
        if add[3] > 0: 
            related.append(add[3])

    # Only keep the unique values 
    related = set(related)

    # Obtain the values in C that cannot be related
    unrelated = set(c) - related

    # === Obtain initial sets ===
    # The initial solution sets need to at least have each value in unrelated at least ONCE
    # The initial solution sets also need to have the value X at least once, where X is the first element in each tuple in add_rels
    solutions = []

    # We initialise each solution set in solutions with values in unrelated, and then with the first elements of each tuple in add_rels
    
    # Add unrelated values
    for i in unrelated: 
        solutions.append(i)

    # Add add_rels values
    for i in add_rels:

        # Only add if they don't already exist
        if i[0] not in solutions: 
            solutions.append(i[0])

    # Sort solutions in descending order and cast each element to a dictionary of the element
    solutions.sort(reverse=True)
    solutions = [{s: 0} for s in solutions]

    # Obtain solution sets
    for sx, s in enumerate(solutions): 

        # Obtain first element of this solution
        s0 = list(s.keys())[0]

        # We instantiate a dictionary of skips, where the keys are the elements of C, and the value is the number of time to skip it
        skips = {}

        # TO be replaced with a while loop
        # [TODO]
        for _ in range(100):
        
            # Obtain the running total
            # The running total is defined as the sum of all current values, i.e. if the target number is 40 and we begin with the solution number 3, the running total after we identify that 3*13 = 39 is the largest number less than 40 will give running total = 39
            # However, this running_total will be instantiated at 0 and will only be edited and used in the following for loop
            running_total = 0

            # Instantiate an intermediate solution set
            i_sol = {s0: 0}

            # We loop down values in C until we get to the current given value of this solution
            for i in reversed(c):
                if i > s0:
                    continue 

                # We attempt to zero out the target number
                factor = math.floor((n - running_total)/ i)
                running_total += factor * i

                # DEBUG(f"iteration: {_}, will i be skipped: {i in skips}, i to be skipped: {i}, current i_sol before skipping: {i_sol}")

                # If the current number exists in skips, we need to reduce it by the required amount
                if i in skips: 

                    # DEBUG(f"i: {i}, factor: {factor}, s0: {s0}, factor > skips[i]: {factor > skips[i]}")

                    # However, we keep in mind that we keep at least a minimum of 1 copy of s0, the original element of C we are attempting to force
                    if i != s0 or (i == s0 and factor > skips[i]):

                        # Revert the running_total and the factor
                        running_total -= i * skips[i]
                        factor -= skips[i]

                # Add this number to the dictionary
                if factor > 0: 
                    i_sol[i] = factor

                # If the running_total == number, we stop it for this solution set
                if running_total == n:
                    break

            # DEBUG(f"iteration: {_}, running total: {running_total}, skips: {skips}, solution set: {i_sol}")

            # At the end, we ensure that the running_total == n
            if running_total != n:

                # We increment skips
                # We run through possible keys to increment skips with
                for key in i_sol.keys():
                    
                    # We check that this key is in skips
                    if key in skips: 
                        
                        # We check that the key has not been maxed out
                        if skips[key] < i_sol[key]:

                            # If it has not been maxed out, we increment it
                            skips[key] += 1

                            break

                        # Else, if the key has been maxed out, we move on to the next key
                        else: 
                            continue

                    # If the key is not in skips, we add the key
                    else: 
                        skips[key] = 1

                # DEBUG(f"i_sol: {i_sol}, skips: {skips}")

                # # We append to 'skips'
                # # If skips exists, we [TODO]
                # if skips != {}: 
                #     raise Exception()

                # # Else, we append the second largest number in the solution set to skips
                # else: 
                #     pass

                #     # skips[] = 1

            # If the running total == n, we break the loop
            else: 
                # Set the solution to i_sol
                # s = i_sol
                solutions[sx] = i_sol

                break 

    # === Expand solution set through relations ===
    # Cache for dynamic programming
    # Holds the current solution set and the compared relation
    cache = []

    while True: 
        # We repeat this expansion until there are no changes to solutions
        changed = False

        # DEBUG(_)

        # Variable to hold new solutions
        new_solutions = []

        # We expand via add_rels
        # We loop through all existing initial set solutions
        for s in solutions:

            # Loop through all possible relations
            for rel in add_rels:

                # Check if the relation can be applied
                # This is only if the first element of rel is in the keys of s
                # If not, it cannot be applied and we can skip it
                if rel[0] not in s.keys():
                    continue 

                # We know that the relation can be used

                # Obtain the cache code
                code = encode(s, rel)

                # Check if the code is in cache
                if code in cache: 
                    
                    # Do not do anything
                    continue 

                else: 
                    
                    # We apply the relation
                    new_sol = get_new_solution(s, rel)

                    # Add this to new_solutions
                    new_solutions.append(new_sol)

                    # We then add this to the cache
                    cache.append(code)

        # Check if there are new solutions
        solutions_set = set([str(s) for s in solutions])
        new_solutions_set = set([str(s) for s in new_solutions])

        # DEBUG(new_solutions_set.issubset(solutions_set))

        if not new_solutions_set.issubset(solutions_set):
            
            # Not all new solutions are in solutions
            # Thus, we extend solutions by new solutions
            for new_sol in new_solutions:

                if new_sol not in solutions:
                    solutions.append(new_sol)

            # We set changed to True
            changed = True 

        # Finally, we check if there was no change
        if changed == False: 
            break 

    # DEBUG(cache)

    return len(solutions)


def get_new_solution(old, rel):
    """
    Obtains a list of possible new solutions based on possible combinations of each coin in old and the list of relations in rel.

    Params
    ======
    old: {}
        dictionary with the key being the coins and the values being the number of coins
    rel: ()
        A tuple.
        Follows the add_rels format

    Returns
    =======
    new: {}
        A dictionary in the format of old
    """
    # Instantiate new
    new = dict(old)

    # We have rel in the form of (C1, C2, k2, C3, k3)
    # We reduce C1 in old by 1, and increment C2 and C3 in old by k2 and k3 respectively
    new[rel[0]] -= 1

    # We ensure that rel[1] and rel[3] exist in old
    if rel[1] not in new.keys():
        new[rel[1]] = 0

    # For rel[3], there is a chance that it is 0. In this case, we do not instantiate it
    if rel[3] != 0 and rel[3] not in new.keys():
        new[rel[3]] = 0

    # We increment C2 and C3 by k2 and k3
    new[rel[1]] += rel[2]

    # We only increment C3 if it is not 0
    if rel[3] != 0: 
        new[rel[3]] += rel[4]

    # Clear up the solutions
    # If a dictionary entry is of size 0, we delete it
    if new[rel[0]] == 0:
        del new[rel[0]]

    # Reorder the dictionary by its keys
    new = {k: v for k, v in sorted(new.items())}

    return new


def encode(s, r):
    """
    From the given solution set and relation, generates a cache code. 

    Params
    ======
    s: {}
        The dictionary of the solution set
    r: ()
        Tuple of 5, following the format of add_rels

    Returns
    =======
    code: str
        The code for the cache
        For a solution set S = {5:1, 4:2, 3:3}, and a given relations set R = (R1, R2, R3, R4, R5), the code is: 
        '5:1 4:2 3:2_R1 R2 R4'
        The code is separated by an underscore, where the left side represents the dictionary. Each key is followed by a colon, where code 1 indicates that there is only 1 occurrence of the coin, while code 2 indicates there's more than one.
        The right side represents R1, R2 and R4.
    """
    # Instantiate the code
    code = ""

    # Loop through items in s.items()
    for k, v in s.items():

        # Get the key
        code += str(k) + ":"

        # Encode the value with either 1 or 2
        code += str(v) + " " if v == 1 else "2 "

    # Remove the final space
    code = code[:-1]

    # Underscore
    code += "_"

    # Add relations
    code += " ".join([str(s) for s in [r[0], r[1], r[3]]])

    return code


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