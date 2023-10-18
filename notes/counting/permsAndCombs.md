# Permutations and Combinations

# The Generalized Multiplication Principle
Suppose we can construct the elements in a set by making a sequence of choices $c_1,c_2,\ldots,c_n$ and
for choice $c_i$ we have $r_i$ options.  Then the total number of elements we can construct, i.e. the size of the set of all such elements is $\prod_limit{i=1}^n r_i = r_1 * r_2 * \ldots * r_n$

### Applications
How many ways are there of rearranging the numbers $1,2,3,\ldots,n$? These are called the permutations of $n$.  To apply our general principle, we can create such a sequence by 
* picking the first number (out of n), then
* picking the second number (out of the n-1 remaining elements), then
* picking the 3rd number (out of the n-2) remaining elements

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
