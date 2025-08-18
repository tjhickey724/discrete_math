# Mathematical Notation
We present below some of the standard mathematical notation that you will often see in proofs.

## Variables
variables typically are single letters in the latin font (a,b,c,...,x,y,z)
but sometime other character sets are used. Most common are 
[greek letters]([https://en.wikipedia.org/wiki/Greek_letters_used_in_mathematics,_science,_and_engineering](https://www.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols)https://www.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols):

| name | lower case | upper case |
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

and we refer to one of these variables with index variables e.g. $a_{i,j}$

In general we can have as many subscripts on a variable as we need
* $b_{i,k}$, $c_{r,s,t,u,v}$

but it gets confusing to have too many subscripts

## Sequences
We can use this subscript notation to define an infinite sequence 
$a_1,a_2,a_3,\ldots$ of numbers. For example,

* the sequence $1,3,5,7,9,11,\ldots$ of odd numbers is defined by $a_i=2i+1$
* the sequence $1,4,9,16,25,36,\ldots$ of square numbers is defined by $a_i=i^2$
* the fibonacci sequence $1,1,2,3,5,8,13,21,\ldots$ is defined by $a_1=a_2=1$ and for each $i>2$ we get the next number in the sequence by adding the previous 2. In our notation we write that as:

  $a_i = a_{i-1} + a_{i-2}$  for all $i>2$



  

