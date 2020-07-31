# === Function ===
def abbreviation(a, b):
    """
    Your code goes here.
    """
    # Cache for dynamic programming
    cache = []

    for _ in range(len(a) + 1): 
        cache.append([])
        for _ in range(len(b) + 1): 
            cache[-1].append(None)

    # We loop through a and b
    # We are interested in ix and jx
    # We want to use these to isolate the first (ix + 1) or (jx + 1) letters of a string
    for ix in range(len(a) + 1): 
        # Here, i refers to the first (ix + 1) letters in a string
        i = a[:ix]

        for jx in range(len(b) + 1): 
            # Similarly, j
            j = b[:jx]

            # Check i and j
            if i == j:
                cache[ix][jx] = True

            else:

                # We check if the last characters of i and j are equal
                # To do so, we must first check that i and j are non-empty
                if i == "":

                    # i is empty and not equal to j
                    cache[ix][jx] = False

                elif j == "":
                    # i is non-empty but j is empty
                    # We attempt to reduce i

                    # Check if we can reduce the last letter in i
                    if i[-1] == i[-1].lower():

                        # We know j is empty and the last letter of i is lowercase
                        # We remove it
                        cache[ix][jx] = cache[ix-1][jx]

                    else:
                        # If i is not empty and j is empty and we cannot reduce i, it is a fail
                        cache[ix][jx] = False

                else: 

                    # Neither i nor j are empty
                    # We compare their last letters
                    i1 = i[-1] 
                    j1 = j[-1]

                    # Check if the last letters are equal
                    if i1 == j1 or i1.upper() == j1:

                        # List of ORs
                        ors = []

                        # Here, we can opt to remove i1, or we can opt to keep it

                        # Check if we can remove i1
                        # If i1 is lowercase, we can either keep or remove it
                        # If i1 is uppercase, we must keep it, resulting in a truncation of both i and j
                        # In either case, we need to consider the keep case. Thus, we  move it outside the if-else block
                        if i1 == i1.upper():

                            # We cannot remove i1
                            # We must keep i1, resulting in a truncation of i and j
                            
                            # Skip
                            pass

                        else:

                            # We can choose to remove i1
                            # We can either keep or remove it

                            # Remove case
                            ors.append(cache[ix-1][jx])

                        # Keep case
                        ors.append(cache[ix-1][jx-1])

                        # If any of the values are True, we set it to True
                        cache[ix][jx] = any(ors)

                    else:
                        
                        # We know i1 != j1 regardless of case
                        
                        # We check if we can remove i1

                        if i1 == i1.upper():

                            # We cannot remove the case
                            cache[ix][jx] = False

                        else:

                            # We can remove the case
                            cache[ix][jx] = cache[ix-1][jx]

        # If none of the most recent additions are True, it will fail. 
        if not any(cache[ix]): 
            return "NO"

    # If the final value is true, we return YES, else NO
    if cache[-1][-1] == True:
        return "YES"
    else: 
        return "NO"


def hashed(a, b): 
    """
    Generate hash of a and b
    """
    return "_".join([a, b])


# === Debug ===
def DEBUG(*args, **kwargs):
    """
    If this function is not run directly, i.e. it is under test, this will take on the print statement. Otherwise, nothing happens. 
    """
    if __name__ != "__main__":
        print(*args, **kwargs)


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
    q = int(input())

    for _ in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')


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