def commonChild(s1, s2):
    """
    Finds the longest substrings of s1 and s2 that match and returns its length.
    """
    # Traceback approach only needs to hold two rows of s2 (we assume characters in s2 make up the columns)
    tb = [[0 for _ in s2] for _ in range(2)]

    # DEBUG_MATRIX(s1, s2, tb) 

    # Loop through s1 and s2
    for ix in range(len(s1)): 
        for jx in range(len(s2)):
            # Get element indices
            i1 = ix % 2 # This row
            i2 = 1 - i1 # Other row
            
            length = 0

            # Check for match
            if s1[ix] == s2[jx]:
                length = 1

                # Check for possible increment
                if jx > 0: 
                    length += tb[i2][jx - 1]

            else: 
                # Get max of top and left
                # Set length as top
                length = tb[i2][jx]

                # Check length against left
                if jx > 0: 
                    if length < tb[i1][jx - 1]:
                        length = tb[i1][jx - 1]

            tb[i1][jx] = length

    return tb[i1][-1]
            

    # # Loop through s1 and s2
    # for ix, i in enumerate(s1): 
    #     tb = [] 
        
    #     for jx, j in enumerate(s2): 
    #         if i == j: 
    #             length = 1

    #             if tb_history != [] and jx > 0: 
    #                     length += tb_history[jx - 1]

    #             tb.append(length) 

    #         else: 
    #             if tb_history != []: 
    #                 top = tb_history[jx]
    #             else:
    #                 top = 0

    #             if jx > 0: 
    #                 left = tb[jx-1]
    #             else:
    #                 left = 0

    #             length = max(top, left)

    #             tb.append(length)

    #     tb_history = tb

    # return tb[-1]

    # DEBUG(tb_history, tb)
        
        # tb.append([])

        # for jx, j in enumerate(s2): 
        #     length = 0

        #     if i == j: 
        #         if ix == 0 or jx == 0: 
        #             length = 1
        #         else: 
        #             length = tb[-2][jx - 1] + 1

        #     # else: 
        #         # top = tb[-2][jx]

        #         # if ix == 0:
        #         #     top = 0

        #     tb[-1].append(length) 

        # DEBUG(tb)

        # if ix != 0: 
        #     tb.pop(0)
            
    # DEBUG(tb)

    return 0


    # # for ix in range(len(s1) + 1): 
    #     tb.append([])

    #     for jx in range(len(s2) + 1): 
    #         length = 0

    #         # Avoid uppermost and leftmost zero-padded row and column
    #         if ix > 0 and jx > 0: 
    #             # Check if match
    #             if s1[ix - 1] == s2[jx - 1]:
    #                 # Add to length of previous diagonal
    #                 length = tb[ix-1][jx-1] + 1

    #             else:
    #                 # Get maximum of adjacent cells
    #                 top = tb[ix-1][jx]
    #                 left = tb[ix][jx-1]

    #                 if ix == 0:
    #                     top = 0
                    
    #                 if jx == 0:
    #                     left = 0
                        
    #                 length = top

    #                 if left > top:
    #                     length = left 

    #         tb[ix].append(length)

    return tb[-1][-1]



    # # Traceback approach dictionary
    # tb = {}

    # # Loop through s1 and s2
    # # s1 is the rows
    # # s2 is the columns
    # for ix, i in enumerate(s1): 
    #     for jx, j in enumerate(s2): 
    #         if i == j: 
    #             length = 1

    #             try: 
    #                 length += tb[(ix-1, jx-1)]
    #             except KeyError:
    #                 length = 1

    #             tb[(ix, jx)] = length                    
                    
    #         else:
    #             try: 
    #                 top = tb[(ix-1, jx)]
    #             except KeyError:
    #                 top = 0

    #             try: 
    #                 left = tb[(ix, jx-1)]
    #             except KeyError:
    #                 left = 0

    #             length = max(top, left)

    #             tb[(ix, jx)] = length

    # DEBUG(tb.keys())

    # return tb[(len(s1) - 1, len(s2) - 1)]



    # # List to hold traceback approach
    # tb = []

    # # Create traceback approach matrix
    # for ix in range(len(s1) + 1): 
    #     tb.append([])

    #     for jx in range(len(s2) + 1): 
    #         length = 0

    #         # Avoid uppermost and leftmost zero-padded row and column
    #         if ix > 0 and jx > 0: 
    #             # Check if match
    #             if s1[ix - 1] == s2[jx - 1]:
    #                 # Add to length of previous diagonal
    #                 length = tb[ix-1][jx-1] + 1

    #             else:
    #                 # Get maximum of adjacent cells
    #                 top = tb[ix-1][jx]
    #                 left = tb[ix][jx-1]

    #                 if ix == 0:
    #                     top = 0
                    
    #                 if jx == 0:
    #                     left = 0
                        
    #                 length = top

    #                 if left > top:
    #                     length = left 

    #         tb[ix].append(length)



    # # Loop through each row, then loop through each column
    # # Each row represents each letter in s1
    # # Each column represents each letter in s2
    # for ix, i in enumerate(s1):
    #     tb.append([])
        
    #     # Check for equality
    #     for jx, j in enumerate(s2):
    #         # Instantiate element in traceback approach matrix
    #         length = 0

    #         # Check if match
    #         if i == j: 
    #             # Add to length of previous diagonal
    #             if ix == 0 or jx == 0: 
    #                 length = 1
    #             else: 
    #                 length = tb[ix-1][jx-1] + 1

    #         else: 
    #             # Get maximum of adjacent cells
    #             top = tb[ix-1][jx]
    #             left = tb[ix][jx-1]

    #             if ix == 0:
    #                 top = 0
                
    #             if jx == 0:
    #                 left = 0
                    
    #             length = top

    #             if left > top:
    #                 length = left 

    #             # tb[ix][jx] = val
    #             # DEBUG(len(s1), len(s2), ix, jx, end='\t')

    #         # Append value 
    #         tb[ix].append(length)
            

            # tb[ix].append(0)

            # # Check if match
            # if i == j: 
            #     # Add to length of previous diagonal
            #     if ix == 0 or jx == 0: 
            #         tb[ix][jx] = 1
            #     else: 
            #         tb[ix][jx] = tb[ix-1][jx-1] + 1
                    
            # else: 
            #     # Get maximum of adjacent cells
            #     top = tb[ix-1][jx]
            #     left = tb[ix][jx-1]

            #     if ix == 0:
            #         top = 0
                
            #     if jx == 0:
            #         left = 0
                    
            #     val = top

            #     if left > top:
            #         val = left 

            #     tb[ix][jx] = val
            #     DEBUG(len(s1), len(s2), ix, jx, end='\t')

    # return tb[ix][jx]


def DEBUG(*args, **kwargs):
    from pprint import pprint 

    try:
        pprint(*args, **kwargs)
    except:
        print(*args, **kwargs)

    True


def DEBUG_MATRIX(s1, s2, mat): 
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1): 

            if i == 0 and j == 0:  
                print('', end='\t')
            elif i == 0 and j != 0: 
                print(s2[j-1], end='\t')
            elif i != 0 and j == 0:
                print(s1[i-1], end='\t')
            else:
                print(mat[i-1][j-1], end='\t')

        print()

    # for i in range(len(mat) + 1): 
    #     for j in range(i + 1): 
    #         print(j, end = '\t')
        
    #     print()