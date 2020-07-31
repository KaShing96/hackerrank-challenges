2020.05.29:
    By adding a break clause to the outer i loop, we reduce the program's runtime. 

    However, the crux of the error lay in the case where i == j or i.upper() == j, where we considered both 'keep' and 'remove' cases without accounting for whether i itself was strictly uppercase or lowercase -- in one of these cases, we cannot consider the 'remove' case. 

    We fixed this. However, runtime was still an issue.

    We remedy this by removing the list(map()) call on ors. Instead of saving the reference elements of the cache,  we instead directly save the value of the cache into the ors list, before calling any() on ors. 

    THIS SUCCEEDED.

2020.05.28: 
    Dynamic programming completed, even if I am severely over time. There seems to be a problem with the verification cases.

2020.05.27: 
    Brief attempt at moving the dynamic programming to the main function. Little progress.

2020.05.24: 
    Dynamic programming is a bit difficult to implement. 

2020.05.23: 
    The logic for dynamic programming was identified by exploring the list of possible values a and b can take, assuming truncation from the front. The logic is given in reMarkable.

2020.05.22:
    It is apparent that the secret to solving this problem lies in dynamic programming. We need to identify the recursion - which we currently have as abbreviations(), and apply dynamic programming to it by storing values in a table. 

2020.05.21: 
    While the while loop is successful in replicating the recursion, it ultimately takes too long, prompting the FunctionTimedOut error. We need to explore an alternative logic. 

2020.05.20: 
    We added an extra rule that checked if the number of capitalised letters in a exceeded the number of capitalised letters in b. In this case, no removal from a can equate it to b, resulting in a fail. 

    Upon checking the error in verifications.txt, we also realise this is prompted by a Recursion Error. Thus, we switch it to a while loop.
    
    The code is rewritten in reMarkable under a similar logic. 
    
    === PSEUDOCODE ===

    # We note due to the presence of ONE path of recursion, we need to use fail() and success() and equate any possible fail and success conditions to fail() and success() respectively.

    while True
        IF a = b?
            success

        ELSE:             
            IF len(a) > len(b)? 
                # Truncation can still happen! 

                IF len(b) == 0:
                    # All letters in a must be lowercase, or they cannot all be removed
                    IF a == a.lowercase
                        success

                    ELSE
                        fail

                ELSE
                    i = a[0], j = b[0]

                    IF i = i.upper()
                        # i cannot be removed from a

                        IF i = j: 
                            # They are the same and i cannot be removed. Thus
                            a = a[1:]
                            b = b[1:]

                            CONTINUE LOOP
                        
                        ELSE:
                            # They are not equal and i cannot be removed
                            fail

                    ELSE
                        # i can be removed from a

                        IF i = j:
                            # 2 scenarios: keep and remove
                            # Difficult to run two while loops in parallel here, so we instead call abbrev again

                        ELSE:
                            # we remove i
                            a = [1:]

                            CONTINUE WHILE LOOP

            ELIF len(a) <= len(b)? 
                # No truncation can happen. If a is shorter than or similar length to b but is not equal to b this is an automatic fail
                FAIL

2020.05.19: 
    The previous logic works on all verification tests. 

    However, when submitted to HackerRank, new errors came to light. These errors have been added to verifications.txt but have not been analysed. 

    An additional point of note is the use of success() and fail(), which interfered with the traditional use of True and False. Calling abbreviations() ultimately returned a string, which always evaluated for True when under the condition of 'if abbreviation()', as opposed to 'if abbreviation() == success()'.

    === TO DO ===
    
    Analyse errors in verifications.txt.

2020.05.18: 
    The suggested use of regexes from yesterday seems overly complicated. Thus, we consult the HackerRank page directly.

    From the given HackerRank page, we've devised a custom logic flow that should work. The logic flow is given, in its early stages, on the reMarkable tablet. It is given, textually, as follows: 

    === 

    Given two strings a and b: 

    STEP 1: a == b? 

    If 1=>TRUE, we return SUCCESS. 
    If 1=>FALSE, we check the first letter in a and b, termed i and j respectively. 

    STEP 1.1: i == j or i.upper() == j? 

    If 1.1=>FALSE, we know that the first letter in a is completely different from that in b. Thus, we want to check if i can be truncated from a. 

    STEP 1.1.1: i == i.upper()? 

    If 1.1.1=>TRUE, we know the first letter in a does NOT match with the first letter in b and cannot be removed. Thus, we return NONE, to signify an end of this exploration branch. 

    Else if 1.1.1=>FALSE, we know the first letter in a can be truncated away. Thus, a = a[1:]. Then, we repeat STEP 1. 

    Working back to STEP 1.1, if 1.1=>TRUE, e know that the first letter in a can match with the first letter in b, whether the first letter in a first needs to be capitalised or not. Thus, we check the following: 

    STEP 1.1.2: i == i.upper()? 

    If 1.1.2=>TRUE, we know that i is already capitalised, and CANNOT be removed. Thus, we truncate both a and b. a = a[1:] and b = b[1:] and restart the process from STEP 1. 

    Else if 1.1.2=>FALSE, we know i is not capitalised. Thus, we can attempt to either capitalise it and keep it, or discard it and try again. We have two branches: 

    STEP 1.1.2.1: a = a[1:]

    STEP 1.1.2.2: a = a[1:]; b = b[1:]

    We try STEP 1 for both of these scenarios and return the OR of their case. 

2020.05.17:
    No progress in resolving the issue. 

    One potential venue to explore is the use of regexes. We can assert that B can be transformed into A by the addition of any number of lowercase characters, as well as the transformation of any combination of letters in B to lowercase. 

    Failing that, we can consult the HackerRank discussion page.

2020.05.16: 
    By changing the if condition to append for if the character in A is uppercase, the test cases were solved.

    However, several verification problems still raised errors. 

    We are attempting to debug a particular case, where a lowercase 'x' is appearing in the result when it should not be. 

2020.05.15:
    Attempting Abbreviations, which has been put on hold for several weeks. 

    We will try to use the method we learned from the common_child problem and run through the two substrings, building the final substring. The substring building process adheres to rules 1 and 2 of the abbreviation problem, failing which the substring is not extended. 

    === CONCLUSION ===
    The function runs quick enough, but the method of appending elements into the TAM needs to be cleared up. In the case of KXzQ and K, the result is recorded as K, even though you can't remove X or Q from KXzQ. 