#!/bin/python3

import math
import os
import random
import re
import sys

"""
Data management
---------------
All string data will be converted to arrays upon being parsed to highestValuePalindrome(). 

They will only be converted back to strings upon returning in highestValuePalindrome().
"""

# === Highest Value Palindrome === 

# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    """ 
    We consider the variable space.
    
    Analysing range of n and k
    --------------------------
    n > 0
    k >= 0: Gives us conclusion 1. 
        If k == 0, there are no moves permitted. 
        If s is not a palindrome, return False.
        If s is a palindrome, return True. 

    Analysing n compared with k
    ---------------------------
    n < k
        There are more moves permitted than letters.
        Change all of them to '9'.
    n == k
        There are as many moves permitted as letters.
        Change all of them to '9'.
    n > k
        There are fewer moves permitted than letters.
        We require logic. 

    Logic for n > k
    ---------------
    We keep in mind 2 cases:
    1) s is a palindrome.
        a) If k is odd:
        ---------------
        We change the middle value to '9'. We then change (k - 1)/2 elements from the front and back to '9', skipping existing '9's where appropriate. 

        We need better logic to accommodate the 'where appropriate' part.

        b) If k is even:
        ----------------
        We change k/2 elements from the front and back to '9', skipping existing '9's where appropriate.

        We need better logic to accommodate the 'where appropriate' part.

        NOTE:
        -----
        Cases a) and b) are similar except for the changing of the center numeric value. 
    2) s is not a palindrome.
        We set values, incrementally, to '9' where appropriate.

    Setting values to '9'
    ---------------------
    We assume s is not a palindrome. We set half_k = math.floor(k/2).

    We set the first and last half_k be '9'. We then record the number of changes we made. We then decrement k by the number of changes. We repeat this process until k is 0 or we reach the middle of the string. We do not stop it prematurely due to the possibility of the center of the half-strings being '9's. 
    """
    # Unwrap s
    s = unwrap(s)

    # Check value of k
    if k == 0:
        # If s is not a palindrome, False 
        # Else if s is a palindrome, True
        if isPalindrome(s, n):
            return wrap(s)
        else:
            return fail()
    else: # k > 0
        if n <= k: 
            s = idealPalindrome(n)
            return wrap(s)

        else: # n > k
            # Get the palindrome of s
            s, changes, len_changes = getPalindrome(s, n)

            # If the number of changes == k, we return the palindrome
            # Elif the number of changes > k, we return -1
            if len_changes == k: 
                return wrap(s)
            elif len_changes > k:
                return fail()
            else: # We can maximise values here
                s = maximisePalindrome(s, changes, n, len_changes, k)


    

    return wrap(s)


# === Palindrome functions ===
def isPalindrome(s, n):
    """Checks if s is a palindrome."""
    for ix in range(half(n)): 
        if s[ix] != s[len(s) - ix - 1]:
            return False 
        
    return True


def idealPalindrome(n):
    """Generates an array of length n with the character '9'"""
    return ['9'] * n
    

def getPalindrome(s, n):
    """Returns the palindrome of s, as well as the changes required to change it to a palindrome."""
    changes = [None] * len(s) 

    for ix in range(half(n)):
        backx = len(s) - ix - 1
        if s[ix] != s[backx]: 
            larger = max(s[ix], s[backx]) 
            
            if s[ix] != larger:
                changes[ix] = larger 
                s[ix] = larger 
            elif s[backx] != larger:
                changes[ix] = larger 
                s[backx] = larger
    
    return s, changes, len(list(filter(lambda x: x is not None, changes)))


def maximisePalindrome(s, changes, n, used_moves, k):
    """Returns s, maximised"""
    moves = used_moves

    for ix in range(half(n)):
        backx = len(s) - ix - 1

        moves_required = []

        if ix == backx:
            if s[ix] != '9':
                moves_required.append(ix)
                
                if changes[ix] is not None:
                    moves_required.append(None)

        else: 
            if s[ix] != '9':
                moves_required.append(ix)
                
                if changes[ix] is not None:
                    moves_required.append(None)

            if s[backx] != '9':
                moves_required.append(backx)
                
                if changes[backx] is not None:
                    moves_required.append(None)
                
        len_moves_required = len(list(filter(lambda x: x is not None, moves_required))) - len(list(filter(lambda x: x is None, moves_required)))

        # # DEBUG(moves, moves_required, changes, moves + len_moves_required <= k)

        if moves + len_moves_required <= k:
            moves += len_moves_required

            for i in moves_required: 
                if i is not None: 
                    # DEBUG(i)
                    s[i] = '9'
            

            # Do we have to change both to '9'
            # TODO

            # if s[ix] != '9' and s[backx] != '9' and moves <= k - 2:
            #     s[ix] = '9'
            #     s[backx] = '9'

                

            #     moves += 2
                
            # elif s[ix] != '9' and moves < k:
            #     s[ix] = '9'

            #     if changes[ix] == None: 
            #         moves += 1
            
            # elif s[backx] != '9' and moves < k:
            #     s[backx] = '9'

            #     if changes[backx] == None: 
            #         moves += 1

    DEBUG(moves, k)

    return s
    

# === Math functions ===
def half(n):
    return math.ceil(n/2)


# === Fail returns ===
def fail():
    return "-1"


    # # Unwrap s into an array
    # s = unwrap(s)

    # if k == 0:
    #     # Check if s is a palindrome

    #     # If s is a palindrome, return s
    #     # Else, return -1
    #     if isPalindrome(s):
    #         return wrap(s)
    #     else:
    #         return '-1'
        
    # if n <= k: 
    #     # Return ideal palindrome
    #     return idealPalindrome(n)

    # # n > k

    # # Get the palindrome #pal# of s
    # pal = getPalindrome(s)

    # # Get the number of changes required to change s to pal
    # s2pal, s2palSum = getChanges(s, pal)

    # DEBUG("ARG CHECK:", "s:", s, "pal:", pal, "s2pal:", s2pal, "s2palSum:", s2palSum, "k:", k)

    # # If the number of changes == k, we return pal
    # # Elif the number of changes > k, we return -1
    # if s2palSum == k: 
    #     return wrap(pal)
    # elif s2palSum > k:
    #     return '-1'

    # # We require logic to change only certain parts of the string to '9', maximising the palindrome.

    # half_n = math.ceil(n/2) # Half the length of the string

    # start_index = 0

    # reservedPal = pal.copy()

    # for index in range(half_n):
    #     # We change the first and last elements to k, looping up to half_n
    #     newPal = pal
    #     newPal[index] = '9'

    #     # Switch newPal to a palindrome and get the total required changes
    #     newPal = getPalindrome(newPal)
    #     pal2NewPal, pal2NewPalSum = getChanges(pal, newPal)
    #     s2NewPal, s2NewPalSum = getChanges(s, newPal)

    #     totalChanges = max(pal2NewPalSum, s2NewPalSum)

    #     DEBUG("LOOP CHECK:", "k:", k, "newPal:", newPal, "pal:", pal, "pal changes:", pal2NewPal, "s:", s, "s changes:", s2NewPal, "total changes:", totalChanges, sep='\n')

    #     if totalChanges <= k:
    #         DEBUG("APPLY CHANGE")

    #         k -= totalChanges

    #         pal = applyChanges(pal, pal2NewPal)
    #         s = applyChanges(s, s2NewPal)
    #     else:
    #         pal = reservedPal.copy()

    #     if k == 0: 
    #         break 

    # return wrap(pal)

    # while True:
        

        
        
        
        # # We only want to edit s from index 0 to math.floor(len(s)/2)
        # # # Get the start index and the length of half_k
        # # Cap the end_index
        # start_index, end_index, changes = getHalfKChanges(k, start_index, n)

        # if start_index == end_index:
        #     # No changes can be made
        #     break 

        # # Get the maximised palindrome based on half_k number of changes
        # # We set the first and last half_k of the palindrome #pal# to '9's
        # maxPal = applyChanges(pal, changes)
        # maxPal = getPalindrome(maxPal)
        # changes, _ = getChanges(s, maxPal)
        
        # # Get the changes from s to maxPal
        # s2maxPal, s2maxPalSum = getChanges(s, maxPal)

        # if s2maxPalSum <= k:
        #     # Apply the changes
        #     k -= s2maxPalSum

        #     s = applyChanges(s, changes)
        #     pal = applyChanges(pal, changes)
            
        #     if k == 0: 
        #         break

    # return wrap(pal)
    

# # === Palindrome ===
# def isPalindrome(string):
#     """
#     Checks if the given array forms a palindrome
#     """
#     try: 
#         for ix in range(math.floor(len(string)/2)):
#             assert string[ix] == string[len(string) - ix - 1] 
#     except AssertionError:
#         return False 

