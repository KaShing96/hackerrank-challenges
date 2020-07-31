# Game of Stones
*This README.md is instantiated by HackerRank Coding Template Version 4.0

This problem can be found [here](https://www.hackerrank.com/challenges/game-of-stones-1/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign).

## Solution
This is a logic problem I've come across before. 

We assume the following numbers of n, in which we look at what moves P1 and P2 can do, with P1 always going first. 
 - 1: P1 loses
 - 2: 2, P2 loses
 - 3: 3, P2 loses
 - 4: 3, P2 loses
 - 5: 5, P2 loses
 - 6: 5, P2 loses
 - 7: 5, 2, P1 loses
    3 => 4: 3, P1 loses
    2 => 5: 5, P1 loses => P1 loses
 - 8: 5, 3, P1 loses
    3 => 5: 5, P1 loses
    2 => 6: 5, P1 loses => P1 loses
 - 9: 5, 3, P1 loses
    3 => 6: 5, P1 loses
    2 => 7: 5, 2, P2 loses
        3 => 4: 3, P2 loses
        2 => 5: 5, P2 loses => P2 loses

Thus, we see a pattern. The one who moves first when the number is 7, as evidenced in 7 and 9, will lose. The one who moves first when the number is 8, will also lose. We continue the pattern. From 9, it is also clear that the one who moves second will lose.

 - 10: 5, 5, P1 loses
    3 => 7: P2 loses => P2 loses
 - 11: 5, 5, P1 loses
    3 => 8: P2 loses => P2 loses
 - 12: 5 => 7, P2 loses

We want to avoid going to infinity. Going from the previous logic where those who land on 7, 8, and 9 will lose, we note that P1 can reduce 9, 10, and 12 to 7. P1 can also reduce 10, 11, and 13 to 8. Thus, P1 will win in these cases. 

 - 13: P2 loses

In the case of 14, P1 must avoid reducing it to 13, 12, 11, 10, and 9, which is impossible. Thus:

 - 14: P1 loses

In the case of 15, P1 must avoid reducing it to 13, 12, 11, and 10. P1 must try to hit 14, which is impossible. Thus, P1 loses.

 - 15: P1 loses

Thus, here, we can extract a pattern. 1 is a dangerous tile. 2, 3, 4, 5 and 6 are safe tiles, because the case of 4 is taken care of by 3, i.e. whoever lands on 4 first can use 3 to win, while those on 6 can use 5 to win. Thus, we know that the next 5 tiles from a given dangerous tile are safe. 

To check this theory, we know 7 is a dangerous tile. We also know 8 is a dangerous tile. 9 is safe, as it can be reduced to 7. From 7, 8, we identify that 9, 10, 11, 12, 13 are safe tiles. We also know 14 and 15 are dangerous tiles. Thus, 16, 17, 18, 19, and 20 are safe tiles, and so on. This leaves 21 and 22 dangerous tiles. 

Thus, we come to the conclusion that 1, any multiples of 7, and any multiples of 7 added by 1, are dangerous tiles. This can be further reduced to k\*7 or k\*7 + 1, where k >= 0. 