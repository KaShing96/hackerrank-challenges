# === Function ===
def biggerIsGreater(w):
    """
    Your code goes here.
    """
    # We note that if there is only one unique letter, it will fail anyway
    if len(set(w)) == 1: 
        return "no answer"

    # We reverse the string
    backwards = "".join(list(reversed(w)))

    # The indices to cut the string
    # They are row index, column index, to avoid confusion with ix and jx used in enumeration
    rx = -1
    cx = -1

    # We loop from the back of the string
    for ix, i in enumerate(backwards):

        # We nest a second loop
        for jx, j  in enumerate(backwards): 

            # We only consider those where jx < ix
            if jx < ix: 

                # Run comparison between i and j
                # We note that we want the row to be less than the column
                # Thus, we want i to be less than j
                if i < j: 

                    # When this occurs, we set rx and cx
                    # We subtract by 1 so the results are 0-indexed
                    rx = len(w) - ix - 1 
                    cx = len(w) - jx - 1

                    break

        # We note we only continue the outer for loop if we do not yet have rx and cx
        if rx > -1 and cx > -1:
            break 

    # We obtain the first section of the new word, i.e. the start of the old word up till, and excluding, rx
    start = w[:rx]

    # We obtain the middle section of the new word, i.e. from cx to the end of the old word
    mid = w[cx:]

    # If possible, we want to sort everything in 'mid', except for the first character
    mid_others = [m for m in mid[1:]]
    mid_others.sort()

    # We then reobtain mid and set it to a string
    mid = [mid[0]]
    mid.extend(mid_others)
    mid = "".join(mid)
    
    # We obtain the final section of the new word, i.e. from rx to cx, excluding cx
    # We similarly need to sort the end
    end = [e for e in w[rx:cx]]
    end.sort()
    end = "".join(end)

    # We join the words
    new = "".join([start, mid, end])

    if w == "sypjbvatgidyxodd":
        print(f"word: {w}, rx: {rx} {w[rx]}, cx: {cx} {w[cx]}, start: {start}, mid: {mid}, end: {end}")

    # Check that the new word is not the same as the old word
    if new == w: 
        return "no answer"
    
    else: 
        # Return the new word
        return new

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
    T = int(input())

    for _ in range(T):
        w = input()

        result = biggerIsGreater(w)

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