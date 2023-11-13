# Overview of Graph Theory and Relations

## Binary Relations

A **binary relation** is a subset $E$ of $A\times B$ for two sets $A$ and $B$ or equivalently a boolean function $R:A\\times H \rightarrow \mathbb{B}$.
When viewed as a boolean function we write
* $aRb \leftrightarrow (a,b)\in E \leftrightarrow R(a,b)=T$

Examples: 
* Let $\mathbb N$ be the natural numbers and let $R$ be the relation defined by $R(a,b) \leftrightarrow a\le b$
* Let $H$ be the set of all five card poker hands and let $R(h1,h2)$ be true if $h2$ is worth more than $h1$
* Let $f:A\rightarrow B$ be a partial function and define $R(a,b) \equiv  f(a)=b$, so every graph can be viewed as a relation
* Let $R$ be the relation defined by $R(x,y) \equiv x=y^2$ then $R$ can be viewed as the multivalued partial function $f(x) = \pm \sqrt{x}$


## Directed Graphs

A **directed graph (or digraph)** $G$ is a pair $(V,E)$ where $V$ is a set of vertices or nodes, and $E$ is a subset of $V \times V$ called the edges of $G$.
We can draw a 2d visual representation of a graph by plotting each of the points $v$ of $V$ as distinct point $p(v)$ on the x-y plane and then
for each edge $(a,b)$ in $E$ draw a line between the points $p(a)$ and $p(b)$, usually with an arrow at the end point to $b$. 

We say that the the edge $d=(a,b)$ goes from $a$ to $b$,
* $a$ is the tail of $e$
* $b$ is the head of $b$


  
