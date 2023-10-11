# Countable Sets
We say that a set $S$ is countable if there is a surjective function $f$ from $\mathbb{N}$ to $S$.

If a set is countable, then the sequence

$(f(0), f(1), f(2), \ldots )$

can be thought of as counting the elements of $S$ and each element $s$ of $S$ will appear as $f(n)$ for some $n$
because $f$ is surjective.  Some elements of $s$ might appear multiple times unless the function is also injective.
You can try to prove that if there is a surjective $f$ then we can always find a bijective function from $\mathbb{N}$ to $S$.

Let's look at some examples:
* the positive even numbers are countable (let $f(x) = 2x+2$)
* the positive odd numbers are countable (let $f(x) = 2x+1$)
* the positive prime numbers are countable (let $f(n)$ be the nth prime number)

What about other sets like the integers, pairs of integers, the rationals, the reals, the powerset of the integers.
We'll answer those questions next, and the first two are countable, the last two are not!

Proposition. If S and T are countable sets, then so is $S\cup T$.
Proof: let $f$ and $g$ be the counting functions for S and T respectively.
Define h as follows:
* h(2n) = f(n)
* h(2n+1) = g(n)

Then h is surjective onto $S$ and $T$. QED.

Corollary. The integers $\mathbb{Z}$ are countable.
Proof: It is easy to show that the negative integers, $\mathbb{Z}^-$ are countable,
and $\mathbb{Z} = \mathbb{N} \cup \mathbb{Z}^-$ is the union of two countable sets
and so is countable. QED.

Proposition. If S and T are countable sets, then so is $S\times T$.
Proof: First we prove it for $\mathbb{N}^2$ and then for any countable sets.
... under construction ...



But what about the rational numbers?


Theorem. The rational numbers $\mathbb{Q}$ form a countable set.

Proof. First we will prove that the positive rational numbers are countable
and a simple change shows that the negative rationals are too, and so their union is.

To see that the positive rationals are countable, we can ...

---

Theorem. for any non-empty set $S$, there does not exists a surjection from $S$ to its power set.
Proof.
We will prove this by contradiction. Suppose it is false.
Then there is a surjective function $f$ which takes elements $a\in A$ to subsets $S_a$ of $A$.
That is

$f(a) = S_a$

where $a\in A$ and $S_a\subseteq A$.

Let us define T to be the set of all elements $a$ such that $S_a$ does not contain $a$:

$T = \\{a \in A | \  a \not\in S_a\\}$

Since $f$ is surjective, there must be some element $b\in A$ with $T = S_b$.

There are two cases and we will show both lead to a contradiction, hence showing that
$f$ can not be surjective.

case 1: $b \in T$.  In this case, by the definition of $T$ we know $b\not\in S_b$. But $S_b$ was chosen to be equal to $T$.
So $b \not \in T$, which is a contradiction.

case 2: $b\not\in T$. In this case, since $T=S_b$ we known that $b \not\in S_b$, so by the definition of $T$, $b\in T$,
and this is also a contradiction.

Both cases lead to a contradiction, so there can be no such surjective function $f$. **QED**

---

Corollary. The power set of $\mathbb{N}$ is not countable!


