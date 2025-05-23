# Summary of Counting Methods

We have seen how to count four different kinds of sequences of elements from an ordered set $A$  of size $n$, e.g. $\\{a_1,\ldots,a_n\\}$

| name | definition | size |
| --- | --- | --- |
| sequence of size $k$: $A^k$ | $\\{(a_1,\ldots,a_k:\ a_i \in A\\}$ | $n^k$ |
| permutation of size $k$: $P(A,k)$ | $\\{(a_1,\ldots,a_k:\ a_i \in A, \ a_i \ {\rm distinct}\\}$ | $P(n,k)=\frac{n!}{(n-k)!}$ |
| combination of size $k$: $C(A,k)$ | $\\{(a_1,\ldots,a_k:\ a_i \in A, \ a_1\lt a_2 \lt \ldots \lt a_k\\}$ | $C(n,k)=\binom{n}{k}=\frac{P(n,k)}{k!} = \frac{n!}{k!(n-k)!}$ |
| mulltiset of size $k$: $M(A,k)$ | $\\{(a_1,\ldots,a_k:\ a_i \in A, \ a_1\le a_2 \le \ldots \le a_k\\}$ | $M(n,k)=\binom{n+k-1}{k} =\frac{(n+k-1)!}{(n-1)!k!}$ |

Note that we have identified subsets of size $k$ of a set $A$ with ordered sequences of distinct elements, because these are in 1-1 correspondence with subsets of size $k$. Any such subset can be sorted and results in a unique ordered sequence of distinct elements.


Other tools we used are
## Disjoint Addition Principle
if $A_1,\ldots,A_m$ are disjoint sets, and 

$A =\bigcup_\limits{i=1}^m A_i$

is their union, then

$\vert A \vert = \sum_\limits{i=1}^m \vert A_i \vert$

## Subtraction Principle
if $A$ and $B$ are sets, then 

$\vert A - B \vert =\vert A\vert - \vert A\cap B\vert$

## Generalized Multiplication Principle
If the elements of a set $A$ can be generated by making a series of choices $c_1,\ldots,c_r$ and each choice has $n_i$ options,
then 

$\vert A\vert = n_1 * \ldots * n_r$

## Bijection principle
If $A$ and $B$ are sets and there is a bijection from $A$ to $B$, then 
$\vert A \vert = \vert B \vert$

## Surjection principle = Pigeonhole Principle
If $A$ and $B$ are sets and there is a surjection from $A$ onto $B$, then 
$\vert A \vert \ge \vert B \vert$

## Injection principle
If $A$ and $B$ are sets and there is a injection from $A$ onto $B$, then 
$\vert A \vert \le \vert B \vert$

## Principle of Inclusion and Exclusion
If $A$, $B$, and $C$ are sets then
* $\vert A \cup B \vert = \vert A \vert + \vert B \vert - \vert A\cap B \vert$
* $\vert A \cup B \cup C \vert = \vert A \vert + \vert B \vert+ \vert C \vert  - \vert A\cap B \vert - \vert A\cap C \vert - \vert B\cap C \vert + \vert A\cap B \cap C\vert$
* and for larger interesections you alternately add and subtract the intersections of increasing numbers of sets

  
