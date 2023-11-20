# Overview of Graph Theory and Relations

## Binary Relations

A **binary relation** is a subset $E$ of $A\times B$ for two sets $A$ and $B$ or equivalently a boolean function $R:A\\times B \rightarrow \mathbb{B}$.
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
Any directed graph can be factored into a DAG whose elements are equivalence classes of the relation
defined by $a\equiv b$ if there is a path from a to b and vice versa.

**Digraph Factoring Skill**
We will have you practice factoring a digraph into a set of equivalence classes with a DAG ontop of those equivalence classes.

## Finite State Machines aka Deterministic Finite Automata
a good example of a digraph is a finite state machine which is used to define "regular expressions" that can easily
be recognized by computer programs. We'll give some examples in class.

**DFA Skill** - determine a DFA for some set of strings and/or determine if a string is accepted by a particular DFA

## Non-deterministic Finite Automata
We can create a more general finite state machine where allow multiple edges out of a node to have the same label.
Given an NFA with states S we can create a DFA whose states are a subset of P(S) 

# Representing Digraphs
The simplest way to represent a digraph is as a 2d table of integer values where
* the ith row and jth column contains $1$ if there is an edge from vertex $i$ to vertex $j$
* otherwise there it contains $0$

This table is called the adjacency matrix.

For a very large matrix it is better to just have a list of adjacent vertices for each vertex.

# Paths in a digraph
It turns out that there is a nice way to calculate the number of paths between each pair of vertices using
the adjacency matrix.  Let $A$ be the adjacency matrix for a graph G with nodes $\\{1,2,\ldots,n\\}$, then
* the entry in A for the ith row and jth column is denoted $A_{ij}$
* this is the number of paths from $i$ to $j$ of length 1

To calculate the number of paths of length 2 between $i$ and $j$ we need to count the number of nodes $k$ for which
there is a path from $i$ to $k$ and from $k$ to $j$.  If we let $A^2$ be the matrix whose $ij$ th entry is the number of paths from $i$ to $j$ of length 2, then
* $A^2_{ij} = \sum_\limits{k-1}^n A_{ik} * A_{kj}$

Notice that this will take $n^3$ multiplications to find all of $n^2$ entries in the matrix $A^2$.

and this is exactly the definition of the matrix multiplication of $A$ with itself!

## Matrix Multiplication
If $A$ is a rxs matrix and $B$ is a sxt matrix, then $A * B$ is the matrix $C$ whose entries are
* $C_{ij} = \sum_\limits{k=1}^s A_{ik}*B_{kj}$

Visually we multiply the $i$ th row by the $k$ th column, by multiplying the corresponding elements (1st 2nd 3rd ..)
and summing those products. Here is an example:

```
1 1 0        1 0 0       2 1 0
0 0 1    *   1 1 0  =    1 1 1
1 0 0        1 1 1       1 0 0
```
For example, multiplying the 1st row of A by the 2nd column of B gives 
* $(1 1 0) * (0 1 1) = 1 * 0 + 1 * 1 + 0 * 1 = 1$

## Reachability and Transitive Closure

We can use a similar approach if we want to find whether node i is reachable from node j.

If we defined the relation $a\prec b$ to mean b is reachable from a, then it is clear this
is a partial order (i.e. it is transitive), but it may not be a strict partial order. We
can compute this relation using a kind of matrix multiplication... 

The reachability relation for a partial order is called the transitive closure of that partial order. Given the adjacency matrix of a partial order, we would like to compute the adjacency
matrix of the transitive closure relatively quickly....

To do this, we can use an adjacency matrix with Boolean values, were 
* $A_{ij}=T$ if i=j or if there is an edge from i to j and
* $A_{ij}=F$ otherwise

To see if there is a path from $i$ to $j$ of length 2, we would use the following calculation
* $A^2_{ij} = \bigvee_\limits{k=1}^n A_{ik}\wedge A_{kj}$

This is just matrix multiplication but using $\vee$ for addition and $\wedge$ for multiplication.

Calculating this boolean matrix requires about $n^3$ conjunctions and disjunctions.

Similarly, we can use the same approach to calculate $(A^2)^2=A^{2^2}$ which will take anohter $n^3$ steps

Continuing $k$ times we can calculate $B = A^{2^k}$ in $kn^3$ steps 
and this will be matrix where $B_{ij}=T$ if there is apath from $i$ to $j$ of length $2^k$ or less.

If the graph contains $n$ nodes, then if there is a path from $i$ to $j$, then there is a path with length
at most $n$ (Prove it!)

This implies that if we compute $B=A^{2^k}$ for $2^k\ge n$,
then $B_{ij}=T$ if and only if there is a path from $i$ to $j$ of any length.

Since $2^k\ge n$ if and only if $k \ge \log_2(n)$, this means we can compute the reachability matrix for the graph $G$
in time $n \log_2(n)$ by repeatedly squaring the matrix $A$ $\log_2(n)$ times.



## Regular Expressions and NFAs
A regular expression over a set $\Sigma$ (Sigma) of characters is defined as follows
* any character $\sigma\in \Sigma$ is a regular expression
* if $\alpha_1$ and $\alpha_2$ are regular expressions then so are $\alpha_1 + \alpha_2$ and $\alpha_1 \alpha_2$
* if $\alpha$ is a regular expression then so is $\alpha *$
* if $\alpha$ is a regular expression then so is $(\alpha)$

A Regular Expressions $\alpha$ defines a set $S(\alpha)$ of strings of characters, by the following rules
* $S(\sigma) = \\{\sigma\\}$ for any character $\sigma\in\Sigma$
* $S(\alpha_1+\alpha_2) = S(\alpha_1)\cup S(\alpha_2)$
* $S(\alpha_1\alpha_2) = \\{a_1 a_2 | a_i\in S(\alpha_i)$\\}$
* $S(\alpha *) = \\{\epsilon\\} \cup S(\alpha alpha *)$ where $\epsilon$ is the empty string and $\epsilon a = a$


For example $a(a+b)*b$ is a regular expression corresponding to all strings that start with an "a", end with a "b"
and have zero or more "a"s or "b"s between them.

It is relatively easy to go from a RE to a NFA
and we have seen earlier how to convert an NFA to a DFA.

## Converting an NFA to a Regular Expression
You can convert an NFA to a RE using a Generalized NFA  (GNFA) where the
edges are marked with regular expressions, not just single characters.
The algorithm is as follows:
* create a new start state and a new final state and add epsilon transitions between the new start and final states and the original start and final states
* remove states from a graph one at a time, resulting in a new GNFA with one fewer state
* continue until you have just one edge from the start state to the final state

The image below shows how to remove a node $b$ from a GNFA  which has $n$ incoming and $k$ outgoing edges and 1 loop.
This process removes the $n+k+1$ edges and 1 node and adds $n*k$ new edges.

![nfa-re.pmg](nfa-re.png)

To go from a RE to an NFA you introduce states between each character in the RE
