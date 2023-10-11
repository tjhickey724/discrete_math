# Sets and Logic
We show here that Set Theory is closely related to  the Predicate Calculus
and we derive several of the transformations on set theory formulas.

## Correspondences of Logic and Set Operations
Let $U$ be a set and consider subsets $A,B,\ldots$ of $U$.

Let $\mathbb{B} = \\{{\rm True},{\rm False} \\}$ be the set of Boolean values.

For any subset $A$ we can define a predicate $P_A: U \rightarrow \mathbb{B}$ by

$\forall x \ \ P_A(x) = {\rm True}  \ \leftrightarrow \  (x \in A)$

---

**Theorem.** For any $A,B\subseteq U$
* $\forall x\ \  P_{A\cap B}(x) \leftrightarrow P_A(x) \wedge P_B(x)$
* $\forall x\ \  P_{A\cup B}(x) \leftrightarrow P_A(x) \vee P_B(x)$
* $\forall x \ \ P_{A^c}(x) \leftrightarrow \neg P_A(x) $

**Proof:**
These follow from the definitions of union and intersection of sets. For example,

$A\cap B = \\{ x\in U:\  x\in A \wedge x\in B\\}$

That is, $P_{A\cap B}(x)$ is true 

if and only if $x \in $A\cap B$ which is 

if and only if $x \in A$ and $x \in B$ which is

if and only if $P_A(x)$ and $P_B(x)$ are true

The proof for $\vee$ and $\neg$ is similar. **QED**

---

**Corollary.** Let $A, B, C \subset U$, then
* $(A \cap B)^c = A^c \cup B^c$
* $(A \cup B)^c = A^c \cap B^c$
* $(A^c)^c = A$
* $A \cup (B \cap C) \ = \ (A \cup B) \cap (A \cup C)$
* $A \cap (B \cup C) \ = \ (A \cap B) \cup (A \cap C)$

**Proof:** These follow from the similar rules in logic, e.g.

$(A\cap B)^c = \\{x\in U | \neg (x in A \wedge x in B) \\}$

$= \\{x\in U | \neg (x in A) \vee \neg( x in B) \\}$

$= A^c \ cup B^c$

The other cases are similar. **QED***

---

