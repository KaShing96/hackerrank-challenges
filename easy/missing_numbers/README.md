# Missing Numbers
Problem found [here](https://www.hackerrank.com/challenges/missing-numbers/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign).

We use a dictionary. The key is the number and the value is an array of length 2, where index 0 gives us the occurrences in the first array and index 1 gives us the occurrences in the second array. 

We then filter out those where the first and second indexes are different and return those numbers. 