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

## Partial Orders
A **partial order** is a binary relation $R$ on $A \times A$ for some set $A$, which satisfies the following property
* Transitive $\forall a \forall b \forall x \ aRb \wedge bRc \rightarrow aRc$

If it also satisfies the following axiom it is a **strict partial order**
* Irreflexive $\forall a \neg (aRa)$
  
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
