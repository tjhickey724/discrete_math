# Induction
In this section we show how to prove that a close formula holds for a sequence defined recursively.
We will use a special case of the Induction Technique.

## Induction Proofs
The induction axiom for the natural numbers $\mathbb{N}$ is used to prove statement of the form
* $\forall n P(n)$

where $P(n)$ is some predicate on the natural numbers $\mathbb{N}$ and the universal quantifier is over all natural numbers $\\{0,1,2,\ldots\\}$

We can prove such a proposition by first proving two simpler propositions:
* A) Prove $P(0)$ is true
* B) Prove that $\forall n. P(n) \rightarrow P(n+1)$
* C) Conclude that $\forall n\ P(n)$

From (A) we know P(0) is true, and expanding out (B) we see
* B1) $P(0) \rightarrow P(1)$
* B2) $P(1) \rightarrow P(2)$
* B3) $P(2) \rightarrow P(3)$
* $\ldots$
  
and hence since $P(0)$ is trye and (B1) says $P(0)\rightarrow P(1)$, we know $P(1)$ is true.

Similarly for $P(2)$, $P(3)$, etc.
  
Hence P(n) is true for all $n\ge 0$.

Sometimes it is easier, with the math notation to prove that P(n-1) implies P(n) for all $n\ge 1$
instead of proving P(n) implies P(n+1) for all $n\ge 0$, but it is the same statement.

## Example 1
Let $s$ be the sequence defined by $s_0=0$, and $s_n=s_{n-1}+n$ for all $n\ge 1$.

By unwinding this definition we see that $s_n = 0 + 1 + 2 + 3 + \ldots + n = \sum_\limits{i=0}^n i$
which is a non-recursive way to define this sequence.

---

**Theorem.** $s_n = \sum_\limits{i=0}^n i = n(n+1)/2$.

**Proof:** We prove this by induction on $n$ where $P(n)$ is the statement $s_n = n(n+1)/2$.

First we prove the base case, that $P(0)$ is true i.e. that $s_0 = 0(0+1)/2 = 0$, which is true by definition of $s$

Next we assume that $P(n-1)$ is true and our induction hypothes is that
* $s_{n-1} = (n-1) * ((n-1)+1)/2$
*  $\ \ \ \  = (n-1)n/2 = (n^2-n)/2$, after simplification

and by the definion of $s_n$ we know that
* $s_n = s_{n-1} + n$
 
So if we substitute in the formula for $s_{n-1}$ that we get from induction we find that
* $s_n = (n^2-n)/2 + n$
* $\ \  = (n^2-n+2n)/2 = (n^2+n)/2 = n(n+1)/2$ after simplification

which is what we were supposed to prove. So 
$s_n = n(n+1)/2$ is true for all $n\ge 0$ by induction.
**QED**

You can try to find a closed form for $\sum_\limits{i=0}^n i^2$ and prove that is is correct using induction.

## Strong Induction
Sometimes we need a stronger form of induction (which is actually a consequence of regular induction).
That is we need to assume that $P(d)$ is true for all $d\lt n$  not just for $n-1$,
and then we can show that $P(n)$ is true.

We can prove a proposition by strong induction by first proving two simpler propositions:
* A) Prove $P(0)$ is true
* B) Prove that $\forall n\ (\forall d\lt n\  P(d)) \rightarrow P(n)$
* C) Conclude that $\forall n \ P(n)$

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

If we knew that the closed form for this has the shape $s_n = (an+b)2^n$, then a=1/2 and b=1/2, that is
* $s_n = n*2^{n-1}$

But can we prove that this holds directly?  Yes, using induction.

---

**Theorem.** Let $s_n$ be the sequence defined above, then 
* $\forall n \ s_n = n 2^{n-1}$

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

so $s_n = n 2^{n-1}$ 
and this is what we were trying to prove. **QED**

---

## Example 3.
Induction is a general proof technique that works whenever you want to prove something is true
for all natural numbers n.

Here is an example of a strong induction proof that has nothing to do with sequences.

Suppose we take one of those chocolate bars which you can break into smaller squares. 
It is typically a 8x4 grid of squares, but in principle it could be any $n x m$ grid of squares.

If we break it along one of the vertical or horizontal lines we'll get two smaller chocolate bars, e.g.
a 4x8 could be broken into a 1x8 and 3x8   or a 4x1 and 4x7 or  a 4x3 and 4x5.

--- 

**Theorem.** The number of breaks you need to split an $n \times m$ chocolate bar into $1 \times 1$ squares
is $nm-1$.

**Proof.** We will prove this by strong induction on $nm$.

_Base case:_ if $nm=1$ then $n=1$ and $m=1$ and it is already a 1x1 square so it requires $1-1=0$ breaks!

_Induction case:_ There are two cases actually, we can break it vertically (if $m\gt 1$ or horizontally if $n\gt 1$)
and if $n$ and $m$ are both 1, we are in the base case, so it is true.

If we break it vertically, then $m=ab$ and we break the $n\times m$ into two pieces $n \times a$ and $n \times b$.

By induction the number of steps to break these two parts are $na-1$ and $nb-1$ so the total number of steps to break the
chocolate bar is $1 + na-1 + nb-1 = 1 + n(a+b) -2 = nm +1-2 = nm-1$ as was to be proved.

The case of breaking horizontally is essentially the same, but we let $n=a+b$ and have pieces of size $a \times m$ and $b\times m$.
By induction they can be fully broken down in $am-1$ and $bm-1$ steps, so the total number of steps is $1 + am-1 + bm-1 = (a+b)m +1-2 = nm-1$.

Since it is true in both cases, we have proven the Theorem by induction. **QED***

---

You can try to prove that the parse tree for a Propositional Formula with $n$ logical operators will have $2n+1$ nodes.
For example, $P\wedge (Q \rightarrow P) \vee (P \oplus Q)$ has 4 operators and the tree and and 9 nodes total (i.e. 5 propositional symbols).
Prove it by induction on the the number of operators.