#     return True 


# def getPalindrome(s):
#     """
#     Gets the palindrome of the string.
#     When comparing two numbers, it keeps the higher number.
#     """
#     string = s.copy()

#     for ix in range(math.floor(len(string)/2)):
#         larger_number = max(int(string[ix]), int(string[len(string) - ix - 1]))

#         string[ix] = str(larger_number)
#         string[len(string) - ix - 1] = string[ix] 

#     return string


# def idealPalindrome(number):
#     """
#     Returns an array of '9's of length number.
#     """
#     return ['9'] * number


# def getChanges(old, new):
#     """
#     Gets the changes required to change old to new.
#     Returns the required changes and the number of changes required.
#     """
#     changes = [c[1] if c[0] != c[1] else None for c in zip(old, new)]
    
#     return changes, len(list(filter(lambda x: x is not None, changes)))
    

# def applyChanges(string, changes):
#     """
#     Applies the changes to the given string.
#     """
#     return [c[1] if c[1] is not None else c[0] for c in zip(string, changes)]


# def getHalfKChanges(k, start_index, n):
#     """
#     Returns the starting and ending index of changes to be applied, as well as the required changes to maximise the given palindrome of length n. 

#     Starting and ending index encapsulates a range that is exclusive of the ending index.
#     """
#     if k == 1:
#         half_k = 1
#     else:
#         half_k = math.floor(k/2)

