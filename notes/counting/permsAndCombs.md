# Permutations and Combinations



# Permutations of k elements out of n
Suppose now we want to pick a sequence $S$ of size $k$ from a set $A$ of size $n$
How many such sequences are there? Since we have $n$ choices for each of the $k$ elements
in the sequence, there are $n^k$ such sequences.

Let's do an example, let's pick 2 elements from $\\{1,2,3\\}$
There are 9 possibilities
```
11 12 13 21 22 23 31 32 33
```

Suppose now we want sequences with no repeated elements!
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
so the answer is 10 * 9 * 8 = 720 as there are 10 choices for the gold medal, then 9 remaining choice
for the silver, and finally 8 for the bronze.

# Combinations
If we don't care about the order, we just want the number of subsets of size $k$ of a set $A$ of $n$ elements, then we will have overcounted each subset by a factor of $k!$ as each permutation of it is the same subset.  Hence the number of such combinations is $P(n,k)/k!$

We denote this as $C(n,k)$ or $\binom{n}{k}$ where

$C(n,k) = \binom{n}{k} = \frac{n!}{(n-k)! k!}$

and we call it "n choose k" as it is the number of ways we can choose k elements out of n,
so "from n choose k"

A fast way to calculate $n$ choose $k$ is to use the following rule.
* start with $n$ and divide by 1
* multiply by $n-1$ and divide by 2
* multiply by $n-3* and divide by 3
* $\ldots$
* multiply by $n-(k-1)$ and divide by $k$

For example. 

$$\dbinom{6}{3} = \frac 61 * \frac 52 * \frac 43 = 30/2\ * \frac 43 = 15 * \frac 43 = 60/3 = 20$$

which is much easier to compute that $6!/3!$.  This works because

$$\dbinom{n}{k} = \dbinom{n}{k-1} * \frac{n-(k-1)}{k}$$

### Applications
How many ways are there of forming two teams, team A and team B, from a group of 4 players?

If we first choose team A, then there are $\binom{4}{2} = 4!/(2! 2!) = 24/4 = 6$ such teams:
```
team A could be one of 12, 13, 14, 23, 24, 34
```

Suppose we want all of the subsets of size 3 from $\\{1,2,3,4,5,6,7,8,9,10\\}$.
This would be 10 choose 3 = $\binom{10}{3} = 10 * 9 * 8/ (3 * 2 * 1) = 120$ and we won't list them!


# The Generalized Multiplication Principle
Suppose we can construct the elements in a set by making a sequence of choices $c_1,c_2,\ldots,c_n$ and
for choice $c_i$ we have $r_i$ options.  Then the total number of elements we can construct, i.e. the size of the set of all such elements is $\prod_\limits{i=1}^n r_i = r_1 * r_2 * \ldots * r_n$

### Applications
How many ways are there of rearranging the numbers $1,2,3,\ldots,n$? 
As we've seen before, these are called the permutations of $n$.  
To apply our general principle, we can create such a sequence by 
* picking the first number (out of n), then
* picking the second number (out of the n-1 remaining elements), then
* picking the 3rd number (out of the n-2 remaining elements), then ...

and repeating until we have only one number, the nth, to pick and there is no choice.

Thus the total number of ways we could generate such a permuation is

$$n * (n-1) * (n-2) * \ldots * 3 * 2 * 1$$

and we call this n factorial and denote it as $n!$

So for n=3 there are 3 * 2 * 1 such permuations:
```
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
```
and for n=4 there are 24 permutations.

**License Plates 2**
Suppose now they change the law and allow license plates with three digits and three letters,
but they can be in any position, e.g.  DDDLLL or DLDLDL or DLLLDD etc.

We can apply the generalized multiplication principle as follows:
* first chose the position of the 3 digits. there are 6 choose 3 such ways
* $\binom 6 3 = 6!/3!^2 = 6 * 5 * 4/ (3 * 2 * 1) = 20$
* next we have $10^3$ choices for the three digits and $26^3$ choices for the three letters
* so the number of license plates is $20 * 10^3 * 26^3$

# Binomials and Multinomials
The n choose k function arises in many places beside in counting. One of the best known is in the binomial formula:

**Theorem** [The Binomial Theorem]

$$
(x + y)^n = \sum_\limits{k=0}^n \dbinom{n}{k} x^ky^{n-k}
$$

We will prove this later when we learn about induction.

Here are some examples of its use:
* $(x+y)^0 = 1$
* $(x+y)^1 = x+y$
*  $(x+y)^2 = x^2 +2xy +y^2$
*  $(x+y)^3 = x^3 +3x^2y +3xy^2 + y^3$
*  $(x+y)^4 = x^4 +4x^4y +6x^2y^2 + 4xy^3 + y^4$

We can think of the n choose k operation as counting the number of subsets of size k in a set of size n, but we can also think of it as the number of ways partitioning a set of size n into two subsets, one of size k and one of size n-k.

The multinomial symbol allows us to count the number of ways of partitioning a set of size n into sequences of sets of size k1, k2, ..., kr. It is defined as follows:

$$
\dbinom{k_1+k+2+\ldots+k_r}{k_1,k_2,\ldots,k_r} = \frac{n!}{k_1! k_2! \ldots k_r!}
$$

and it can be computed more effectively as

$$
\dbinom{n}{k_1} * \dbinom{n-k_1}{k_2} * ... * \dbinom{n-(k_1+\ldots+k_{r-1}}{k_r}
$$

e.g.

$$
\dbinom{10}{2,2,6}=
\dbinom{10}{2} * \dbinom{8}{2} * \dbinom{6}{6} ＝
  \frac{10 * 9}{1 * 2} * \frac{8 * 7 }{1 * 2} * \frac{6}{6} 
  = 45 * 28 * 1 = 1260
$$

which is the number of ways of choosing sets (A,B,C) of sizes 2,2,6 from {1,...,10}
whose usion is {1,2,...,10}.

We can see how this works with the generalized multiplication rule. First choose the subset A which is 10 choose 2. Then there are 8 left, so choose the next subset of 2, which is 8 choose 2, then the third subset is all that is left, that is 6 choose 6.

So we can get the same result as the multinomial formula but by using the generalize multiplication rule and the binomial formula.

