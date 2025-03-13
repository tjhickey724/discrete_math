# Basic Counting Technqiues
Here we introduce the simplest (and yet still powerful) counting techniques.

Recall that if $A$ is a finite set then we use the notation $\vert A \vert$ to denote the size
of the set.



---

# The Multiplication Principle:
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

**License Plates**
Current Massachusetts license plates (as of 2023) have the form D LLL DD
where D is a digit and L is a letter. How many different license plates can there be?

If we let $L$ be set of 26 letters and $D$ be the set of 10 digits, then each license plate
is an element of $D\times L^3\times D^2$ and the size of this set is

$\vert D\times L^3\times D^2\vert = \vert D \vert^3 * \vert L \vert^3 = 1000*26^3 = 17,576,000$


---


# The Addition Principle
_The size of a disjoint unions of sets is the sum of their sizes_

Suppose $A$ and $B$ are disjoint sets, then
* $\vert A \cup B \vert = \vert A \vert\ +\  \vert B \vert$

and if $A_i$ are disjoint sets, then
* $\vert \bigcup_\limits{i=1}^n A_i\vert \ = \ \sum_\limits{i=1}^n \vert A_i\vert$

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

Similarly if $A,B,C$ are sets 

$\vert A \cup B \cup C \vert = \vert A \vert + \vert B \vert +\vert C\vert - \vert A \cap B \vert - \vert A \cap C \vert - \vert B \cap C \vert+\vert A \cap B \cap C\vert$

### Applications

**FizzBuzz**
How many integers in the range [1,100] are divisible by 3 or by 5? This is the basis of the FizzBuzz
challenge where you count from 1 to 100 but say fizz for numbers divisible by 3 and buzz for numbers divisible by 5, e.g. you can play this with a group of friends taking turns (but its not so fun for one person if the number of friends is 3 or 5)

1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16 17 fizz 19 buzz ...

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

Now, find the number of integers in [1,100] which are not divisible by 2, 3, or 5.
To do this, we first find the number which are divisible by 2,3, or 5 and then subtract that from 100.
Using the inclusion exclusion principle, let $A= A_2$, $B=A_3$ and $C=A_5$ then

* $\vert A_2 \vert = 50$
* $\vert A_3\vert =33$
* $\vert A_5 \vert = 20$
* $\vert A_2\cap A_3 \vert = \vert A_6\vert = 16$
* $\vert A_2\cap A_5 \vert = \vert A_{10}\vert = 10$
* $\vert A_3\cap A_5 \vert = \vert A_{15}\vert = 6$
* $\vert A_2\cap A_3 \cap A_5 \vert = \vert A_{30}\vert = 3$

so

$\vert A \cup B \cup C \vert = \vert A \vert + \vert B \vert +\vert C\vert - \vert A \cap B \vert - \vert A \cap C \vert - \vert B \cap C \vert+\vert A \cap B \cap C\vert$

$= 50 +33 +20 - (16+10+6) + 3 = 103 - 32 + 3= 71+3=74$

So the number of integers in the range [1,100] which are divisible by 2,3, or 5 is 74.

So the number of integers in the interval [1,100] which are not divisible by 2,3, or 5,
is 100-74 = 26.

---

# Counting Subsets
Another useful rule is that the number of subsets $S$ of a set $A$ of size $n$ is $2^n$.
We can see this is true by associating each subset $S$ of $A= \\{a_1,a_2,a_3,\ldots,a_n\\}$ with a binary sequence $(b_1,b_2,\ldots,b_n)$ of length $n$ where 

$$
b_i=
\left\\{
\begin{array}{ll}
1 &\text{if }g_i\in S \\ 
0 &\text{if }g_i\not\in S
\end{array} 
\right.
$$

Since there are $2^n$ binary sequences of length $n$ there must then be $2^n$ subsets $S$ of $A$.

We are using the bijection principle here with $f$ mapping length n bit strings one-one and onto the subsets of an n element set.





---

# The Bijection principle

If $f:A\rightarrow B$ is a bijection, where $A$ and $B$ are finite sets, then $A$ and $B$ have the same size, that is $\vert A\vert = \vert B \vert$.

### Applications.
We'll show how to use the Bijection Principle to count the number of functions between two sets.

**Theorem.** Let $T_{A,B}$ be the set of total functions from $A$ to $B$,
then 
* $\vert T_{A,B}\vert = \vert B \vert ^{\vert A\vert}$

**Proof:** 
Let $A=\\{a_1,\ldots,a_r\\}$ be a set with $r$ elements, 
and let $B=\\{b_1,\ldots,b_s\\}$ be a set with $s$ elements.
We will define a bijection 
* $\phi: T_{A,B} \rightarrow B^{\vert A\vert}$

and this will prove our Theorem since the size of $B^r$ is $\vert B\vert^r$.

The bijection takes a length $r$ sequence $s=(s_1,\ldots,s_r)$ of elements $s_i$ of B,
and associates it to a function $f_s:A\rightarrow B$ by
* $f_s(a_i) = s_i$

This is clearly a 1-1 total function. To see that it is onto, we need to show that if
$g:A\rightarrow B$ is any total function, then there is a sequence $s$ with $g=f_s$.
This is easy to do, let $s = (g(a_1),\ldots,g(a_r))$ and by definition of $f_s$ we have
* $f_s(a_i) = s_i = g(a_i)$

**QED**

---


