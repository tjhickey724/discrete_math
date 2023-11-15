# Overview of Graph Theory and Relations

## Binary Relations

A **binary relation** is a subset $E$ of $A\times B$ for two sets $A$ and $B$ or equivalently a boolean function $R:A\\times H \rightarrow \mathbb{B}$.
When viewed as a boolean function we write
* $aRb \leftrightarrow (a,b)\in E \leftrightarrow R(a,b)=T$

Examples: 
* Let $\mathbb N$ be the natural numbers and let $R$ be the relation defined by $R(a,b) \leftrightarrow a\le b$
* Let $H$ be the set of all five card poker hands and let $R(h1,h2)$ be true if $h2$ is worth more than $h1$
* Let $f:A\rightarrow B$ be a partial function and define $R(a,b) \equiv  f(a)=b$, so every graph can be viewed as a relation




## Multi-valued Partial Functions
Another way to think about a relation is as
a *multi-valued partial function*, which is a function $f:A \rightarrow 2^B$ where $f(a)$ is the set of values that $f$ takes on $a$
which could be empty, could be a single value $b$ or could be set of values $\\{b)1,\ldots,b_n\\}$

For example, we can define $f_1:\mathbb{R} \rightarrow 2^\mathbb{R}$ by $f_1(x)$ is the set of real numbers such that $y^2=x$.
So $f_1(4)= \\{2,-2\\}$ and $f_1(0) = \\{0\\}$ and $f_1(-1) - \\{\\}$, we usually write this as $f_1(x) = \pm \sqrt{x}$.

Let $R$ be the relation defined by $R(x,y) \equiv x=y^2$ then $R$ can be viewed as the multivalued partial function $f_1(x) = \pm \sqrt{x}$

Any binary relation $R$ can be viewed as a multi-valued partial function $f$ and vice versa via
* $aRb \equiv b\in f_R(a)$ and
* $f_R(a) = \\{b: aRb\\}$
We sometime just write $R(a)$ instead of $f_R(a)$.

We can define the image and the inverse image of a set under $R$ in the same way as for functions:
* $R(S) = \\{b: \exists a \ aRb\\}$
* $R^{-1}(T) = \\{a: \exists b\  aRb\\}$

We can also compose multivalued partial functions
* $R_1(R_2(S)) = \\{c\in C | \exists a\in A \exists b\in B aR_1b \wedge bR_2c\\\}$

In other words, it is the set of all elements which can be reached by the following the arrows
from a node in $S$.

## In and out degree
The figure below shows four binary relations

![binary relations](binary_relations.png)

* R1 is not a function, it is however a multi-valued partial function
* R2 is a bijection
* R3 is a surjective partial function
* R4 is an injective function

We can extend the notion of injectivity and surjectivity to Relations by looking at the number of edges leaving each node in A (the out degree)
and the number of edges going into a node in B,  the in degree.
* R is a function if the outdegree $\le 1$ for each $a\in A$
* R is a total function if the outdegree is $= 1$ for each $a\in A$
* R is injective if the indegree is $\le 1$ for each $b\in B$
* R is surjective if the outdegree is $\ge 1$ for each $b in B$


## Partial Orders
A **partial order** is a binary relation $R$ on $A \times A$ for some set $A$, which satisfies the following property
* Transitivity: $\forall a \forall b \forall x \ aRb \wedge bRc \rightarrow aRc$

If it also satisfies the following axiom it is a **strict partial order**
* Irreflexivity $\forall a \neg (aRa)$
  
The canonical partial order is the less-than-or-equal-to relationship on integers $a\le b$
and the standard strict partial order is the less-than relation $a\lt b$.


## Equivalence Relations
An **equivalence relation** is a binary relation $R$ on $A\times A$ which is
* reflexive; $\forall a \ aRa$
* symmetric: $\forall a \forall b aRb \rightarrow bRa$
* transitive: $\forall a \forall b \forall x \ aRb \wedge bRc \rightarrow aRc$

An equivalence relation partitions the set $A$ into equivalence classes consisting of
all of the elements which are equivalent to each other.

### Example
Let $A$ be the set of integers and let $aEb$ be true if 2 divides $a-b$.
The the equivalence classes are the even numbers and the odd numbers.


## Partitioning a set into equivalence classes

Given a partial order $R$ we can define an equivalence relation $E$ by
* $aEb \leftrightarrow aRb \wedge bRa$

for example, the equivalence relation for $a\le b$ on the integers is just equality
* $a==b \ \equiv \ (a\le b) \wedge (b \le a)

We can define a strict partial order from our original partial order by
* $a < b \ \leftrightarrow \  (a\le b) and not (a E b)$

## Linear Orders
a partial order $R$ is a linear order if 
* $\forall a \forall b aRb\ \vee \ bRa$

In many programming languages, the sorting methods ask you to pass in a linear order relation
to allow the elements to be sorted.


## Directed Graphs

A **directed graph (or digraph)** $G$ is a pair $(V,E)$ where $V$ is a set of vertices or nodes, and $E$ is a subset of $V \times V$ called the edges of $G$.
We can draw a 2d visual representation of a graph by plotting each of the points $v$ of $V$ as distinct point $p(v)$ on the x-y plane and then
for each edge $(a,b)$ in $E$ draw a line between the points $p(a)$ and $p(b)$, usually with an arrow at the end point to $b$. 

We say that the the edge $d=(a,b)$ goes from $a$ to $b$,
* $a$ is the tail of $e$
* $b$ is the head of $b$

## Digraphs are another way of thinking about Binary Relations
We can easily create a digraph from a relation R on $A\times B$ by letting $V= A\cup B$ and letting $E = \\{(a\rightarrow b) ir aRb\\}$

Likewise, given a digraph $(V,E)$ we can create a binary relation $R:V\rightarrow V$ where $aRb \equiv (a,b)\in E$

## Labelled graphs
Sometimes we label the edges and/or vertices of a digraph. 

## Directed Acyclic Graphs
A graph without any cycles is called a **directed acyclic graph** or **DAG**

## Factoring a digraph
Any directed graph can be factored into a DAG whose elements are equivalence classes...

**Digraph Factoring Skill**
We will have you practice factoring a digraph into a set of equivalence classes with a DAG ontop of those equivalence classes.

## Finite State Machines aka Deterministic Finite Automata
a good example of a digraph is a finite state machine which is used to define "regular expressions" that can easily
be recognized by computer programs. We'll give some examples in class.

## Non-deterministic Finite Automata
We can create a more general finite state machine where allow multiple edges out of a node to have the same label.
Given an NFA with states S we can create a DFA whose states are a subset of P(S) 
