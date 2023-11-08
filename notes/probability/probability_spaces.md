# Probability Spaces

## Definitions
A **Sample Space** is countable set S (finite or infinite)
* the elements of a sample space $S$ are called **outcomes**
* a subset of S is called an **event**


A **Probability Function** on a sample space $S$ is a total function ${\rm Pr}:S\rightarrow \mathbb{R}$
  from $S$ to the real numbers $\mathbb{R}$ such that 
* ${\rm Pr}[\omega]\ge 0$ for all $\omega \in S$
* $\sum_\limits{\omega in S} {\rm Pr}[\omega] = 1$

We define the probability of an event $E$ to the the sum of the probabilities of all outcomes in $E$
* ${\rm Pr}[E] = \sum_\limits{\omega\in E} {\rm Pr}[\omega]$

Because the probability function is a function on subsets of $S$ we can easily prove several very useful identities, e.g.

* $
