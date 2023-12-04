# Analysis of Algorithms

In this section we give an overview of techniques for analyzing the performance of algorithms.

## Big-Oh, Big-Omega, and Big-Theta notation
The first step is to define some families of functions that we use to classify algorithms by their
performance...  Rather than find the exact time a program will take we want a rough classification
that allows us to compare different programs and we're especially interested on large data inputs
and not too interested on the speed of the particular computer... This leads naturally to these three
families of sets...

We will consider sequences $s(0), s(1_, ..., s(n), \ldots$ where $s(i)$ is the "time" that the program
takes on inputs of size $i$.  In practice, there may be many inputs of size $i$ so we would have to 
specify if we are talking about the worst case time (i.e. the one with the longest runtime), or the
best case, or the average case. Typically we consider the worst case unless otherwise specified.

We will then classify such sequences by their growth rates...

### Asymptotic Notation
Let $f$ and $g$ be functions from $\mathbb{N}\rightarrow \mathbb{R}^+$ where $\mathbb{R}^+$ is the set of non-negative real numbers.

* $O(f) = \\{g:\mathbb{N}\rightarrow \mathbb{R} \vert \exists c \exists k \ \forall n\gt k \ g(n)\le f(n)$
* $\Omega(f) = \\{g:\mathbb{N}\rightarrow \mathbb{R} \vert \exists c \exists k \ \forall n\gt k \ g(n)\ge f(n)$
* $\Theta(f) = O(f) \cap \Omega(f)$

We call these sets big-Oh of f, little-Oh of f, big-Omega of f, little-Omega of f, big-Theta of f.

We sometimes also use the following two sets of functions where 
$o(f) \subset O(f)$ and $\omega(f)\subset \Omega(f)$.
* $o(f) = \\{g:\mathbb{N}\rightarrow \mathbb{R} \vert \forall c \exists k \ \forall n\gt k \ g(n)\le f(n)$
* $\omega(f) = \\{g:\mathbb{N}\rightarrow \mathbb{R} \vert \forall c \exists k \ \forall n\gt k \ g(n)\ge f(n)$
For these two the function $f$ is strictly bigger than the best possible upper bound...

We call these sets little-Oh of f and little-Omega of f.

Intuitively, big-Oh is used to give a simple upper bound on functions of particular types. The most common
asymptotic classes in Computer Science are the following
* constant upper bounds $O(1)$
* functions that get close to zero as n gets large $o(1)$
* logarithmic upper bounds $O(\log(n))$
* square root upper bounds $O(\sqrt(n))$
* sub-linear upper bounds $o(n)$  grows slower than any linear function
* linear upper bounds $O(n)$
* log-linear upper bounds $O(n \log(n))$
* quadratic upper bounds $O(n^2)$
* cubic upper bounds $O(n^3)$
* exponential upper bounds $O(2^n)$

If we are interested in lower bounds, then we use the big-Omega and little-omega notation.
If we are interested in more precise bounds, both lower and upper, we use big-Theta.

## Intuition
Looking closely at the formulas we see there are two constants $c$ and $k$ used in the definition.
The $c$ is there because we don't in general care about the speed of the actual computer running the program.
A slower computer will have a larger value of $c$. For example, consider the problem of examining a list of $n$ numbers to see if $n$ is odd or even.  A formula for the time it takes humans to do this (possibly working in shifts through the nights) would be two per second. So the time in seconds would be 
* $h(n) = 0.5*n$ seconds
whereas if we were to use a computer, it could scan through billions of numbers per second so it would be
* $c(n) = 10^{-9} n$ seconds
Likewise if were to look through a sorted list to see if an element is in the list (say a list stored in a
file on a computer), we could do this with a binary search algorithm (keeping track of the lowest and highest position it could be in, then looking in the middle and adjusting our bounds). This would take $\log_2(n)$ steps
and each step would take a few seconds, but for a computer each step would billionths of a second. Still the algorithm is the same.

The constant $k$ is used to focus our attention only on efficiency for large values of $n$. It is often the case that the best algorithm for large $n$ is not the one you want to use for small values. For example, if you need to sort three numbers, it is better to have a few if-statements than to use the merge-sort or quick-sort algorithms.

## Practice
We say that $g$ is big-Oh of $f$ if $g \in O(f)$.

Let's show that $g(n) = 2n^2 + 3n+4$ is big-O of $n^2$ 
that is lets show $g\in O(n^2)$

So we want to find $c$ and $k$ such that
* $2n^2 + 3n+4 \le c n^2$ whenever $n>k$

Let's factor out an $n^2$ from the formula to get
* $n^2 (1 + 3/n + 4/n^2) \le c n^2$ when $n>k$

If we pick k=10, then $3/n<3/10$ and $4/n^2 < 4/100$ so
* $n^2 (1 + 3/n + 4/n^2) \le n^2 (1+0.3 + 0.04) = 1.34n^2$ if $n>10$

and we can let $c=1.34$ and $k=10$, which shows that $2n^2 + 3n+4 \in O(n^2)$

The same approach works for almost all such calculations. We find the "fastest growing term"
and factor it out of the rest of the terms, then all of those should get small for larger $n$.

We can use the same approach to show that $g \in \Omega(f)$ by looking for lower bounds, e.g.
* $2n^2 + 3n+4 \ge 2 n^2$ whenever $n>1$ because $3/n+4/n^2\ge 0$ if $n\ge 1$
* so $2n^2 + 3n+4 \ge 2 n^2 \in \Omega(n^2)$
* so $2n^2 + 3n+4 \ge 2 n^2 \in \Theta(n^2)$

## Divide and Conquer algorithms and Recursion equations
We'll look at some interesting algorithms and find simple formulas for their asymptotic growth.
* summing a list of numbers
* finding the smallest number is a list
* testing if a number is in a sorted list of numbers
* sorting a list of numbers
* multiplying two $n$-bit numbers
* multiply two nxn matrices





