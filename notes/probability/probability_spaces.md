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
* ${\rm Pr}[\overline{E}]  = 1 - {\rm Pr}[E]$ where $\overline{E}$ is the complement of $E$, i.e. $\overline{E} = S-E$
* ${\rm Pr}[E_1 - E_2] = {\rm Pr}[E_1] - {\rm Pr}[E_1\cap E_2]$
* if $A\subseteq B$ then ${\rm Pr}[A] \le {\rm Pr}[B]$
* ${\rm Pr}[\bigcup_\limits{i=1}^\infty E_i] \le  \sum_\limits{i=1}^\infty {\rm Pr}[E_i]$

We sometimes use logic operations instead of set operations on events since 
* the event $E_1\cup E_2$ can be viewed as $E_1 \vee E_2$ occurring, and
* the event $E_1\cap E_2$ can be viewed as $E_1 \wedge E_2$ occurring, and
* the event $\overline{E_1}$ can be viewed as the outcomes where $\neg E_1$


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

## Exercise 1
Calculate the conditional probability using the example from the MIT text.

Two teams, A and B, are playing a 3 game tournament and the first team to win 2 games wins the tournament.

Team A also has the following property. If the win a game, then they are enthused and the probability they win their next game is 2/3.
If they lose, then they are demoralized and the probability they win the next game is 1/3.  Find the probability that they win the tournament
assuming they win the first game. Draw the tree, identify the events of interest, calculate the probabilities of each outcome (assume that team A wins the first game with probability 1/2), then calculate the probabilities of the events and use the definition of conditional probability in terms
of usual probability to find the answer.

## Bayes Rule
Baye's rule allows one to calculate the "inverse" of conditional probabilities.

$$
{\rm Pr}[B \vert A]   = \frac{{\rm Pr}[B] \ {\rm Pr}[A\vert B]}{ {\rm Pr}[A]}
$$

This follow easily from the fact that ${\rm Pr}[A \cap B]   = {\rm Pr}[B] \ {\rm Pr}[A \vert B]$

## Exercise 2
We can use Bayes rule to calculate the "probability" that the team won their first game, if we know they won the tournament....
This does raise philosophical issues!

## Independent Events
An event A is independent of an event B if ${\rm Pr}[B]=0$ or if ${\rm Pr}[B]\not = 0$ and
* ${\rm Pr}[A \vert B] = {\rm Pr}[A]$

Unrolling the defintion of conditional probability
* ${\rm Pr}[A \vert B]  =  {\rm Pr}[A \cap B] / {\rm Pr}[B]$

We see that A is indepent of B if an only if 
* ${\rm Pr}[A \cap B] = {\rm Pr}[A]\  {\rm Pr}[B]$

In other words, the probability that A and B both occur is the product of their probabilities of occuring individually.
If we assume that two events are independent, it makes them much easier to work with!


## Random Variables

A **random variable** X on a probability space is a total function whose domain is the sample space.

Since we are assuming the sample space $S$ is either finite or countable infinite, the range of a random
variable is either finite or countably infinite, and the outcomes where $X$ takes a given value can be viewed
as events written as
* ${\rm Pr}(X=k)$

Two random variables $R_1$ and $R_2$ are said to be independent provided these events are all independent, that is

$R_1$ and $R_2$ are said to be **independent random variables** by definition if forall $j$ and $k$ we have
* ${\rm Pr}[R_1=j]$ and ${\rm Pr}[R_2=k]$ are independent events

$$
{\rm Pr}[(R_1=j) \wedge (R_2=k)] = {\rm Pr}[R_1=j] * {\rm Pr}[R_2=k] 
$$

Making the assumption that two random variables are independent makes it easier to reason about them
because knowing the value of one variable doesn't impact the value of the other, that is

* ${\rm Pr}[(R_1=j) \ \vert \ (R_2=k)]$
* $= {\rm Pr}[(R_1=j) \wedge (R_2=k)]/{\rm Pr}[R_2=k]$  by definition of conditional probability
* $= {\rm Pr}[R_1=j] * {\rm Pr}[R_2=k] /{\rm Pr}[R_2=k]$ by definition of independence
* $=  {\rm Pr}[R_1=j]$ by algebra assuming ${\rm Pr}[R_2=k] \not - 0$

If we can reasonably believe that two variables are independent, it makes it much easier to reason about them.

## Expected Value, a generalization of the mean

The **expected value** $E(R)$ of a random varaible $R$ on a probability space with sample space $S$ is defined to be

$$
{\rm E}[R] = \sum_\limits{\omega\in S} R(\omega)\ {\rm Pr}[\omega]
$$


When $S$ is a finite set and every outcome has the same probability, this gives the mean of that set of values!
Expected value is more general than the mean as it allows for non-uniform distributions and even infinite sample
spaces.

We can also define the expected value in terms of larger events than outcomes.

**Theorem** 
The expectation is the weighted average of all values in the range of $R$
where the weights are the probability the variable takes that value, i.e.

$$
{\rm E}[R] = \sum_\limits{k\in R(S)} k\ {\rm Pr}[R=k]
$$

## Exercise 3
Let $S$ be the sample space of rolls of 1 six-sided die and let $R_1(\omega)$ be the
value that is rolled. What is the expected value of $R$ assuming the die is fair?
What if the die is loaded so that "1" appears 50% of the time and the other 5 numbers
appear $10% of the time?
Suppose we are rolling $k$ dice, let $R_k$ be the random variable that sums the values on
the dice. What is the expected value of $R_2$?

## Exercise 4
Let $S$ be the sample space of all craps games, i.e. an outcome is a sequence of dice rolls
that might appear in a game of Craps. Let $R$ be the random variable which counts the lenght
of the game, i.e. the number of time the dice were rolled.  How would you calculate the
expected value of $R$, i.e. the averate length of a game of craps?

## Exercise 5
Let $S$ be the sample space of all finite sequences of coin flips.
Let $R(\omega)$ be the position of the first "tails" in the coin flip, so $R(HHHT)=4$
What is the expected value of $R$?

## Applications to Computer Science
A very common application of random variables is to estimate the average esecution time $T$ for a program.
The sample space is the set of all inputs $\omega$, the random variable is the execution time $T(\omega)$on a particular input,
the events of interest are $E_1,E_2,\ldots$ where $E_k$ is the set of inputs of size $k$ and we want to find
a formula for the expected value of $T$ when we restrict $S$ to the inputs of size $k$, or when we model 
a distribution which occurs in practice, i.e. what is the probablity that the program be give input $\omega$.

One classic example is to compute the averate execution time for sorting algorithms such as quicksort. 
But this also comes up when analyzing the efficiency of a web app where you can model the likelihood of 
particular inputs from the users (e.g. google searches!)




