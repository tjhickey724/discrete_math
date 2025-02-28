# The Well Ordering Principle 
# and The Fundamental Theorem of Arithmetic

A very powerful variation of the proof bu contradiction relies on the following statement, called the Well Ordering Principle.

**Theorem** _Every non-empty set of positive integers has a smallest element_

**Proof**

Let's prove it by contradiction... Suppose it is false so there is some
non-empty set of positive integers which doesn't have a smallest elemnet
Since the set is non-empty, it contains at least one number $n$.

But if $n$ is not the smallest element in the set, then there is an $n_1$ in the set with $n_1$ smaller than $n$.
Likewise, since the set has no smallest element it has an $n_2$ smaller than $n_1$. 
Continuing in this way we can construct a sequence of positive integers

$n \gt n_1 \gt n_2 \gt \ldots$ >0

but since these are all positive integers, this sequence of numbers can have length no more than $n$,
hence it has to be a finite sequence with last element $n_k$ which would be the smallest element in the set.
So it does indeed have a smallest element. This is a contradiction, so our theorem is true.  **QED**

### How to use the Well-Ordering Principle.
The standard usage is when proving something by contradiction. We assume the conclusion isn't true
and in such a case, we form a set of counterexamples from the positive integers.  Since such a set has
a smallest element, we use that smallest element to derive a contradition, usually by showing that we could
construct an even smaller counter example.  We implicitly use this principle when our proof has the phrase:

_Let n be the smallest integer which is part of a counterexample_

and assuming we have such an $n$ we either
* show that it is not a counterexample, or
* show that we can use it to construct a smaller counterexample

## Example: 
Here is a typical application. We will show that every number can be factored into primes.


**Definition:** a positive number $n$ has a non-trivial factorization if it can be written as $n=a*b$
with $1\lt a \lt n$ and $1\lt b\lt n$.  

The cases where $n = 1 * n$ and $n = n * 1$ are trivial factorizations which are not interesting to us.

**Definition:** a positive integer $n$ is prime if it can not be factored (non-trivially).

---

**Theorem.** Every positive integer can be represented as a product of prime numbers.

**Proof:** We will prove this by contradiction using the Well-Ordering Principle.  Suppose
it is false and let $n$ be the smallest positive integer which can not be represented as
a product of primes.

We argue by cases. Either $n$ can be factored or it can not be factored.

Case 1: if it can not be factored, then $n$ is by definition a prime, and hence can be represented
as a product of one prime (itself!)  which is a contradiction.

Case 2: if it can be non-trivially factored, then $n=a*b$ with $a$ and $b$ positive integers less than $n$.
Since $n$ is the smallest integer without a factorization into primes, both a and b can be factored into primes.
So there exist primes $p_1,\ldots,p_r$ and $q_1,\ldots,q_s$ such that

$a = p_1 * \ldots * p_r$ and $b = q_1 * \ldots * q_s$

so $n = a*b = p_1 * \ldots * p_r * q_1 * \ldots * q_s$

which is a factorization into primes. This is a contradiction to the claim that $n$ is a counter example.

Since both cases result in contradictions, there can't be any counterexamples, so the theorem is true.

**QED**

---

We actually know that every positive integer has a unique factorization into primes. This is called
the fundamental theorem of arithmetic.

---

**Theorem** [The Fundamental Theorem of Arithmetic] For every positive integer $n$ there is a set of prime numbers $p_1\lt p_2 \lt \ldots p_k$
and positive integers $a_1, a_2, \ldots, a_k$ such that n can be represented a a product of powers of primes

$n = p_1^{a_1} p_2^{a_2} \ldots p_k^{a_k}$

and this representation is unique, that is there is no other set of primes and powers which can be used to
factorize $n$.

---

We won't prove this now, but we will show how it can be used.

---

**Theorem** for every prime $p$ and all positive integer $n$ and $s$, 
$p$ divides $n^s$ if an only if $p$ divides $n$.

**Proof:**
We will prove by this by proving the "if" part first and then the converse,
and we will prove each of these parts by direct proof.

if $p$ divides $n$ then it is easy to see that $p$ divides $n^s$, as $n=pd$ for some d
so $n^s = p^s*d^s$ which is a multiple of $p$.

Suppose now that $p$ divides $n^s$ and let's show that $p$ dividesd $n$.
We know $n$ can be factored into primes in a unique way so

$n = p_1^{a_1} p_2^{a_2} \ldots p_k^{a_k}$

where $p$ is one of the primes, say $p=p_i$

and so $n^s$ has the factorization which raises each of the factors of $n$ to the power $s$

$n = p_1^{sa_1} p_2^{sa_2} \ldots p_k^{sa_k}$

so $p_i$ divides $n$ (in fact $p_i^{a_i}$ divides $n$).

**QED**

---

Here is another Theorem using the Fundamental Theorem of Arithmetic.

---

**Theorem** $\log_2(3)$ is irrational.

**Proof:** 
We will prove this by contradiction. Suppose it is not irrational.
Then there exists positive integers $r,s$  such that $\log_2(3)=r/s$

Remember that $\log_a(b)=e$ means $b = a^e$. So we know that

$3 = 2^{r/s} $

Raising each side to the power $s$ we see that

$3^s = (2^{r/s})^s$

but $(a^b)^c = a^{bc}$ so 

$3^s = (2^{r/s})^s = 2^{(r/s)*s} = 2^r$

But the number $n=3^s$ would then have two different prime factorizations, as $3^s$ and as $2^s$,
and we know by the Fundamental Theorem of Arithmetic, that each positive integer has one and only
one factorization into primes.

This contradiction shows that $\log_2(3)$ can not be rational, and hence is an irrational number.
**QED**

---


