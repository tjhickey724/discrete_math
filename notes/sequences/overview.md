# Overview of Sequences

In this section, we define a sequence $s$ will always be an infinite sequence of integers (or sometimes reals or complex numbers)

$s = s_0,s_1,s_2,\ldots,s_n,\ldots$

These are important in Computer Science because we often measure the efficiency of a program by how it performs on inputs of length $n$.
If we let $s_n$ be that measure, for example an upper bound on the number of steps it takes or on the amount of memory it requires, then if we can calculate $s_n$ as a function of $n$ it will allows us to determine how efficient the program is.

We will look at 2 different kinds of sequences
* [polynomial sequences](polynomial_sequences.md) where $s_n=p(n)$ for some polynomial $p(x) = a_0 +a_1 x + a_2 x^2 + \dots a_k x^k$
* [exponential sequences](exponential_sequences.md) where $s_n =a_0 b_0^n + a_1 b_1^n + \ldots a_k b_k^n$

We will learn how to recognize when a sequence is one of these two types, and how to find the coefficients $a_i$ (and mabybe $b_i$)
when it is.

