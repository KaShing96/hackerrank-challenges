# Anagram
*This README.md is instantiated by HackerRank Coding Template Version 4.0

This problem can be found [here](https://www.hackerrank.com/challenges/anagram/problem?utm_campaign=challenge-recommendation).

# Solution
We split the string based on its length into two substrings, `s1` and `s2`. We then compare if these two strings are different, character by character. 

We then count the number of occurrences of each letter in each substring. The difference in these occurrences is the answer.