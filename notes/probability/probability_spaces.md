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
