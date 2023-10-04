# Notation for Summations and Products

## Summation formulas
It is very common to write expressions that represent summations. We do this using the capital greek letter Sigma which allows us to write a sum of several terms in a compressed fashion. For example, we can express the sum of four numbers four numbers $a_0$, $a_1$, $a_2$, and $a_3$.
as 

$a_0 + a_1 + a_2 + a_3$

but if we wanted the sum of $k$ numbers for some integer $k$ we would write

$a_0 + a_1 + a_2 + \ldots + a_k$

a more succinct way of writing this is to use the summation notation as shown below

$\sum_\limits{i=0}^k a_i  = a_0 + a_1 + a_2 + \ldots + a_k$

which we could also write as

$\sum_\limits{0\le i \le k} a_i  = a_0 + a_1 + a_2  + \ldots + a_k$

The constraint beneath the sigma specifies the values that should be used in the summation.

### Polynomials

A typical example is to express a general polynomial of degree k as a sum:

$p(x) = \sum_\limits{i=0}^n a_i x^i = a_0 + a_1x + a_2x^2 + a_3x^3 + \ldots + a_nx^n$

## Product formulas

Likewise, we use the capital greek letter Pi to indicate products. For example,

$\prod_\limits{i=0}^3 a_i  = a_0 * a_1 * a_2 * a_3$

is the product of four numbers $a_0$, $a_1$, $a_2$, and $a_3$ and

$\prod_\limits{i=0}^k a_i  = a_0 * a_1 * a_2 * \ldots * a_k$

is the product of $k$ numbers.

### Factorial

Likewise we can define the factorial $n!$ for an integer $n$ using the following notation.

$n! = \prod_\limits{i=1}^{n} i$

which we could also write as

$n! = 1 * 2 * 3 * 4 * \ldots * n$

but this is slightly confusing because it looks like $n$ has to be at least equal to 5 as we included 5 terms (1,2,3,4,n),
but in fact this notation is used to suggest the way the $a_i$ are related to $i$ and so it should be read to imply that 
$1!=1$, $2!=2$, $3!=6$, $4!=24$

## Practice Problems

Let's get some practice working with mathematical notation...

**Exercise 1a**
Suppose $a_0=2$, $a_1=-3$, $a_2=0$, and $a_3=10$ and $k=3$, 
write down the polynomial given by

$p(x) = \sum_\limits{i=0}^k a_i x^i = a_0 + a_1x + \ldots + a_kx^k$

**Exercise 1b**
What are the values of $a_i$ and $k$ that make the following formula true:

$\sum_\limits{i=0}^k a_i x^i = x^3 +2x^2 -x + 3$

**Exercise 2a**
What is the result of adding the following two polynomials:

$p(x)= x^2-x+1$ and $q(x) = 3x^2 +2x +2$

**Exercise 2b**
What is the result of multiplying the following two polynomials:

$p(x)= x^2-x+1$ and $q(x) = 3x^2 +2x +2$

**Exercise 2c**
With $p(x)$ and $q(x)$ defined as above,
Let $r(x)=p(x)+q(x)$ where

$r(x) = \sum_\limits{i=0}^2 c_i x^i$

What are the coefficients c0, c1, c2?

**Exercise 2d**
With $p(x)$ and $q(x)$ defined as above,
Let $r(x)=p(x)*q(x)$ where

$r(x) = \sum_\limits{i=0}^4 d_i x^i$

What are the coefficients d0, d1, d2, d3, d4?

**Exercise 3a**
if $p(x) = a_0+a_1x + a_2x^2$ and
$q(x) = b_0+b_1x + b_2x^2$,
what is $p(x)+q(x)$

**Exercise 3b**
if $p(x) = a_0+a_1x + a_2x^2$ and
$q(x) = b_0+b_1x + b_2x^2$,
what is $p(x)*q(x)$

**Exercise 4a:**
Suppose $r(x) = \sum_\limits{i=0}^k c_i x^i$,
what are the values of c and k if $r(x)=p(x)+q(x)$
with $p$ and $q$ as in Exercise 3a.

**Exercise 4b:**
Suppose $r(x) = \sum_\limits{i=0}^k d_i x^i$,
what are the values of d and k if $r(x)=p(x)*q(x)$
with $p$ and $q$ as in Exercise 3a.

**Exercise 5:**
Suppose $a_{n,i} = (n+1-i)/i$
what are the values for  $a_{5,1}$, $a_{5,2}$, $a_{5,3}$, $a_{5,4}$, $a_{5,5}$ 

**Exercise 6:**
with $a_{n,i}$ as above what is  $\prod_\limits{i=1}^3 a_{n,i}$

**Exercise 7:**
Write the polynomial $p(x) = 1 + 2x + 3x^2 + 4x^3 + \ldots (n+1)x^n$
using the summation notation. What is the coefficient of $x^k$ as a function of k.


## Using summation notation in proofs


## Using product notation is proofs
We can use this notation to express the Unique Factorization Theorem for integers

---

**Theorem** Every positive integer $n$ can e factored uniquely into primes

$n = \prod_\limits{i=0}^k p_i^{a_i}$

where the $p_i$ are primes $p_1\lt p_2\lt \ldots\lt p_k$ and the $a_i$ are positive integers.

---

We will prove this later in the course. Using this Theorem we can prove another interesting result.
These kinds of results are called "Corollarys to a Theorem" if they can be proved relatively easily from
the Theorem. Think of a Corollary as a relatively easy consequence of the Theorem.

---

**Corollary** Let $p$ be a prime, and the $n$ and $k$ be positive integers, then $p$ divides $n^k$, if and only if $p$ divides $n$.

**Proof:** 
This is a biconditional so we will first prove that $p$ divides $n^k$ implies $p$ divides $n$.  Then we will prove the
converse, that is if $p$ divides $n$, then $p$ divides $n^k$.

Let first assume $p$ divides $n^k$. 
Let $n$ have the prime factorization shown in the Theorem above, then $n^k$ has the same factorization
except the each $a_i$ is multiplied by $k$ because multiplication is commutative.

$n^k =  \prod_\limits{i=0}^k p_i^{a_i}$

So if a prime $p$ divides $n^k$, then it must be one of the $p_i$, and hence it must also divide $n$.

Conversely, if $p$ divides $n$ then $n=pd$ for some integer $d$, so $n^k = p^kd^k = p(p^{k-1}d^k)$ so $p$ divides $n_k$.
**QED**

---