#     start = start_index
#     end = start_index + half_k

#     changes = [None] * n
     
#     for i in range(end - start):
#         changes[i + start] = '9'

#     return start, end, changes


# === String wrapping and unwrapping ===
def unwrap(string):
    """
    Converts a string to an array of characters.
    """
    return [c for c in string]


def wrap(array):
    """
    Converts an array of characters to a string.
    """
    return "".join(array)


# === Debug ===
def DEBUG(*args, **kwargs):
    print(*args, **kwargs)
    

    



    
    




#     if n <= k:
#         return ''.join(findIdealPalindrome(s))

#     # Get the palindrome of s
#     pal = findPalindrome(s) 

#     # Get changes to get the palindrome
#     s2pal = getChanges(s, pal) 

#     # Check that the number of changes is permitted
#     s2palSum = len(list(filter(lambda x: x is not None, s2pal)))

#     # print(s, pal, s2pal, list(filter(lambda x: x is not None, s2pal)))

#     if s2palSum > k:
#         # If the number of changes is greater than the permitted number of changes, return '-1'
#         return '-1'
#     elif s2palSum == k: 
#         # Elif the number of changes is equal to the permitted number of changes, we return the palindrome as is
#         return ''.join(pal)

#     # We know more than the minimum number of moves can be made
#     # We want each one to maximise the value of the palindrome as much as it can, without exceeding the number of moves permitted
    
#     # For each index in pal, up to half its length, rounded up, we set it to 9 and get the required changes and compare this with the moves permitted
#     for i in range(math.ceil(n/2)):
#         idealPal = pal[:] # Copy the list instead of the reference

#         # Set the i'th value to '9'
#         idealPal[i] = '9'

#         # Find the palindrome of idealPal
#         idealPal = findPalindrome(idealPal)

#         # Get the number of changes required
#         s2idealPal = getChanges(s, idealPal)
#         s2idealPalSum = len(list(filter(lambda x: x is not None, s2idealPal)))

#         # If s2idealPalSum is less than the permitted number of moves, we set this as pal and we check the rest
#         # If s2idealPalSum is equal to the permitted number of moves, we take this value immediately
#         # If it is greater, we skip the value
#         if s2idealPalSum < k:
#             pal = idealPal 
#         elif s2idealPalSum == k:
#             pal = idealPal
            
#             break 
#         else:
#             # TODO If it exceeds, does it logically mean we JUMP to the middle to check if it can be 9'ed?
#             # Or should we throw half of the available remaining moves on the first half of the string, and repeat until we go down to the ones? 
#             continue 

