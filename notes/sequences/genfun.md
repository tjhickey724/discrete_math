# Generating Function Cheat Sheet

## constant sequence
if $s=(1,1,1,\ldots)$ then $f_s(x) = 1 + x + x^2 + x^3 + \ldots = \sum_\limits{n=0}^\infty x^n$ and 

$f_s(x) = 1/(1-x)$.

## geometric sequence
if $s = (1,t,t^2,t^3,\ldots, t^k,\ldots)$ then  $f_s(x) = 1 + tx + t^2x^2 + t^3x^3 + \ldots = \sum_\limits{n=0}^\infty t^nx^n$ and 

$f_s(x) = 1/(1-tx)$.

## Generalize binomial Theorem
If $s_k = (\binom{r}{k}$ then 
$f_s(x) = (1-x)^r$

where $\binom{r}{k} = \frac{r * (r-1) * \ldots * (r-k+1)}{k!}$ holds for negative and postive real numbers, not just positive integers!

## polynomial sequence
If $s_k=p(k)$ for some polynomial k of degree d, then

$f_s = q(x)/(1-x)^d$ where q is a polynomial of degree less than $d$


## sequences from a recurrence relation
