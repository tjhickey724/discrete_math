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
| $$ | $(0,1,4,9,16,25,36,49,64,81,100,\ldots)$ | sequence of squares |
| $D(s)$ | $(1,3,5,7,9,11,13,15,17,19,\ldots)$ | sequence of odd numbers|
| $D(D(s))$  | $(2,2,2,2,2,2,2,\ldots)$  | sequence of 2s |
| $D(D(D(s)))$ | $(0,0,0,0,0,\ldots)$ | sequence of 0's |

Any sequence which eventually becomes a sequence of zeroes is a polynomial sequence
and if $D^n(s) = 0$ then s is a polynomial sequence of degree $n-1$.

## Polynomial Fitting
If you suspect a sequence is a polynomial sequence of degree $n$ then you can use polynomial fitting
to find the polynomial! Let's use the triangle numbers sequence as an example.

## Recurrence Equations




