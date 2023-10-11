# Binary Relations

Next we look at a binary relations, which are a generalization of the notion of function and which have many applications in Computer Science.

A binary relation $R$ consists of
* a set $A$, called the domain of $R$ and
* a set $B$ called the codomain of $R$, and
* a subset $G_R$ of $A\times B$ called the graph of $R$

We indicate that $(a,b)\in G_R$ by the notation $aRb$.

**Example 1.**
A standard example is the $\le$ relation on the real numbers
where $A=B=\mathbb{R}$ and $R$ is defined as follows:

$$
aRb \ \equiv \ (a\le b)
$$


**Example 2**
Any function $f:A\rightarrow B$ defines a relation $R_f$ by

$$
aR_f b \ \equiv \ f(a)=b
$$


**Example 3**
The square root function (with both positive and negative branches) is another
good example.

* $x S y \equiv (x = y^2)$ 

this corresponds to the square root function 
* $y = \sqrt{x}$ 

which is only defined for $x\ge 0$.
If $x=0$ it has one value $\\{0\\}$
and if $x\gt 0$ it has two values: the positive square root and the negative square root!
* $f_S(-1) = \\{\\}$
* $f_S(0) = \\{0\\}$
* $f_S(1) = \\{-1,1\\}$
* $f_S(2) = \\{\sqrt{2},-\sqrt{2}\\}$

**Example 4.**
Finite Bipartite Graphs.  Next we have an example from graph theory.
Suppose that A and B are finite sets. Then R can be visualized as arrows from
elements of A on the left to elements of B on the right. We can use this analogy
even with infinite sets $A$ and $B$ though it may be impossible to draw the diagram
for complex relations. 
