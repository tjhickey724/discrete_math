# Notation for Summations and Products

## Summation and Product formulas
It is very common to write expressions that represent summations. We do this using the capital greek letter Sigma which allows us to write a sum of several terms in a compressed fashion. For example

$\sum_\limits{i=0}^3 a_i  = a_0 + a_1 + a_2 + a_3$

which we could also write as

$\sum_\limits{0\le i \le 3} a_i  = a_0 + a_1 + a_2 + a_3$

The constraint beneath the sigma specifies the values that should be used in the summation.

A typical example is to express a general polynomial of degree k as a sum:

$p(x) = \sum_\limits{i=0}^k a_i x^i = a_0 + a_1x + a_2x^2 + a_3x^3 + \ldots + a_nx^n$

Likewise, we use the capital greek letter Pi to indicate products. For example,

$\prod_\limits{i=0}^3 a_i  = a_0 * a_1 * a_2 * a_3$

$n! = \prod_\limits{i=1}^{n} i$

We can use this notation to express the Unique Factorization Theorem for integers

---

**Theorem** Every positive integer $n$ can e factored uniquely into primes

$n = \prod_\limits{i=0}^k p_i^{a_i}$

where the $p_i$ are primes $p_1\lt p_2\lt \ldots\lt p_k$ and the $a_i$ are positive integers.

---

We will prove this later in the course. Using this Theorem we can prove another interesting result.
These kinds of results are called "Corollarys to a Theorem" if they can be proved relatively easily from
the Theorem. Think of it as a relatively easy consequence of the Theorem.

---

**Corollary** If a prime $p$ divides $n^k$, for positive integers $n$ and $k$, then $p$ divides $n$.

**Proof:** Let $n$ have the prime factorization shown in the Theorem, then $n^k$ has the same factorization
except the each $a_i$ is multiplied by $k$

$n^k =  \prod_\limits{i=0}^k p_i^{a_i}$

So if a prime $p$ divides $n^k$, then it must be one of the $p_i$, and hence it must also divide $n$.

**QED**
---

Let's get some practice working with mathematical notation...

**Exercise 1**
What are the values of $a_i$ and $k$ that make the following formula true:

$\sum_\limits{i=0}^k a_i x^i = x^3 +2x^2 -x + 3$

**Exercise 2**
if $p(x) = a_0+a_1x + a_2x^2$ and
$q(x) = b_0+b_1x + b_2x^2$,
what is $p(x)*q(x)$

**Exercise 3:**
with $p$ and $q$ as in Exercise 2, what is $p(x)*q(x)$

**Exercise 4:**
Suppose $r(x) = \sum_\limits{i=0}^k c_i x^i$,
what are the values of c and k if $r(x)=p(x)*q(x)$

**Exercise 5:**
Suppose $a_{n,i} = (n-i)/i$
what are the values for $a_{5,1}$, $a_{5,2}$, $a_{5,3}$, $a_{5,4}$, $a_{5,5}$ 

**Exercise 6:**
with $a_{n,i}$ as above what is  $\prod_\limits{i=1}^3 a_{n,i}$

**Exercise 7:**
Write the polynomial $x^n + 2x^{n-1} + 3x^{n-2} + \ldots + nx + (n+1)$
using the summation notation.
