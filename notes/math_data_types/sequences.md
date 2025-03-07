# Sequences

A sequence is a list of elements from a set.
We will write them inside parentheses, separated by commas, as so

* (2,7,1,8,2,8)  is a sequence of six digits
* (apple, cherry, banana) is a sequence of 3 strings of characters (or three fruits)
* $(1,3,5,7,9,11,13,\ldots)$  = the infinite sequence of odd numbers
* $(1,4,1,4,2,\ldots)$ = the infinite sequence of digits of the square root of 2

## Products of Sets
The product of sets $S_1,\ldots,S_n$ is written
* $S_1\times S_2 \times \ldots \times S_n$

and is defined as the set of all length n sequences $(s_1,s_2,\ldots,s_n)$ with $s_i\in S_i$ for each $i$.

The product of $S$ with itself $n$ times is written $S^n$

For example if $A=\\{0,1\\}$ then the elements of $A^2$ are
* $\\{(0,0),(0,1),(1,0),(1,1)\\}$

if $B=\\{T,F\\}$ then the elements of $A\times B$ are
* $\\{(0,F),(0,T),(1,F),(1,T)\\}$

## Exercise 1
1. Describe in English the set $A = \mathbb{N}\times \\{0,1\\}$ and list a few members of this set
2. Let $B=\\{0,1\\}$, list the elements of the set $C$ defined by $C=B\\times{\cal P}(B)$
    where ${\cal P}(B) = 2^B$ is the powerset of B.
3. List the elements of the set $D = \\{(a,s)\in C | a \in s\\}$

## Sizes of product sets
We will use the following notation to represent the size of a set $S$, i.e. the number of elements it contains:
* $\vert S \vert$

---

**Theorem.** Let $A$ and $B$ be any finite sets, then
* $\vert A\times B\vert = \vert A \vert * \vert B \vert$

**Proof:** To see that  $\vert A\times B\vert = \vert A \vert * \vert B \vert$, we can
create a table of size $\vert A \vert * \vert B \vert$ whose elements are precisely the
elements of $A\times B$. Let the rows be indexed by $A$ and the columns by $B$, and the
entries in row "a" and column "b", be $(a,b)$. 

|| b1 | b2 | ... | bs |
|--- | ---  | --- | --- | --- |
| a1 | (a1,b1) | (a1,b2) | ... | (a1,bs) |
| a2 | (a2,b1) | (a2,b2) | ... | (a2,bs) |
| ... | ... | ... |  ...| ... |
| ar | (ar,b1) | (ar,b2) |  ... | (ar,bs) |


This table will contain all elements of $A\times B$
and since a table with $n$ rows and $m$ columns has $n * m$ entries. Q.E.D

--- 
**Corollary.** Let $A_1,A_2,\ldots,A_n$ be finite sets, then

$\vert A_1\times\ldots\times A_n\vert = \prod_\limits{i=1}^n\vert A_i \vert$

**Proof:** 
We will prove this by contradiction using the Well-Ordering principle.
Suppose it is not true and let $n$ be the smallest integer for which it is not true.
Observe that it is clearly true for $n=2$ as it says 

$\vert A_1\times A_2\vert = \vert A_1\vert * \vert A_2\vert$

and it is trivially true for $n=1$ as it says $\vert A_1 \vert = \vert A_1 \vert$
So we can assume that $n\gt 2$.

Let 

$S =\prod_\limits{i=1}^{n-1} A_i$

then 

$\prod_\limits{i=1}^n\vert A_i \vert = S \times A_n$

Also, since $(n-1) \lt n$, we know by our assumption that the Corollary holds, so

$\vert S \vert = \vert A_1\times\ldots\times A_{n-1}\vert = \prod_\limits{i=1}^{n-1}\vert A_i \vert$

So by the Theorem

$\vert A_1\times\ldots\times A_n\vert = \vert S \times A_n \vert
   = \prod_\limits{i=1}^{n-1}\vert A_i \vert  * \vert A_n \vert = \prod_\limits{i=1}^n\vert A_i \vert$

but this shows that that the Corollary holds for $n$ 
which contradicts our assumption that $n$ was the smallest number for which it holds. 
Hence the Corollary must hold for all $n$. QED.

---

**Theorem.** Let $A$ be a finite set and let ${\cal P}(A)$ be the power set of $A$, i.e. the set of all subsets of $A$, then
* $\vert {\cal P}(A)\vert = 2^{\vert A \vert }$

**Proof:** We will show that there is a one-to-one correspondence $b \leftrightarrow S_b$
between binary numbers of size $n$ and subsets of $A$, where $n$ is the size of $A$. 
Let $a_1,\ldots,a_n$ be the elements of $A$ and let $b$ be a binary number of length $n$,
then $b$ is a sequence of $n$ bits $(b_1,b_2,\ldots,b_n)$ where each $b_i \in B=\\{0,1\\}$.
Let $S_b$ be the set 
* $S_b = \\{a_i | 1\le i\le n \wedge b_i=1\\}$.
Likewise if $S$ is an subset of $A$ we can define
* $b_S = (b_1,b_2,\ldots,b_n)$ where $b_i=1 \leftrightarrow a_i\in S$

For example let $A=\\{a_1,a_2,a_3\\}$, then here is the correspondence

|b | Sb |
| --- | --- |
| 000 | {} |
| 001 | {a3} |
| 010 | {a2} |
| 011 | {a2,a3} |
| 100 | {a1} |
| 101 | {a1,a3} |
| 110 | {a1,a2} |
| 111 | {a1,a2,a3} |


This show that each binary number $b$ can be associated to a unique subset $S_b$
and each subset $S$ is $S_b$ for some binary number $b$. So the number of subsets of $A$
is equal to the number of binary numbers of length $n$ which is $2^n$.  
QED.

---

**Exercise 1**
Recall that ${\cal F}_n = \\{0,1,\ldots,n-1\\}$
Calculate the sizes of the following sets, and write down a few of their elements.
1. ${\cal F}_2^3$
2. ${\cal F}_3 \times {\cal F}_5$
3. ${\cal P}({\cal F}_3)$
4. ${\cal F}_3\times {\cal P}({\cal F}_2)$
5. ${\cal P}({\cal F}_3)^2$
6. ${\cal P}({\cal P}({\cal F}_2))$










