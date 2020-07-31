# === Function ===
def maxSubarray(arr):
    """
    Your code goes here.
    """
    # Maximum subarray
    # Get max subarray
    m_arr_nums = None

    # Set of numbers
    m_arr_set = []
    
    # Cache of max value
    cache = None

    # Total of m_arr_set
    total = 0

    # Loop through numbers
    for ix, i in enumerate(arr):

        # Append to existing set
        m_arr_set.append(i)

        # If this is the first element of arr, we skip the remainder of the code
        if ix == 0:
            continue

        # Else, we have two elements in m_arr_set
        # Case 1 represents the situation where the first element is larger than the second element
        # Case 2 represents the situation where the second element is larger than the first element
        # Case 3 represents the situation where both elements are larger than they are individually
        case1 = m_arr_set[0]
        case2 = m_arr_set[1]
        case3 = case1 + case2 

        # We check if Case 3
        if case3 > case2 and case3 > case1:
            
            # We set m_arr_set = [case3]
            m_arr_set = [case3]

        # We check if Case 2
        elif case2 > case1:

            # We set m_arr_set = [case2]
            m_arr_set = [case2]

        # If Case 1 is larger than Case 2 and Case 3, we cache the value
        else: 

            # If cache is None, we set it to whatever case1 is
            if cache is None: 
                cache = case1 

            # If cache is a value, we check that case1 is larger than the cache value before setting it
            elif cache < case1:
                cache = case1 

            # Otherwise, we do nothing
            
            # After setting the cache value, we need to set m_arr_set
            if case3 > case2:
                m_arr_set = [case3]

            else:
                m_arr_set = [case2]

        DEBUG(arr, case1, case2, case3, cache)

    # In the final loop, m_arr_set will consist of only one element. We compare this element with the value of cache, if it exists. We then let it be the maximum subarray value. 
    if cache and cache > m_arr_set[0]:
        m_arr_nums = cache

    else:
        m_arr_nums = m_arr_set[0]

    # Maximum subsequence
    # Get max subsequence
    m_sq = []

    # Check if first index is positive
    pos = False

    if arr[0] > 0: 
        pos = True 
        lowest = 0

    else:
        lowest = arr[0]

    for i in arr: 
        if not pos and i > 0: 
            pos = True
            
            lowest = 0
        elif not pos and i > lowest: 
            lowest = i

        if i >= lowest: 
            m_sq.append(i)

    # DEBUG(arr, lowest, m_sq)

    m_sq = list(filter(lambda x: x >= lowest, m_sq))

    DEBUG(m_arr_nums, m_sq)

    return [m_arr_nums, sum(m_sq)]


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
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        # fptr.write('\n')



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