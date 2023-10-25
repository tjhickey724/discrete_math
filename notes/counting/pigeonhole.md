# The Pigeon Hole Principle
This principle gets its name from the observsation that if you have 11 pigeons that are roosting in 10 holes,
then one hole must contain at least 2 pigeons.

Formally, we state it as follows:

**Theorem** Let $f:A\rightarrow B$ be a total function. If $\vert A\vert > \vert B \vert$,
then $f$ is not injective, that is there exists $a_1,a_2\in A$ with $a_1\not = a_2$ and $f(a_1)=f(a_2)$

**Proof:** We prove this by contradiction. If not, then $\vert f(A) \vert = \vert A \vert$,
but $f(A)\subseteq B$ so $\vert A\vert = \vert f(A) \vert \le \vert B \vert$, which contradicts our
assumption that  $\vert A\vert > \vert B \vert$. **QED**

**Corollary** Let $f:A\rightarrow B$ be a total function. If $\vert A\vert > \vert B \vert$,
then  $\vert f^{-1](b)\vert \ge 2$ for some $b\in B$.

**Proof:** this is just another way of saying that at least two elements of $A$ get mapped to the same
element of $B$, i.e. that $f$ is not 1-1.

We also have a similar theorem for when $A$ is much bigger than $B$.

**Theorem** Let $f:A\rightarrow B$ be a total function. If $\vert A\vert >k* \vert B \vert$ for some integer k>1,
then $\vert f^{-1](b)\vert \ge k$ for some $b\in B$.