#     # return (''.join(pal),
#     #     "s:", s, 
#     #     "n:", n, 
#     #     "k:", k, 
#     #     "pal:", pal, 
#     #     "s2pal:", s2pal, 
#     #     "s2palSum:", s2palSum, 
#     #     "idealPal:", idealPal, 
#     #     "s2idealPal:", s2idealPal, 
#     #     "s2idealPalSum:", s2idealPalSum
#     #     )

#     return ''.join(pal)

    
        
#     assert False, (
#         "s:", s, 
#         "n:", n, 
#         "k:", k, 
#         "pal:", pal, 
#         "s2pal:", s2pal, 
#         "s2palSum:", s2palSum, 
#         "idealPal:", idealPal, 
#         "s2idealPal:", s2idealPal, 
#         "s2idealPalSum:", s2idealPalSum
#         )





#     # TODO We need to increment from the back and front, ideally collecting the required changes via getChanges() and then checking that the sum is less than or equal to the required number of moves; if it exceeds, take the previously legalised number
    



#     # Here, we know that you can attempt more than the minimum required to become a palindrome
#     # Attempt to maximise a few numbers
#     # We look at changing all the changes in s2pal to '9'
#     s2idealPal = ['9' if t is not None else None for t in s2pal]
    
#     # We apply s2idealPal to the palindrome and find the required changes
#     # This is the new s2idealPal
#     s2idealPal = applyChanges(s, s2idealPal)
#     s2idealPal = findPalindrome(s2idealPal)
#     s2idealPal = getChanges(s, s2idealPal)

#     s2idealPalSum = sum(list(map(lambda x: x is not None, s2idealPal)))

#     # if s2idealPalSum == k:
#         # This is the perfect 


#     # # Here, we identify three types of strings that can be returned. 
#     # # - We ignore the case where all are 9s, as this is captured above
#     # # The palindrome
#     # # The idealised palindrome, where the changes made are all '9's
#     # # - We keep in mind this can be None if the initial string is a palindrome
#     # # The incremental palindrome, where the changes are incrementally made
#     # s2incPal = [None for t in s2pal]

#     # # We know moves_remaining > 0
    
#     # # We ensure that the change s



#     # # Get the remaining number of moves
#     # moves_remaining = k - s2palSum


#     assert False, str([s, s2idealPal])

#     # Here, we know the number of permitted changes exceeds the number of required changes to at least make it a palindrome
#     # We want to change it to a palindrome first and foremost, so we work from #pal#
    
#     # print(pal)

#     # For every character in pal, we want to maximise it
#     for cx, c in enumerate(pal):
#         first = pal[cx]
#         second = pal[len(pal) - cx - 1]

#         moves_required = sum([first != '9', second != '9'])
#         moves_made = sum([s2pal[cx] is not None, s2pal[len(pal) - cx - 1] is not None])

#         # We decrement moves_required by 1 if it's the middle value of the palindrome
#         if len(pal) % 2 == 1 and cx == math.floor(len(pal)/2):
#             moves_required -= 1

#         # print(first, second, moves_required, moves_remaining, s2pal, moves_made)

#         if moves_required - moves_made <= moves_remaining:
#             pal[cx] = '9'
#             pal[len(pal) - cx - 1] = '9'

#             moves_remaining -= moves_required + moves_made

#         assert moves_remaining == 0, moves_remaining

#         # Break if it's beyond half the palindrome
#         # if cx > math.floor(len(pal)/2):
#         #     break

#     # print(pal)


#     # # Else, we can change 1 or more of the values to '9'

#     # # Get ideal palindrome
#     # idealPal = findIdealPalindrome(s)

#     # # Get changes to ideal palindrome
#     # s2idealPal = getChanges(s, idealPal)

#     # # Get number of changes to ideal palindrome
#     # s2idealPalSum = len(list(filter(lambda x: x is not None, s2idealPal)))

#     # # We have s2pal and s2idealPal, where s2idealPal has equal or more non-None elements than s2pal
#     # # We go element by element for every character in #pal#
#     # # If the index of the element is in s2pal, we decrement the moves required by 1 and apply the change to the front and back of #pal#
#     # # If the index of the element is not in s2pal, we decrement the moves required by 2
#     # moves_remaining = k - s2palSum

#     # print(s, pal, s2pal, idealPal, s2idealPal, s2idealPalSum, moves_remaining)

#     # for cx, c in enumerate(pal): 
#     #     if s2pal[cx] is not None and moves_remaining >= 1:
#     #         moves_remaining -= 1
            
