# Sherlock and Array

This problem can be found at [here](https://www.hackerrank.com/challenges/sherlock-and-array/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign).

We attempt to create two variables, left and right, individually with the sum of every variable to the left and the right of the current index. 

We then add the previous index to left, and remove the current index from right, until we get that they are equal. Then, we return YES. Otherwise, we return NO. 