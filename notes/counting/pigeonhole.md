# The Pigeon Hole Principle
This principle gets its name from the observsation that if you have 11 pigeons that are roosting in 10 holes,
then one hole must contain at least 2 pigeons.

Formally, we state it as follows:

**Theorem** Let $f:A\rightarrow B$ be a total function. If $\vert A\vert \gt \vert B \vert$,
then $f$ is not injective, that is there exists $a_1,a_2\in A$ with $a_1\not = a_2$ and $f(a_1)=f(a_2)$

**Proof:** We prove this by contradiction. If not, then $f$ is a bijection from $A$ onto its image $f(A)$
and so $A$ and $f(A)$ have the same size: $\vert f(A) \vert = \vert A \vert$.
But $f(A)\subseteq B$ so the size of $f(A)$ is smaller or equal to the size of $B$. 
Thus, $\vert A\vert = \vert f(A) \vert \le \vert B \vert$, which contradicts our
assumption that  $\vert A\vert > \vert B \vert$. **QED**

**Corollary** Let $f:A\rightarrow B$ be a total function. If $\vert A\vert \gt \vert B \vert$,
then  $\vert f^{-1}(b)\vert \ge 2$ for some $b\in B$.

**Proof:** this is just another way of saying that at least two elements of $A$ get mapped to the same
element of $B$, i.e. that $f$ is not 1-1.

We also have a similar theorem for when $A$ is much bigger than $B$.

**Theorem** Let $f:A\rightarrow B$ be a total function. If $\vert A\vert \gt k* \vert B \vert$ for some integer k>1,
then $\vert f^{-1}(b)\vert \ge k$ for some $b\in B$.

**Proof:** By contradiction. Suppose it is not true, then $\vert f^{-1}(b)\vert \lt k$ for every $b$ in $B$.
But this means that the size of $A$ is at most $k$ times the size of $B$ as $A$ is a disjoiont union of the inverse
images of points in $B$:

$$
A = \bigcup_\limits{b\in B} f^{-1}(b)
$$

and since this is a disjoint union

$$
\vert A \vert = \sum_\limits{b\in B} \vert  f^{-1}(b)\vert \le \sum_\limits{b\in B} k \le \vert B\vert *k
$$

and this contradicts our assumption that $\vert A\vert \gt k* \vert B \vert$  **QED**

# Applications
### Show that is $S$ is the set of at most 20 numbers less than 100, then there are at least 2 subsets of $S$ with the same sum.

**Proof:** ...
