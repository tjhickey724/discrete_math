# Generating Function Cheat Sheet

One of the most powerful techniques for finding a closed form for the elements of a recursively defined sequences
it to use the sequence $s$ to create a function $f_s(x)$ and to show how the recursion equation on $s$ translates
into properties of the function $f_s(x)$. We can the use those properties to find a closed form for the coefficients
of the function, which give a formula for the original sequence!

## Definition of the Generating Function for a Sequence
Let $s = (s_0,s_1,\ldots)$ be an infinite sequence of numbers,
then we can associated to $s$ a powerseries $f_s$ (i.e. an infinite degree polynomial)  defined by

$$f_s(x) = \sum_{i=0}^\infty s_i x^i = s_0 + s_1x + s_2x^2 + s_3x^3 + s_4x^4 + \ldots$$

## constant sequence
if $s=(1,1,1,\ldots)$ then 

$$f_s(x) = 1 + x + x^2 + x^3 + \ldots = \sum_\limits{n=0}^\infty x^n$$

and 

$f_s(x) = 1/(1-x)$.

## geometric sequence
if $s = (1,t,t^2,t^3,\ldots, t^k,\ldots)$ then  

$$f_s(x) = 1 + tx + t^2x^2 + t^3x^3 + \ldots = \sum_\limits{n=0}^\infty t^nx^n$$

and 

$f_s(x) = 1/(1-tx)$.

## Generalized Binomial Theorem
If $s_k = \binom{r}{k}$ then 

$$f_s(x) = \sum_\limits{k=0}^\infty \binom{r}{k} x^k = (1+x)^r$$

where $\binom{r}{k} = \frac{r * (r-1) * \ldots * (r-k+1)}{k!}$ holds for all real values of $r$ including negative and positive real numbers, not just positive integers!

### Example
e.g.
* with $r=-2$
  * $\binom{-2}{0}= 1$
  * $\binom{-2}{1}= -2/1$
  * $\binom{-2}{2}= \frac{-2 * -3}{1 * 2} = 3$
  * $\binom{-2}{3}= \frac{-2 * -3 * -4}{ 1 * 2 * 3} = -4$
  * $\ldots$
  * $\binom{-2}{k}= (k+1) * (-1)^k$
  * So

$$(1+x)^{-2} = 1 - 2x +3x^2 -4x^3 + \ldots + (k+1) * (-1)^kx^k + \ldots = \sum_{k=0}^\infty (k+1)(-1)^kx^k$$

and so

$$(1-tx)^{-2} = 1 +2tx +3t^2x^2 +4t^3x^3 + \ldots + (k+1) * t^kx^k + \ldots = \sum_{k=0}^\infty (k+1)t^kx^k$$
  

## polynomial sequence
If $s_k=p(k)$ for some polynomial k of degree d, then

$f_s = q(x)/(1-x)^d$ where q is a polynomial of degree less than $d$


## sequences from a recurrence relation
If $f_s$ is a powerseries in $x$, and $a$ is a number, then $g = ax f_s$ is also a powerseries and

$$
ax f_s(x) = ax\sum_{i=0}^\infty s_i x^i = as_0x + as_1x^2 + as_2x^3 + as_3x^4 + as_4x^5 + \ldots
 = \sum_{i=1}^\infty as_{i-1}x^i
$$

Likewise, 

$$
bx^2 f_s(x)  = bx^2\sum_{i=0}^\infty s_i x^i = bs_0x^2 + bs_1x^3 + bs_2x^4 + bs_3x^5 + bs_4x^6 + \ldots
 = \sum_{i=2}^\infty bs_{i-2}x^i
$$

So

$$ (1 -ax -bx^2) f_s(x) = \sum_{i=0}^\infty s_{i}x^i - \sum_{i=1}^\infty as_{i-i}x^i - \sum_{i=2}^\infty bs_{i-2}x^i
= s_0 + as_1x + \sum_{i=2}^\infty (s_i - as_{i-1}- bs_{i-2})x^i
$$

So if $s$ satisfies the recursive equation

$s_0 = u$ $s_1 = v$ and $s_i = a s_{i-1} + b s_{i-2}$ for all $i\ge 2$

Then we see that

$$(1 -ax -bx^2) f_s(x) = s_0 + as_1 x $$

and $s_0 = u$ and $as_1 = av$ and

$$f_s(x) = \frac {u + avx}{1 - ax - bx^2}$$

So if we can find a closed form for the coefficients of this, then we'll have a closed form for the sequence!

Our first step is to factor $(1-ax-bx^2) = (1-\alpha_1 x) (1 - \alpha_2 x)$
and if $\alpha_1\ne\alpha_2$ we can use polynomial interpolation to find numbers $r$ and $s$ such that

$$f_s(x) = \frac {u + avx}{1 - ax - bx^2} = \frac r {1-\alpha_1 x} + \frac s {1-\alpha_2 x}$$

but if $\alpha_1 = \alpha_2 = \alpha$ then

$$f_s(x) = \frac {u + a v x} {(1-\alpha x)^2}$$

and both of these forms have nice closed form solutions as we have seen above!

A similar argument works for linear recurrences with 3 or more terms...



