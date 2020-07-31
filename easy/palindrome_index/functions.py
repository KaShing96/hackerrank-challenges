# === Function ===
def palindromeIndex(s):
    """
    Given a string of lowercase letters in the range ascii[a-z], determine a character that can be removed to make the string a palindrome. There may be more than one solution, but any will do. For example, if your string is "bcbc", you can either remove 'b' at index 0 or 'c' at index 3. If the word is already a palindrome or there is no solution, return -1. Otherwise, return the index of a character to remove.

    Given a string s of length n, we check from the edges inwards. If the edges are equal, we check inwards. If the edges are NOT equal, we split the string into two potential strings: a and b. We then check if either a or b are palindromes. If neither of them are palindromes, we return -1. 
    """
    # Check if a string is a palindrome
    if isPalindrome(s):
        
        # If the string is a palindrome, return -1
        return -1

    else:

        # We check from the edges inwards
        for cx, c in enumerate(s): 
            cx_end = len(s) - cx - 1

            # If the characters at the edges are the same, continue checking inwards
            if c == s[cx_end]:
                continue 

            # If they are different, we split them into two strings, a and b
            a = remove(s, cx)

            # If a is not a palindrome, we check b
            if isPalindrome(a): 

                return cx 
            
            else: 
                b = remove(s, cx_end)

                # If b is not a palindrome, there can be no removal of a single character
                if isPalindrome(b):

                    return cx_end

                else: 
                    return -1


        # If none of them are palindromes, return -1
    #     return -1

    # return -1


def isPalindrome(string): 
    """
    Checks if the given string is a palindrome.

    Params
    ======
    string: str
    
    Returns
    =======
    result: bool
    """
    # Length of string
    length = len(string)
    
    # Loop through every character in the string 
    for cx, c in enumerate(string): 

        # Get the last index in the string
        cx_end = length - cx - 1

        # Only check if the characters are equal if cx is strictly less than cx_end
        # If it is an even-numbered string, cx being strictly less than cx_end ends only after the midpoint
        # If it is an odd-numbered string, the loop ends when cx == cx_end, which doesn't need to be checked
        if cx >= cx_end:
            break

        # Check c with the index at the end of the string
        if c != string[cx_end]:
            return False 

    return True


def remove(string, cx): 
    """
    Removes the character from the string.

    Params
    ======
    string: str
    cx: int
        The index of the character to remove

    Returns
    =======
    _: str
    """
    return "".join([string[:cx], string[cx + 1:]])


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

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')


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

        DEBUG(string)

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