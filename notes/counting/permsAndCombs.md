# Permutations and Combinations

# The Generalized Multiplication Principle
Suppose we can construct the elements in a set by making a sequence of choices $c_1,c_2,\ldots,c_n$ and
for choice $c_i$ we have $r_i$ options.  Then the total number of elements we can construct, i.e. the size of the set of all such elements is $\prod_\limits{i=1}^n r_i = r_1 * r_2 * \ldots * r_n$

### Applications
How many ways are there of rearranging the numbers $1,2,3,\ldots,n$? These are called the permutations of $n$.  To apply our general principle, we can create such a sequence by 
* picking the first number (out of n), then
* picking the second number (out of the n-1 remaining elements), then
* picking the 3rd number (out of the n-2 remaining elements), then ...

and repeating until we have only one number, the nth, to pick and there is no choice.

Thus the total number of ways we could generate such a permuation is

$n * (n-1) * (n-2) * \ldots * 3 * 2 * 1$

and we call this n factorial and denote it as $n!$

So for n=3 there are 3*2*1 such permuations:
```
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
```
and for n=4 there are 24 permutations.

# Permutations of k elements out of n
Suppose now we want to pick a sequence $S$ of size $k$ from a set $A$ of size $n$
How many such sequences are there? Since we have $n$ choices for each of the $k$ elements
in the sequence, there are $n^k$ such sequences.

Let's do an example, let's pick 2 elements from $\\{1,2,3\\}$
There are 9 possibilities
```
11 12 13 21 22 23 31 32 33
```

Suppose now we want sequence with no repeated elements!
There are 
* $n$ choices for the position 1,
* $n-1$ for position 2
* $n-2$ for position 3
* $\ldots$
* $n-(k-1)$ for position $k$

So the total number of such sequences is 

$n * (n-1) * (n-2) * \ldots * (n-(k-1))$

which is equal to $n!/(n-k)!$

We usually use the notation $P(n,k) = n!/(n-k)!$
to denote the number of permutations of $k$ elements out of $n$.

### Applications
Suppose we have 10 people competing for the All Around Championship
and we will have 3 medals: gold, silver, bronze. How many possible outcomes
are there?

We are looking for the number of sequences of length 3 from a set of 10 elements,
so the answer is 10*9*8=720 as there are 10 choices for the gold medal, then 9 remaining choice
for the silver, and finally 8 for the bronze.

# Combinations
If we don't care about the order, we just want the number of subsets of size $k$ of a set $A$ of $n$ elements, then we will have overcounted each subset by a factor of $k!$ as each permutation of it is the same subset.  Hence the number of such combinations is $P(n,k)/k!$

We denote this as $C(n,k)$ or $\binom{n}{k}$ where

$C(n,k) = \binom{n}{k} = \frac{n!}{(n-k)! k!}$

and we call it "n choose k" as it is the number of ways we can choose k elements out of n,
so "from n choose k"

### Applications
How many ways are there of forming two teams, team A and team B, from a group of 4 players?

If we first choose team A, then there are $\binom{4}{2} = 4!/(2! 2!) = 24/4 = 6$ such teams:
```
team A could be one of 12, 13, 14, 23, 24, 34
```




Suppose we want all of the subsets of size 3 from $\\{1,2,3,4,5,6,7,8,9,10\\}$.
There are 10 choices for the first 
