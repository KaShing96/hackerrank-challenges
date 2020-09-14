# Electronics Shop
*This README.md is instantiated by HackerRank Coding Template Version 5.0

This problem can be found [here](https://www.hackerrank.com/challenges/electronics-shop/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign).

# Solution
We first sort both `keyboards` and `drives` such that they are in descending order. Then we loop past `keyboards` and `drives`, skipping to the next keyboard if the value exceeds `b`. 

We will have a selection that is initialised with a value of `None` that keeps track of the most expensive keyboard and drives pair.