#     #         pal[cx] = '9'
#     #         pal[len(pal) - cx - 1] = '9'

#     #     elif s2pal[cx] is None and moves_remaining >= 2:
#     #         moves_remaining -= 2

#     #         pal[cx] = '9'
#     #         pal[len(pal) - cx - 1] = '9'

#     #     if moves_remaining < 0:
#     #         raise Exception('Negative moves remaining. Logic error.')
        
    

#     return ''.join(pal)

# def splitString(s):
#     n = len(s) 

#     # Splits a string into the first half, the middle, and the last half
#     first = s[:math.floor(n/2)]
#     if n % 2 == 1:
#         mid = s[math.floor(n/2)]
#     else:
#         mid = ''
#     second = ''.join(reversed(s))[:math.floor(n/2)]

#     # Return as arrays
#     first = [c for c in first]
#     mid = [mid]
#     second = [c for c in second]

#     return first, mid, second 

# def findPalindrome(s):
#     # Finds the required changes to #s# to make it a palindrome
#     # Going by the required policy, we aim to maximise the value being changed
#     # i.e. the value that's being changed should always be increased
#     first, mid, second = splitString(s)

#     for (ix, iStr), (jx, jStr) in zip(enumerate(first), enumerate(second)):
#         i = int(iStr)
#         j = int(jStr) 

#         if i == j:
#             continue
#         else:
#             first[ix] = str(max(i, j))
#             second[ix] = str(max(i, j))
            
#     pal = first 
#     if mid != ['']: 
#         pal += mid
#     pal += list(reversed(second))

#     return pal

# def findIdealPalindrome(s):
#     # Finds the ideal palindrome of the same length, but with all characters being '9'
#     return ['9' for c in s]

# def getChanges(s1, s2):
#     # Returns an array of equal length to s1 and s2
#     # Each element of the array corresponds to the change to s1 to make it s2
#     changes = []

#     for i, j in zip(s1, s2):
#         # print(i, j, i == j)
         
#         if i == j: 
#             changes.append(None)
#         else:
#             changes.append(j)

#     return changes 


# def applyChanges(s1, s2):
#     # Applies the changes in s2 that are not none to the elements in s1

#     s1 = [c for c in s1]

#     for ((ix, i), j) in zip(enumerate(s1), s2):
#         if j is not None:
#             s1[ix] = j

#     return ''.join(s1)


    


#     # # Instantiate palindrome as empty string
#     # palindrome = ''

#     # # Check to see if there's a middle, untouched character
#     # s_is_odd = len(s) % 2 == 1
#     # oddity = [None] if s_is_odd else []

#     # # Get the number of changes required to change it to a palindrome
#     # changes, rev_changes = change_to_palindrome(s)
#     # total_changes = changes + oddity + list(reversed(rev_changes))

#     # # Check if s is palindrome
#     # number_of_changes = sum([x is not None for x in total_changes])

#     # # Check if we are allowed the number of changes
#     # # If this is negative, we know there are more changes required than permitted
#     # # Thus it is impossible
#     # # If this is 0, we know the exact number of change required
#     # # Thus, we set the changes
#     # # If this is greater than 0, we have a few options to explore
#     # extra_changes_permitted = k - number_of_changes

#     # if extra_changes_permitted == -1:
#     #     return '-1'
#     # elif extra_changes_permitted == 0:
#     #     palindrome = [t[0] if t[1] is None else t[1] for t in zip(s, total_changes)]

#     #     return ''.join(palindrome)
#     # else:
#     #     # Instantiate palindrome
#     #     palindrome = [char for char in s]

#     #     # We get the maximal palindrome of 9999...
#     #     ideal_maximum_palindrome = ['9' for char in s]

#     #     # Obtain the 'ideal' number of changes
#     #     idealised_changes = [t[0] if t[0] is None or int(t[0]) > int(t[1]) else t[1] for t in zip(total_changes, ideal_maximum_palindrome)]

#     #     # Here we know it is definitely even
#     #     while extra_changes_permitted > 0:
#     #         for i in range(len(ideal_maximum_palindrome)):
#     #             if idealised_changes[i] == '9' and i != math.ceil(len(s)/2) - 1:
#     #                 idealised_changes[len(idealised_changes) - i - 1] = '9'

#     #                 extra_changes_permitted -= 1

