# Mathematical Notation
We present below some of the standard mathematical notation that you will often see in proofs.

_UNDER CONSTRUCTION_

## Variables
variables typically are single letters in the latin font (a,b,c,...,x,y,z)
but sometime other character sets are used. Most common are 
[greek letters]([https://en.wikipedia.org/wiki/Greek_letters_used_in_mathematics,_science,_and_engineering](https://www.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols)https://www.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols):

| name | lowercase | upper case |
|--- | --- | --- |
|alpha| $\alpha$| $A$|
| beta |$\beta$ |$B$|
| gamma |$\gamma$| $\Gamma$|
| delta |$\delta$ |$\Delta$|
| epsilon |$\epsilon$ |$E$|
| zeta | $\zeta$ | Z|
|eta | $\eta$ | H |
|theta | $\theta$| $\Theta $|
| iota |$\iota$ | I |
| kappa | $\kappa$ | K|
|lambda | $\lambda$ | $\Lambda$ |
| mu | $\mu$ | M |
| nu | $\nu$ | N |
| xi | $\xi$ | $\Xi$ |
| omicron | o | O|
| pi | $\pi$ | $\Pi$|
| rho | $\rho$ | P |
|sigma | $\sigma$ | $\Sigma$ |
| tau | $\tau$ | T|
|upsilon | $\upsilon$ | $\Upsilon$ |
| phi | $\phi$ | $\Phi$ |
| chi | $\chi$ | X |
| psi | $\psi$ | $\Psi$ |
| omega | $\omega$ | $\Omega$|

And sometimes letters from other alphabets such as Hebrew aleph $\aleph$

## Subscripts
We often add subscripts to a variable so we can refer to a sequence of values, e.g.
* $a_1,a_2,\ldots,a_n$

and we refer to one of these variables using an index variable for the subscript
* $a_i$

If we need a table of values, we can use two subscripts

| ...| column1 | column2 |column3 |
|---|---|---|---|
|row 1 | $a_{1,1}$ | $a_{1,2}$ | $a_{1,3}$ |
|row 2 | $a_{2,1}$ | $a_{2,2}$ | $a_{2,3}$ |

and we refer to one of these variables with index variables (typically $i,j,k,...$

In general we can have as many subscripts on a variable as we need
* $b_{i,,k}$, $c_{r,s,t,u,v}$

but it gets confusing to have too many subscripts

## Summation and Product formulas
It is very common to write expressions that represent summations. We do this using the capital greek letter Sigma which allows us to write a sum of several terms in a compressed fashion. For example

$\sum_\limits{i=0}^3 a_i  = a_0 + a_1 + a_2 + a_3$

which we could also write as

$\sum_\limits{0\le i \le 3} a_i  = a_0 + a_1 + a_2 + a_3$

The constraint beneath the sigma specifies the values that should be used in the summation.

A typical example is to express a general polynomial of degree k as a sum:

$p(x) = \sum_\limits{i=0}^k a_i x^i = a_0 + a_1x + a_2x^2 + a_3x^3 + \ldots + a_nx^n$

Likewise, we use the capital greek letter Pi to indicate products. For example,

$\prod\limits_{i=0}^3 a_i  = a_0 * a_1 * a_2 * a_3$

$n! = \prod_limits_{i=1}^{n} i $




