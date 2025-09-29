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

$\prod_\limits{i=1}^k a_i  = a_1 * a_2 * \ldots * a_k$

is the product of $k$ numbers.

### Factorial

Likewise we can define the factorial $n!$ for an integer $n$ using the following notation.

$n! = \prod_\limits{i=1}^{n} i$

which we could also write as

$n! = 1 * 2 * 3 * 4 * \ldots * n$

but this is slightly confusing because it looks like $n$ has to be at least equal to 5 as we included 5 terms (1,2,3,4,n),
but in fact this notation is used to suggest the way the $a_i$ are related to $i$ and so it should be read to imply that 
$1!=1$, $2!=2$, $3!=6$, $4!=24$


## Using summation notation in proofs


## Using product notation is proofs
We can use this notation to express the Unique Factorization Theorem for integers

---

**Theorem** Every positive integer $n$ can e factored uniquely into primes

$n = \prod_\limits{i=1}^k p_i^{a_i}$

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

$n^k =  \prod_\limits{i=0}^k p_i^{k a_i}$

So if a prime $p$ divides $n^k$, then it must be one of the $p_i$, and hence it must also divide $n$.

Conversely, if $p$ divides $n$ then $n=pd$ for some integer $d$, so $n^k = p^kd^k = p(p^{k-1}d^k)$ so $p$ divides $n^k$.
**QED**

---
