# Bigger Is Greater
## Meta Information
Start date: 20 July 2020
End date: 20 July 2020

## Solution 1
### Matrix generation
For a given string of length N, we first create a matrix of NxN. The rows and columns are the characters in the string, in order. We are, however, only interested in the upper right triangle of this matrix. 

### Matrix population
We are only interested in elements of the matrix whereby the column index is greater than the row index. This allows us to populate all elements in the matrix above the diagonal line. 

The value of the element is True if the row character is smaller than the column character. We do this for all elements above the diagonal line. 

### Character shuffling
Going from the bottom right of the populated values, we check leftwards for a True value. If we exhaust a particular row, we repeat from the rightmost column of the next (upper) row. 

Once we find a 'True' value, we select the character in the current column and all characters to the right of this character and place this set of characters in front of the character in the current row. This should give us the answer. 

### Optimisations
Instead of using a matrix, we note that we only need to identify the first 'True' value. 

Thus, we loop through every character in the string, from back to front, where i is the character in question. Then we nest a second loop within this first loop, where j is the character in question. The indices ix and jx are used to denote the 0-indexed indices, working from the back. So, the (N-1)th index is now the 0 index, the (N-2)th index is now the 1 index, and so on. We only perform a comparison if jx < ix. 

When we obtain the first True, we keep all letters from the 0th index of the original string, up to but not including i. Then, we replace it with the characters from j to the end, and then the characters from i to j, exclusive of j. 

## Solution 2
### Modifications
As we want to get the first lowest value, we want to sort 'mid' before we add it together.

## Solution 3
### Modifications
We similarly need to sort 'end'.