# Generating Function Cheat Sheet

## constant sequence
if $s=(1,1,1,\ldots)$ then $f_s(x) = 1 + x + x^2 + x^3 + \ldots = \sum_\limits{n=0}^\infty x^n$ and 

$f_s(x) = 1/(1-x)$.

## geometric sequence
if $s = (1,t,t^2,t^3,\ldots, t^k,\ldots)$ then  $f_s(x) = 1 + tx + t^2x^2 + t^3x^3 + \ldots = \sum_\limits{n=0}^\infty t^nx^n$ and 

$f_s(x) = 1/(1-tx)$.

## combination series
if $s = (\binom{n}{0},\binom{n}{1},\binom{n}{2},\ldots,\binom{n}{k},\ldots)$ then $s_k = \binom{n}{k}$ and

$f_s = 1/(1-x)^k

## polynomial series
If $s_k=p(k)$ for some polynomial k of degree d, then

$f_s = q(x)/(1-x)^d$ where q is a polynomial of degree less than $d$

## sequences from a recurrence relation
