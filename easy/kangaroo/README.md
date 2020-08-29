# Kangaroo
*This README.md is instantiated by HackerRank Coding Template Version 4.0

This problem can be found [here](https://www.hackerrank.com/challenges/kangaroo/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign).

# Solution
This challenge reads more like a math problem than a coding problem. 

We let `y1` and `y2` be the positions of the kangaroos after time `t`. Thus: 
```
y1 = x1 + v1 * t
y2 = x2 + v2 * t
```
Equating them together, we have: 
```
x1 + v1 * t = x2 + v2 * t
x1 - x2 = t * (v2 - v1)
      t = (x1 - x2)/(v2 - v1)
```
Now, we know that time `t` is discretised to represent each jump. Thus, `t` must be a positive integer, that is, `t >= 1` and `t == int(t)` or `(x1 - x2) % (v2 - v1) == 0`. Otherwise, they will never meet. 

We also account for the case where `v2 - v1 == 0`, which leads us to a division by zero. In this case, the only way the kangaroos land on the same spot is if `x2 == x1`, that is, they travel at the same rate and they start at the same position. 

