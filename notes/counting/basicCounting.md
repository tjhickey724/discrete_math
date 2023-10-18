# Basic Counting Technqiues
Here we introduce the simplest (and yet still powerful) counting techniques.

Recall that if $A$ is a finite set then we use the notation $\vert A \vert$ to denote the size
of the set.

---

# The multiplication principle:
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


---


# The Addition Principle
_The size of a disjoint unions of sets is the sum of their sizes_

Suppose $A$ and $B$ are sets, then
* $\vert A \cup B \vert = \vert A \vert\ \cup\  \vert B \vert$

and if $A_i$ are disjoint sets, then
* $\vert \bigcup_\limits{i=1}^n A_i\vert \ = \ \bigcup_\limits{i=1}^n \vert A_i\vert$

This follows directly from what it means for two sets to be disjoint.

### Applications
**Passwords**
Suppose that on a particular system a valid password must have 6,7,or 8 symbols
and the first must be a letter while the rest can be letters or digits. What is the size
of the set $V$ of all valid passwords?

If we let $L$ be the set of 26 letters and $D$ the set of 10 digits, and $S$ the set of 36 letters or digits.
Then we can use the product rule to calculate the number of passwords of length 6 (V6), length 7 (V7) and length 8 (V8).
Since these are disjoint sets, we add their sizes to get the size of $V$.

* $\vert V6 \vert = \vert L \vert * \vert S \vert^5 = 26*36^5$
* $\vert V7 \vert = \vert L \vert * \vert S \vert^6= 26*36^6$
* $\vert V8 \vert = \vert L \vert * \vert S \vert^7= 26*36^7$
* $\vert V \vert = \vert V6\vert + \vert V7\vert + \vert V8\vert = 26 * 36^5 +26 * 36^6 +26 * 36^7$

So the total number of valid passwords is $26 * 36^5 +26 * 36^6 +26 * 36^7$.

---

# Principle of Inclusion and Exclusion
Let $A$ and $B$ be two sets which are not necessarily disjoint, then

$\vert A \cup B \vert = \vert A \vert + \vert B \vert - \vert A \cap B \vert$

To see why, observe that every element of $A \cap B$ will be counted twice, once in $\vert A\vert$ and once in $\vert B \vert$
so subtracting $\vert A \cap B \vert$ removes that double counting.

### Applications
How many integers in the range [0,100] are divisible by 3 or by 5?

Let $A_n$ be the set of numbers in [1,100] which are divible by $n$.
We want to know the size of $A = A_3\cup A_5$

Observe that $\vert A_n\vert = 100//n$  where $a//b$ means divide a by b and throw away the remainder.
(Why?)

So $\vert A = \vert A_3\vert + \vert A_5\vert - \vert A_3\cap A_5\vert$

but $A_3\cap A_5$ is the numbers divisible by 3 and 5, i.e. by 15, so 

* $\vert A_3\vert =100//3 = 33$
* $\vert A_5\vert =100//5 = 20$
* $\vert A_3\cap A_5\vert = \vert A_{15}\vert = 100//15 = 6$
* $\vert A \vert = 33 + 20 - 6 = 53-6 = 47$



So $\vert A \vert = 

and notice that $A_{15} = A_3 \cap A_5$
