2020.05.14: 
    The accuracy issues raised by the test arise because the 'fnc.fptr.answers' variable is not being reset between tests. Changing the extraction of answers to a method under fnc.fptr which resets the '.answers' variable solved the issue.

    SUCCESS!

2020.05.13:
    Completed a primitive execution of palindromeIndex() by doing simple character removal of each character and checking if it is a palindrome. 

    This succeeded on the test cases but failed on some verification cases.

    We attempt a different methodology. Given a string s of length n, we check from the edges inwards. If the edges are equal, we check inwards. If the edges are NOT equal, we split the string into two potential strings: a and b. We then check if either a or b are palindromes. If neither of them are palindromes, we return -1. 

    The test runs extremely quickly. However, there are accuracy issues with the test. 

    === TODO ===
    Debug the accuracy issues raised by the test. 

2020.05.12: 
    Completed the test environment. 

    === TODO ===
    I can try to proceed with palindromeIndex() by doing a simple character removal of each character and checking if it is a palindrome. 

2020.05.11:
    Developed the test environment further with functions.main() and functions.input() functions.

    .main() is simply a wrapper for the code executed in functions.py. 

    .input() aims to mock the input() function so a more straightforward copy-paste of the problem from HackerRank can be performed.

    === TODO ===
    We aim to 'update' a list of mockable data by input() with each test case. Calling .main() will then run HackerRank's `if __name__ == '__main__'` block, with the input() command mocked by .input(). 

2020.05.09: 
    Start. 

    Redid test_functions.py to reduce overhead in converting .txt arguments to .json arguments when porting case values from HackerRank to local.