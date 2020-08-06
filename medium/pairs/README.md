# Pairs
*This README.md is instantiated by HackerRank Coding Template Version 4.0

This problem can be found [here](https://www.hackerrank.com/challenges/pairs/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign).

# Solution 1
We attempt to run through the array twice, checking if the subtraction of each pair of values gives the desired number. 

If we let the first number be i and the second number be j, we only calculate for i - j, taking the absolute value, and only for indices ix > jx as the reverse case will only give us a mirror, i.e. abs(j - i) = abs(i - j).

This solution, however, does not run within the desired time limit for some cases.

# Solution 2
Drawing inspiration from the two-pointer technique, for every given element in `arr`, there will thus only be *one* other element of which the subtraction gives us `k`. Thus, when we increment the `answers` variable, we break the `jx` loop and continue the `ix` loop.

We also note that we must first sort `arr`. If we are running loops by the condition of `jx >= ix`, this suggests that we can substitute it by `j >= i`, suggesting that we don't take `abs(j-i)` but instead take `j-i`. This also suggests that all `j` will be larger than the given `i` after the number is incremented, allowing us to break the `jx` loop after an increment in `answer`.

This fails on time limits as well, though it succeeds for a greater number of tests. 

# Solution 3
We gain one more insight from **Solution 2**. Assume we have `n` elements in `arr`, where `arr` is sorted in ascending order, and we loop through them with the variables `i` and `j`, where `i < j` (or, alternatively, our condition of `j >= i`). Here, 

If `i=1` and `j=4` and `j - i = k`, we know that for `i = 2`, the only values of `j` which give `j - i = k` will be `j > 4`. Thus, instead of looping from `j = i + 1`, we loop from `j = j' + 1`, where `j'` is the previous value of `j`. 

Furthermore, to avoid checking if each `j > j'`, which would require looping through the entire array regardless, we use the `range()` function, running from `j'` to `len(arr)`. In the code, `j'` is obtained with `previous_j`. 

We also know that, if `j - i > k`, then no other value of `j` will satisfy `j = i == k`, thus we break the loop.