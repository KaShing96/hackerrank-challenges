# Drawing Book 
*This README.md is instantiated by HackerRank Coding Template Version 5.0

This problem can be found [here](https://www.hackerrank.com/challenges/drawing-book/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign).

# Solution
We know that the first page is on the right, thus all odd-numbered pages occur on the right. Similarly, all even-numbered pages occur on the left. We focus on only the left-side pages, i.e. for a book with `n=5` pages, we focus on the following pages: `[0, 2, 4]`. 

Thus, if `n%2==1` or `p%2==1`, we subtract those by 1. 

This makes it easier to obtain `t` turns, which is simply `t=min(p/2, (n-p)/2)`. 