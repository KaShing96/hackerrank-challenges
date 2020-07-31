2020.07.18: 
    Return to Maximum Subarray after a long hiatus. 

    Implemented reMarkable code logic. The function initially still timed out due to the presence of the DEBUG function. After commenting this out, both test and verification functions passed.

2020.06.04:
    A simpler solution has been devised for obtaining the maximum subarray, and is found on the reMarkable.

    === TO DO ===
    Implement reMarkable code logic.

2020.06.03:
    We loop through each number.

    As we do, we add the number to a set of numbers. Then we have three operations we can choose from: 

    1. Keep the first in the set and drop the last in the set.
    2. Drop the first in the set and keep the last in the set.
    3. Keep everything in the set. 

    We compute the sums for all three values. If CASE1 is maximum, we add it to the record, because we do not want to drop the last in the set as that will break the condition for the maximum subarray.

    Then, between CASE2 and CASE3, the larger case gets selected, and the set is maintained. 

    If there are no new numbers, we break the loop.

    === CONCLUSION ===
    The updated method seems to work time-wise. However, there is still an error in one of the verification tests. 

2020.06.01: 
    The problem is found here: https://www.hackerrank.com/challenges/maxsubarray/problem
    
    We use a naive approach to solve 1) and 2). 

    We realise that having a nested loop for the array will result ultimately in exceeding the time limit for a verification scenario, necessitating the removal of the nested loop.
