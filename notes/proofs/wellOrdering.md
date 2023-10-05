# The Well Ordering Principle

A very powerful variation of the proof bu contradiction relies on the following statement, called the Well Ordering Principle.

**Theorem** _Every non-empty set of positive integers has a smallest element_

**Proof**

Let's prove it by contradiction... Suppose it is false so there is some
non-empty set of positive integers which doesn't have a smallest elemnet
Since the set is non-empty, it contains at least one number $n$.

But if $n$ is not the smallest element in the set, then there is an $n_1$ in the set with $n_1$ smaller than $n$.
Likewise, since the set has no smallest element it has an $n_2$ smaller than $n_1$. 
Continuing in this way we can construct a sequence of positive integers

$n \gt n_1 \gt n_2 \gt \ldots$

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
So there exists primes $p_1,\ldots,p_r$ and $q_1,\ldots,q_s$ such that

$a = p_1 * \ldots * p_r$ and $b = q_1 * \ldots * q_s$

so $n = a*b = p_1 * \ldots * p_r * q_1 * \ldots * q_s$

which is a factorization into primes. This is a contradiction to the claim that $n$ is a counter example.

Since both cases result in contradictions, there can't be any counterexamples, so the theorem is true.

**QED**

---




