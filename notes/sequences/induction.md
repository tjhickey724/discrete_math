# Induction
In this section we show how to prove that a close formula holds for a sequence defined recursively.
We will use a special case of the Induction Technique.

## Induction Proofs
The induction axiom for the natural numbers $\mathbb{N}$ is used to prove statement of the form
* $\forall n P(n)$

where $P(n)$ is some predicate on the natural numbers $\mathbb{N}$ and the universal quantifier is over all natural numbers $\\{0,1,2,\ldots\\}$

We can prove such a proposition by first proving two simpler propositions:
* A) Prove $P(0)$ is true
* B) Prove that $forall n. P(n) \rightarrow P(n+1)$

From (A) we know P(0) is true, and hence by (B) P(1) is true, and so P(2) is true, etc....
Hence P(n) is true for all $n\ge 0$.

Sometimes it is easier, with the math notation to prove that P(n-1) implies P(n) for all $n\ge 1$
instead of proving P(n) implies P(n+1) for all $n\ge 0$, but it is the same statement.

## Example 1
Let $s$ be the sequence defined by $s_0=0$, and $s_n=s_{n-1}+n$ for all $n\ge 1$.

By unwinding this definition we see that $s_n = 0 + 1 + 2 + 3 + \ldots + n = \sum_\limits{i=0}^n i$
which is a non-recursive way to define this sequence.

---

**Theorem.** $s_n = \sum_\limits{i=0}^n i = n(n+1)/2$.

**Proof:** We prove this by induction where $P(n)$ is the statement $s_n = n(n+1)/2$.

First we prove that $P(0)$ is true i.e. that $s_0 = 0(0+1)/2 = 0$, which is true by definition of $s$

Next we assume that $P(n-1)$ is true and prove that $P(n)$ is true.
* $P(n-1)$ is $s_{n-1} = (n-1) * ((n-1)+1)/2 = (n-1)n/2 = (n^2-n)/2$

and by the definion of $s_n$ we know that
* $s_n = s_{n-1} + n$
So if we substitute in the formula for $ds_{n-1}$ that we get from induction we find that
* $s_n = (n^2-n)/2 + n = (n^2-n+2n)/2 = (n^2+n)/2 = n(n+1)/2$

which is what we were supposed to prove. **QED**


## Strong Induction
Sometimes we need a stronger form of induction (which is actually a consequence of regular induction).
That is we need to assume that $P(d)$ is true for all $d\lt n$ and then we can show that $P(n)$ is true.

We can prove a proposition by strong induction by first proving two simpler propositions:
* A) Prove $P(0)$ is true
* B) Prove that $(forall d\lt n\  P(d)) \rightarrow P(n)$

From (A) we know P(0) is true, and hence by (B) P(1) is true, and so P(2) is true, etc....
Hence P(n) is true for all $n\ge 0$.

---

## Example 2.
Let's try this on an exponential sequence. We will use strong induction, since we will prove that a formula for $s_n$ holds
by assuming it holds for $s_{n-1}$ and $s_{n-2}$.

Suppose we define $s$ by
* $s_0 = 0$
* $s_1 = 1$
* $s_n = 4 *(s_{n-1}  - s_{n-2})$ for all $n\ge 2$

Then in the last lesson we showed that if the closed form for this has the shape $s_n = (an+b)2^n$, then a=1/2 and b=1/2, that is
* $s_n = n*2^{n-1}$

But can we prove that this holds directly?  Yes, using induction.

---

**Theorem.** Let $s_n$ be the sequence defined above, then 
* $\forall n s_n = n 2^{n-1}$

**Proof:** We prove this using induction on $n$. For n=0 and 1 it holds because
* $0 * 2^{0-1} = 0 * 1/2 = 0 = s_0$
* $1 * 2^{1-1} = 1 * 2^0 = 1 * 1 = 1 = s_1$

and for $n\ge 2$ lets assume, by induction that $s_k = k 2^{k-1}$, then
* $s_{n-1} = (n-1) 2^{n-1-1} = (n-1) 2^{n-2}
* $s_{n-2} = (n-2) 2^{n-2-1} = (n-2) 2^{n-3}

So
* $s_n = 4 s_{n-1} - 4 s_{n-2}$
* $\ \  = 4 (n-1) 2^{n-2} - 4 (n-2) 2^{n-3}$
* $\ \  = (n-1)2^n - (n-2)2^{n-1}$  as $4=2^2$ and $2^a * 2^b 2^{a+b}$
* $\ \  = n2^{n} - 2^n + n 2^{n-1} - 2 * 2^{n-1}$
* $\ \  = n(2^{n} - 2^{n-1}) + 2^n -  2^{n}$
* $\ \  = n 2^{n-1} $, as $2^n - 2^{n-1} = 2^{n-1} * (2 - 1) = 2^{n-1}$

and this is what we were trying to prove. **QED**

---




