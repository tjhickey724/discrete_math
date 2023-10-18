# Basic Counting Technqiues
Here we introduce the simplest (and yet still powerful) counting techniques.

Recall that if $A$ is a finite set then we use the notation $\vert A \vert$ to denote the size
of the set.

## The multiplication principle:
_The size of a product of sets, is the product of their sizes_

Suppose $A$ and $B$ are sets, then
* $\vert A \times B \vert = \vert A \vert\ *\  \vert B \vert$

and
* $\vert A^n \vert \ = \ \vert A\vert^n$

and more generally, if $\\{A_i | 1\le i\le n\\}$ is a finite collection of sets, then
* $\vert \prod_\limits{i=1}^n A_i\vert \ = \ \prod_\limits{i=1}^n \vert A_i\vert$

### Applications

**How many binary sequences of length $n$ are there?**

If we let $B=\\{0,1\\}$ be the set of two bits, then $B^n$ is the set of binary sequences of length $n$,
and by the multiplication principle, $\vert B^n\vert \  = \ \vert B\vert^n \  = \ 2^n$. So there are $2^n$
binary sequences of length $n$

** License Plates**
Current Massachusetts license plates (as of 2023) have the form D LLL DD
where D is a digit and L is a letter. How many different license plates can there be?

If we let $L$ is tbe set of 26 letters and $D$ be the set of 10 digits, then each license plate
is an element of $D\times L^3\times D^2$ and the size of this set is

$\vert D\times L^3\times D^2\vert = \vert D \vert^3 * \vert L \vert^3 = 1000*26^3 = 17,576,000




## The size of a disjoint unions of sets is the sum of their sizes
Suppose $A$ and $B$ are sets, then
* $\vert A \cup B \vert = \vert A \vert\ \cup\  \vert B \vert$

and if $A_i$ are disjoint sets, then
* $\vert \bigcup_\limits{i=1}^n A_i\vert \ = \ \bigcup_\limits{i=1}^n \vert A_i\vert$

This follows directly from what it means for two sets to be disjoint.


