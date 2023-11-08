# Probability Spaces

## Definitions
A **Sample Space** is countable set S (finite or infinite)
* the elements of a sample space $S$ are called **outcomes**
* a subset of S is called an **event**


A **Probability Function** on a sample space $S$ is a total function ${\rm Pr}:S\rightarrow \mathbb{R}$
  from $S$ to the real numbers $\mathbb{R}$ such that 
* ${\rm Pr}[\omega]\ge 0$ for all $\omega \in S$
* $\sum_\limits{\omega in S} {\rm Pr}[\omega] = 1$

A **Probability Space** is a Sample Space with a Probability function.

A Probability Space is **uniform** if ${\rm Pr}[\omega]$ is the same for all $\omega$ in $S$.
This only makes sense for finite sample spaces...

## The Birthday Principle
The MIT text finds a formula in Chapter 16.4 for the probability $b(d,n)$ that a sequence of size n
with elements from a set of size d has no duplicate elements, assuming they are chosen from 
a uniform distribution. The estimate they prove is

$$
b(d,n) = P(d,n)/d^n =\frac{d(d-1)\ldots(d-n+1)}{d * d * \ldots * d}=
\left (\frac{1}{1-\frac 1d}\right ) \left (\frac{1}{1-\frac 2d}\right ) \ldots\left (\frac{1}{1-\frac{n-1}{d}}\right ) 
\lt e^{-\frac 1d} e^{-\frac 2d} \ldots e^{-\frac {n-1}{d}} = e^{-(n(n-1)/2d}
$$

As a rule of thumb if we substitute in $d = n^2/2$ we get $b(d,n)< e{-1} \approx 0.368$ and this is a fairly good estimate

**Birthday Principle** The probability that a sequence of size $n$ taken from a set with $n^2/2$ elements as duplicate elements is about 
$1-1/e = 0.632$.  or equivalently a sequence of size $sqrt{2d}$ taken from a set of size $d$ will have duplicate elements with probability $0.632$.

## Properties of Probability functions.
We define the probability of an event $E$ to the the sum of the probabilities of all outcomes in $E$
* ${\rm Pr}[E] = \sum_\limits{\omega\in E} {\rm Pr}[\omega]$

Because a probability function is a function on subsets of $S$ we can easily prove several very useful identities, e.g.

* ${\rm Pr}[E_1 \cup E_2] = {\rm Pr}[E_1] + {\rm Pr}[E_2]$ if $E_1$ and $E_2$ are disjoint subsets of $S$.
* ${\rm Pr}[E_1 \cup E_2] = {\rm Pr}[E_1] + {\rm Pr}[E_2] - {\rm Pr}[E_1\cap E_2] \le {\rm Pr}[E_1] + {\rm Pr}[E_2]$ for any events $E_1$, $E_2$
* ${\rm Pr}[\overline{E}]  = 1 = {\rm Pr}[E]$ where $\overline{E}$ is the complement of $E$, i.e. $\overline{E} = S-E$
* ${\rm Pr}[E_1 - E_2] = {\rm Pr}[E_1] - {\rm Pr}[E_1\cap E_2]$
* if $A\subseteq B$ then ${\rm Pr}[A] \le {\rm Pr}[B]$
* ${\rm Pr}[\bigcup_\limits{i=1}^\infty E_i] \le  \bigcup_\limits{i=1}^\infty {\rm Pr}[E_i]$
