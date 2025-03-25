# Generating Function Cheat Sheet

## definition of the Generating Function for a Sequence
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

## Generalize binomial Theorem
If $s_k = \binom{r}{k}$ then 

$$f_s(x) = \sum_\limits{k=0}^\infty \binom{r}{k} x^k = (1+x)^r$$

where $\binom{r}{k} = \frac{r * (r-1) * \ldots * (r-k+1)}{k!}$ holds for negative and postive real numbers, not just positive integers!

e.g.
* with $r=-2$
  * $\binom{-2}{0}= 1$
  * $\binom{-2}{1}= -2/1$
  * $\binom{-2}{2}= -2 * -3/*(1 * 2) = 3$
  * $\binom{-2}{3}= -2 * -3 * -4/*(1 * 2 * 3) = -4$
  * $\binom{-2}{k}= (k+1) * (-1)^k$
* likewise for $r=-3$  $\binom{-3|{k} = (k+1)*(k_2)/2$
* so

$$(1-x)^{-2} = \sum_\limits{k=0}^\infty \binom{-2}{k} x^k = \sum_\limits{k=0}^\infty (k+1)(-1)^{k} (-x)^k =  \sum_\limits{k=0}^\infty (k+1) x^k $$
  

## polynomial sequence
If $s_k=p(k)$ for some polynomial k of degree d, then

$f_s = q(x)/(1-x)^d$ where q is a polynomial of degree less than $d$


## sequences from a recurrence relation