#     #                 break 

#     #         if i == range(len(ideal_maximum_palindrome)):
#     #             break
        
#     #     if s_is_odd and extra_changes_permitted % 2 == 1 and extra_changes_permitted > 0:
#     #         idealised_changes[math.ceil(len(s)/2) - 1] = '9'

#     #         extra_changes_permitted -= 1
#     #     # # Finalise changes by selecting changes only from front to end
#     #     # permitted_finalised_changes = sum([t is not None for t in idealised_changes])
#     #     # finalised_changes = [None for t in idealised_changes]
        
#     #     # # We know permitted finalised_changes is either odd or even
#     #     # # If it's odd we add the middle change
#     #     # if permitted_finalised_changes % 2 == 1:
#     #     #     finalised_changes[math.ceil(len(s/2)) - 1] = '9'

#     #     #     permitted_finalised_changes -= 1

#     #     # # Here, we know permitted finalised changes even

        

#     #     # Implement changes
#     #     palindrome = [t[0] if t[1] is None else t[1] for t in zip(palindrome, idealised_changes)]
        
#     #     return ''.join(palindrome)

#     #     # return ''.join(palindrome)

#     #     print('ideal max palindrome:', ideal_maximum_palindrome)
#     #     print('ideal changes:', idealised_changes)

#     #     # If it is 2, we instantiate the change, not just for the suggested changes, but for their counterparts, i.e. instead of changing i[0] to equal to i[len(s)], we change BOTH to 9. We do this working incrementally from changes and rev_changes
#     #     # If it is 3, we do the case of 1 and 2
#     #     # If it is 4, we can do 2 twice
#     #     # If it is 5, we can do the case of 1 and 4
#     #     # Essentially, if it is odd, we do the case of 1. Then, we take care of the case of 2n. 
#     #     # palindome = [char for char in s]
#     #     # if extra_changes_permitted % 2 == 1:
#     #     #     palindrome[math.ceil(len(s) / 2)] = 9

#     #     #     extra_changes_permitted -= 1

#     #     # while extra_changes_permitted > 0:

        
        

#     # print('s is odd:', s_is_odd)
#     # print('s:', s)
#     # print('changes:', changes, rev_changes)
#     # print('total changes:', total_changes)
#     # print('number of changes:', number_of_changes)
#     # print('extra change permitted:', extra_changes_permitted)
#     # print('palindrome:', palindrome)
#     # # We first want to check if it's a palindrome
#     # s_is_palindrome = is_palindrome(s)

#     # # If s is not a palindrome, change it to a palindrome
#     # if not s_is_palindrome:
#     #     palindrome, changes = change_to_palindrome(s)

    

#     # We check how many moves we can make
#     # k = 1, 2, 3...
#     # If k is 0 and s is a palindrome, we return s as is
#     # If k is 1 and s is a palindrome, we have four cases
#         # k = 1                 # s is odd              # s is even
#         # s is a palindrome     Mid char to 9           Nothing
#         # s is not a palindrome Change to palindrome    Change to palindrome

# def split_string(s):
#     """
#     Splits into first and second half
#     """
#     if len(s) % 2 == 1: # odd
#         odd = True
#     else:
#         odd = False 

#     middle_character = ''

#     if odd:
#         middle_character = s[math.ceil(len(s)/2)]

#     first_half = s[:math.floor(len(s)/2)]
#     second_half = ''.join(reversed(s))[:math.floor(len(s)/2)]

#     return first_half, middle_character, second_half


# def is_palindrome(s):
#     """
#     Checks if is palindrome
#     """
#     first, mid, second = split_string(s) 
#     return first == second


# def change_to_palindrome(s):
#     """
#     Gives suggested changes index-wise to change s to a palindrome
#     No 'maximising' of palindrome
#     """
#     first, mid, second = split_string(s)

#     first_changes = [None for t in range(len(first))]
#     second_changes = [None for t in range(len(second))]

#     # suggested_changes = [None for t in range(len(s))]

#     for (ix, str_i), (jx, str_j) in zip(enumerate(first), enumerate(second)):
#         i = int(str_i)
#         j = int(str_j)

#         if i == j:
#             continue 
#         elif i > j:
#             second_changes[jx] = str(i) 
#         elif i < j: 
#             first_changes[ix] = str(j)

#     return first_changes, second_changes