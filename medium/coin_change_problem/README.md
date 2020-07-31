# Coin Change
Started on 21st July 2020.

21st July 2020: Solution 1 failed. Attempt alternate logic.

22nd July 2020: The increment() function needs to be altered so that we fill up the largest possible coins. Currently, it may not be performing this way, as evidenced by verification 01.txt. 

23rd July 2020: Solution 2 failed. Alternate logic worked out as Solution 3. 

24th July: Solution 3 and Modified Solution 3 failed. 

25th July: Started on Solution 4, based off an online answer.

26th July: Solution 4 succeeded.

## Table of Contents
 - [Solution 1](#sol1)
 - [Solution 2](#sol2)
 - [Solution 3](#sol3)
 - [Solution 3 (Modified)](#sol3mod)
 - [Solution 4](#sol4)

<a name="sol1">

## Solution 1
Given a total N and an array of integers C, we want to identify the number of ways we can obtain N from the elements in C. Each element in C can be either included or excluded in obtaining N. 

### Terminology
We have a number N, which is the number we are attempting to obtain.

We have an array of numbers, C, each of which can be used to obtain N. We label the elements of C as C1, C2, C3... CC.

The resulting solution set comprising the elements of C that give N will be termed S. 

### Insight 1 - Divisibility of N
We know that, if S is a set of only one unique number, then this suggests that N is divisible by that number. For example, if N = 6 and S = {2, 2, 2}, the insight here is that 6 is divisible by 2 with no remainder. 

Thus, we know that <b>if N is purely divisible by an element in C, we have a set S containing only that element</b>.

### Insight 2 - Multiplicative Relations Within C
We assume that C = [C1, C2, C3], and that N is purely divisible by C3. We also assume C1 < C2 < C3. 

We then want to investeigate the relationship between C1, C2, and C3. We note that, if C3 is a multiple of C2, it can give us two distinct scenarios: 
1. S = [C2, C2, C2...], where S is a set of only C2. This is captured by <b>Insight 1</b> where N is divisible by C2. 
1. S = [C2, C2, C3...], where S is now a set of only C2 and C3. This is a new insight, suggesting that if C3 is a multiple of C2, the solution set can be uniquely defined by only C2 and C3.

Assuming this is the case, we now have S1 = {C3}, S2 = {C2} and S3 = {C2, C3}. We assume further that C2 is a multiple of C1. Thus, <i>for every set with C2 in it</i>, we can generate a set containing the original unique elements of C, and C1. In this case, S2 and S3 contain C2. Thus, we can generate S4 = {C2, C1} and S5 = {C3, C2, C1}. 

Thus, the rule of thumb here is that, working from the largest element in C, <b>if the next smallest element in C is a factor of any of the previous larger elements in C, then every solution set Ss containing the larger element can generate a new solution set containing the smaller element.</b>

We also keep in mind that, to apply Insight 2, the **occurrences** are important. If S1 = [C3] and C3 = kC2, then S2 = {C2}. However, if S1 = [C3, C3], then we have S2 = {C3, C2} and S3 = {C2}. To simplify this, we can obtain a dictionary where the key is the element in C, and the value is its number of occurrences. In the above scenario, if S1 = {C3: 1}, then we have S2 = {C2: k}. Meanwhile, if S1 = {C3: 2}, we have S2 = {C3: 2 - 1, C2: 1 * k}. We also note that, if S1 = {C3: 3}, then S2 = {C3: 2, C2: k} and S3 = {C3: 1, C2: 2k} give S2 and S3 as two different possible solutions.

### Insight 3 - Additive Relations Within C
We investigate the case for when the elements in C are additively related. If C = [C1, C2, C3] and C3 = C1 + C2, then for a given set S1 = {C3: 1}, we can obtain S2 = {C2: 1, C1: 1}. This carries similarly to the previous case. If S1 = {C3: 3}, then we can have S2 = {C3: 2, C2: 1, C1: 1} and S3 = {C3: 1, C2: 2, C1: 2}. 

### Insight 4 - A generalisation of Insights 2 and 3
Carrying from Insights 2 and 3, we assume we have C = [C1, C2, C3, ... CC]. We also assume that for some element of C, Cc1, it is related to other elements of C, Cc2, Cc3, ... CcC, by the following formula: Cc1 = k2Cc2 + k3Cc3 + ... + kC CcC, where k2, k3, ... kC are constants.

Then, we loop through all existing sets containing Cc1 >= 1 and apply the above transformation. We repeat this for all values of Cc1, going from CC to C(C-1) to C(C-2), all the way down to C3, C2, C1. 

### Potential Problem
For the above, we note that Insight 1 gives us a method to generate sets containing only one unique element of C, and that Insights 2, 3 and 4 require there to be existing sets from which Insight 4 can be applied. 

Thus, we first need to generate the possible sets from which Insight 4 can be applied. This returns us to the general problem of how many sets we need, as an alternative way of generating these sets might invalidate Insight 4. 

A simple way to do so is to sort C in ascending order, and then to subtract the largest value from N, going down the values until the remaining value is 0. We then have a solution set from which to begin. 

<a name="sol2">

## Solution 2
We attempt a more 'brute-force' method by obtaining subsets of C where each subset, C1, C2, etc. contains varying combinations of each element in C. 

### Obtaining the largest set
The Largest Set is the solution set containing the largest coin. 

We can obtain the Largest Set with a function inspired by that in Solution 1, when attempting to obtain the initial solution set. 

From this largest set, we can slowly decrement the largest value by 1, and attempt to fill up this largest value with smaller coins, incrementing the solution set with these smaller coins. We then repeat until we get to the lowest value in the solution set. 

This allows us to perform dynamic programming at what is hopefully a much simpler level. 

<a name="sol3">

## Solution 3
We attempt to use dynamic programming to a greater extent here. 

We assume a given case of n=4 and c={1, 2, 3}. Here, we have top-level solutions of {3:1, 1:1}, {2:2} and {1:4}. 

We know that {2:2} can be expanded to {2:1, 1:2}. 

### Relations
In this solution, we consider a concept from Solution 1: *relations*. More specififcally, we consider *additive relations*. 

We know that, from 1, 2, and 3, we have 3 = 2 + 1 and 2 = 1 + 1. We consider each of these relations individually: 
1. 2 = 1 + 1
2 can be broken down into **1** unique coin. Thus, for every coin 2, we have +1 cases. This unique coin cannot be broken down further, i.e. it gives us +0 unique cases. Thus, every 2 gives us +1 + (+0) = +1 case. 
1. 3 = 2 + 1
3 can be broken down into **2** unique coins Thus, for every 3, we have +2 cases. However, we note that 3 can be broken down into 2, which gives us +1 unique cases, and 1, which gives us +0 unique cases. Thus, 3 gives us +2 + (+1 + +0) = +2 cases. 

Then, we need to apply this concept to our top level solutions. 

For a given solution set, we identify MAX, the maximum coin in the set, and REST, the rest of the coins. 

The additional number of cases from a given top level solution is thus given by: 
(MAX - 1) * (unique cases from MAX) + (REST) * (unique cases from REST), where the second term in the entire equation is repeated for each coin that is not MAX. To illustrate, take the above sets: 
1. {3:1, 1:1}
(1-1)\*(+2) + (1)\*(+0) = +0
1. {2:2}
(2-1)\*(+1) = +1
1. {1:4}
(4-1)\*(+0) = +0

We have three top level cases. Thus, the total answer is 3 + 1 = 4. 

### The relation equation
Here, we arrange the coins in ascending order: 1, 2, 3.

We also arrange the relations in ascending order:
1. 2 = 1 + 1
1. 3 = 2 + 1

Then, we go up the ordered coins: 
1. 1 cannot be broken down into anything as it is not in the relations list. Thus, 1 => +0. 
2. 2 can be broken down into 1 and 1. Each 1 cannot be broken down into anything else. However, if we simply multiply each unique constituent it can be broken down into, by the number of cases that constituent can be broken down into, we would get +1\*+0 = +0. An alternative we can explore is the function: max(+1, +1\*(+0)) = +1. Here, the first argument does not include the cases. The second argument does. We note that here, there is only one unique case, 1, thus we only have an additional 1 case per unique case, +0. 
3. 3 can be broken down into 2 and 1. Thus, there are 2 extra unique cases. In these unique cases, 2 can be broken up into 1 additional unique case. Thus, we have: max(+2, +2 * (+1+0)) = +2. 

Thus, we stick with max(a, b), where a is the number of immediately unique cases, and b is the number of unique cases multiplied by those cases' unique cases. 

### More complicated example
For a more complicated example, let's take the case of n=6, c={1, 2, 3, 4}.

We have the following relations. For each of the relations, we identify the number of *unique* coins (u) it can be decomposed into, and the additional cases (a) each of those unique coins bring. 
1. 2 = 1 + 1
max(+1u, +1u*(+0a)) = +1
1. 3 = 2 + 1
max(+2u, (+2u)*(+1a+0a)) = +2
1. 4 = 3 + 1
max(+2u, (+2u)*(+2a+0a)) = +4
1. 4 = 2 + 2
max(+1u, (+1u)*(+1a)) = +1

Adding the relations all up together, we have:
1. 1 => +0
1. 2 => +1
1. 3 => +2
1. 4 => +5

We identifty the top level solutions: 
1. {4:1, 2:1}
1. {3:2}
1. {2:3}
1. {1:6}

Then, we implement the MAX-REST functions.
1. {4:1, 2:1}
(1-1)\*(+5) + (1)\*(+1) = +1
1. {3:2}
(2-1)\*(+2) = +2
1. {2:3}
(3-1)\*(+1) = +2
1. {1:6}
(6-1)\*(+0) = +0

We have four initial answers. Thus, we now have: 4 + 1 + 2 + 2 + 0 = 9

To check our answer, we have the following combinations: 
1. {4:1, 2:1}
1. {4:1, 1:2}
1. {3:2}
1. {3:1, 2:1, 1:1}
1. {3:1, 1:3}
1. {2:3}
1. {2:2, 1:2}
1. {2:1, 1:4}
1. {1:6}

<a name="sol3mod">

## Modified Solution 3
We encounter an issue where there are two coins that cannot be decomposed. 

Upon closer inspection, the *Relations* in Solution 3 also has problems, and is the point of propagation of error. 

### Problem with Relations
We consider the case of c = [1, 2, 3, 4]
1. 2 = 1 + 1
{2:1} => {1:2} => +1
1. 3 = 2 + 1
{3:1} => {2:1, 1:1}, {1: 3} => +2
1. 4 = 3 + 1
{4:1} => {3:1, 1:1}, {2:1, 1:3}, {1:4} => +3
1. 4 = 2 + 2
{4:1} => {2:2}, {2:1, 1:2}, {1:4} => +3
However, we note that, for 4, there are actually only **5** unique cases: {3:1, 1:1}, {2:1, 1:3}, {1:4}, {2:2}, and {2:1, 1:2}. Thus, we can reduce 4 => +5. 

We understand here that the previous relations equation does not properly represent the number of cases available. 

### Modification to Relations
We consider the similar case of c = [1, 2, 3, 4]
1. 2 = 1 + 1
We have 1 extra case. We know that 1 cannot be decomposed. Thus, 2 => +1. 
1. 3 = 2 + 1
We have 1 extra case. We know 2 can be decomposed as per 2 => +1, thus, we add +1. We know that 1 cannot be decomposed. Thus, 3 => +1 +1 +0 = +2. 
1. 4 = 3 + 1
We have 1 extra case. We know that 3 can be decomposed and 1 cannot be decomposed. Thus, we have 4 => +1 +2 +0 => +3.
1. 4 = 2 + 2
We have 1 extra case. We know that 2 can be decomposed as per 2 => +1. Thus, we have 4 => +1 +1 => +2. 

Thus, it is simply a case of checking whether a relations exist, in which case the relations_score += 1. Then, for each unique decomposition, we check if that in itself has a score, which we add to relations_score. The final score is the score for the given relation. 

<a name="sol4">

## Solution 4 
Solution 4 is obtained from the following page on the [Coin Change Problem](https://www.ideserve.co.in/learn/coin-change-problem-number-of-ways-to-make-change).

### Problem Summary
We work with n=4, c=[1, 2, 3]. 

We identify the largest coin in c, which is 3. This problem is thus a question of identifying the number of solutions for 3 = 0 and 3 = 1. 

For the case of 3 = 0, it is then a case of identifying the number of solutions for 2 = 0, 1, 2. 

For 2 = 0, it is then a case of identifying the number of solutions for 1. As the solution set is of size 1 and it is divisible by 4, we return 1, because there is only 1 way we can arrange a combination of 1 to be divisible by 4. 

We then repeat this for 2 = 1, 2, where we identify the case of 4-1\*2 being divided by 1, and then 4-2\*2=0, wherein we do not pursue the matter further. 

We then repeat this for 3 = 1. 

### Optimisation
We store the solution for the target number and the given number of sets within a dictionary, where the key is n, and the value is a dictionary, where the key to this dictionary is str(c) and the value is the number of cases.