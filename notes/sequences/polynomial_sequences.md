# Polynomial Sequences

Polynomial sequences have the form $s_n = p(n)$ where $p$ is a polynomial,
e.g. 
* if $p(x)=2x+1$, then $s = (1,3,5,7,9,...)$ is the odd numbers
* if $p(x) = x^2$ then $s = (0,1,4,9,16,25, ...)$ is the sequence of square numbers
* if $p(x) = x(x+1)/2$ then $s=(0,1,3,6,10, \ldots)$ is the triangle numbers 

## The Difference Test
One way to determine that a sequence is a polyomial sequence is by applyng the difference operator $D$
which you get by subtracting the neigboring pairs of numbers in the sequence:

$D(s) = t$ where $t_i = s_{i+1}-s{i}$

If we apply this operator $n$ times and get the zero sequence $(0,0,0,\ldots)$

For example, let's apply $D$ successively to the seequence $s$ of squares 

| sequence | values | description |
| --- | --- | --- |
| $s$ | $(0,1,4,9,16,25,36,49,64,81,100,\ldots)$ | sequence of squares |
| $D(s)$ | $(1,3,5,7,9,11,13,15,17,19,\ldots)$ | sequence of odd numbers|
| $D(D(s))$  | $(2,2,2,2,2,2,2,\ldots)$  | sequence of 2s |
| $D(D(D(s)))$ | $(0,0,0,0,0,\ldots)$ | sequence of 0's |

Let's try it with the triangular numbers

| sequence | values | description |
| --- | --- | --- |
| $s$ | $(0,1,3,6,10,15,21,\ldots)$ | sequence of triangle numbers |
| $D(s)$ | $(1,2,3,4,5,6\ldots)$ | sequence of positive integers|
| $D(D(s))$  | $(1,1,1,1,1,\ldots)$  | sequence of 1s |
| $D(D(D(s)))$ | $(0,0,0,0,0,\ldots)$ | sequence of 0's |

Any sequence which eventually becomes a sequence of zeroes is a polynomial sequence
and if $D^k(s) = 0$ then s is a polynomial sequence of degree $k-1$.

**Difference skill** be able to calculate differences to show a sequence might be polynomial of degree d

## Polynomial Fitting
If you suspect a sequence is a polynomial sequence of degree $n$ then you can use polynomial fitting
to find the polynomial! Let's use the triangle numbers sequence as an example.

Let's assume $s_n = a n^2 + b n + c$ for some numbers a,b,c. Then since we know the value of $s_i$ for small values of $i$ we can conclude that
* $0 = s_0 = a * 0^2 + b * 0 + c = c$
* $1 = s_1 = a * 1^2 + b * 1 + c = a+b+c$
* $3 = s_2 = a * 2^2 + b * 2 + c = 4a +2b + c$

This gives us three linear equations in a,b,c (i.e. not squares or higher powers)
* $c=0$
* $a+b+c = 1$
* $4a + 2b + c = 3$

## Solving Systems of Simultaneous Linear Equations
Using the Polynomial fitting approach always generates a set of linear equations whose variables
are the coefficients of the polynomial, and we can evaluate the polynomial of degree k on k+1 points
so we wil have k+1 equations in k+1 variables. Any such system can be "solved" if it does come from a 
polyomial sequence. The process is to add and subtact multiples of the equations from each other to
eliminate variables and then to use substitution to get the values of the eliminated variables. We illustrate
that below with our "triangle number" example.

Since we have three linear equations in three variables, we can attempt to solve this by substituting in 
values (e.g. c=0) into the other equations and then subtracting multiples of one equation against another to
eliminate variables...

Start with replacing $c$ with 0 in the other two equations and we get:
* $a+b=1$
* $4a+2b=3$

now multiply the first equation by 4 to get $4a+4b=4$ and subtract the seccond equation to get
* $2b = 1$

so $b=1/2$  and substitution into $a+b=1$ we get $a+1/2 = 1$ so $a=1/2$


and this shows that $s_n = (1/2)n^2 + (1/2)n = n(n+1)/2$

**Solving Linear Equations skill** use variable elimination and substitution to solve a system of linear equations

**Polynomial fitting skill** use polynomial fitting to find the coefficients of a possible polynomial closed for for a sequence

## Recurrence Equations
Polynomials sequences often arise when analyzing algorithms and we are able to verify two properties of the sequence:
* a base condition $s_0=a_0$, $s_1=a_2$, ... for some numbers $a_0$, $a_1$, ...
* a recurrence relations: $s_n = s_{n-1}+ f(n)$ for some function $f$ and all $n>j$ for some number $j$.

Notice that if $s$ is defined by a recurrence relation as above, then
* $s_n = s_{j}+ \sum_\limits{i=j+1}^\infty f(j)$

For example, the triangle numbers are defined by $s_n = s_{n-1} + n$ for $n>0$ and $s_0=0$, so
* $s_n = \sum_\limits{i=0}^n i = 0.5 n^2 + 0.5 n$

If $f$ is a polynomial of degree $d$ then $s$ is a polynomial sequence of degree $d+1$

If you have a polynomial sequence defined by a recurrence relation, and you have used polynomial fitting 
to find a candidate polynomial p where $s_n=p(n)$, you can prove that $s_n=p(n)$ using induction

## Induction
We show how to prove that a predicate $P(n)$ is true for all $n$ by proving the following to properties:
* $P(0), P(1), \ldots, P(k)$ are true
* $\forall j>k: P(j) \rightarrow P(j+1)$

If these two propositions are true, then we can conclude that
* $\forall n P(n)$ is true where $n$ ranges over all natural numbers, 0,1,2,...

Let's try this out!


**Induction skill** use induction to show that a sequence defined by a summation or a recurrence equation is polynomial for a particular polynomial $p$.



