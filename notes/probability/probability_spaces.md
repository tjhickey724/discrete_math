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

As a rule of thumb if we substitute in $d = n^2/2$ we get $b(d,n)< e{-1} \approx 0.368$ and this is a fairly good estimate.
Note that if $d=n^2/2$ then $n = \sqrt{2d}$

**Birthday Principle** The probability that a sequence of size $\sqrt{2d}$ taken from a set of size $d$ will have duplicate elements is about $1-\frac 1e \approx 0.632$.

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

## Conditional Probability
We use the notation ${\rm Pr}[E \vert F]$ for the probability that event $E$ occurs, assuming that event $F$ also occurs. It is defined set-theoretically as follows:

$$
{\rm Pr}[E \vert F] = \frac{{\rm Pr}[E \cap F]}{ {\rm Pr}[F]}
$$

**Lemma** 
* ${\rm Pr}[E \cap F]   = {\rm Pr}[F] \ {\rm Pr}[E \vert F]$
* ${\rm Pr}[E_1 \cap E_\cap E3]   = {\rm Pr}[E_1] \ {\rm Pr}[E_2 \vert E_1]  \ {\rm Pr}[E_3 \vert E_1 \cap E_2] $

**Proof:**  For the first, multiply both sides of the defintion by ${\rm Pr}[F]$.
For the second replace the conditional probabilities with their defintions and everything cancels out. **QED**

## Example 1
Calculate the conditional probability using the example from the MIT text.

Two teams, A and B, are playing a 3 game tournament and the first team to win 2 games wins the tournament.

Team A also has the following property. If the win a game, then they are enthused and the probability they win their next game is 2/3.
If they lose, then they are demoralized and the probability they win the next game is 1/3.  Find the probability that they win the tournament
assuming they win the first game. Draw the tree, identify the events of interest, calculate the probabilities of each outcome (assume that team A wins the first game with probability 1/2), then calculate the probabilities of the events and use the definition of conditional probability in terms
of usual probability to find the answer.

## Bayes Rule
Baye's rule allows one to calculate the "inverse" of conditional probabilities.
$$
{\rm Pr}[B \vert A]   = \frac{{\rm Pr}[B] \ {\rm Pr}[A\vert B]}{ {\rm Pr}[A] }
$$

This follow easily from the fact that ${\rm Pr}[A \cap B]   = {\rm Pr}[B] \ {\rm Pr}[A \vert B]$
We can use it to calculate the "probability" that the team won their first game, if we know they won the tournament....
but this does raise philosophical issues!

## Independent Events
An event A is independent of an event B if ${\rm Pr}[B]=0$ or if ${\rm Pr}[B]\not = 0$ and
* ${\rm Pr}[A \vert B] = {\rm Pr}[A]$

Two events are independent of each other if
* ${\rm Pr}[A \cap B] = {\rm Pr}[A]\  {\rm Pr}[B]$
