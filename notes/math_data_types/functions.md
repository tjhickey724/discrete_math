# Functions
A function $f$ is an associations of elements in one set $A$ called the domain of f to elements in another set $B$ called the codomain of f
and is written:

$f: A \rightarrow  B$

The element $b$ of $B$ that a function $f$ associates to an element $a$ of $A$ is denoted $f(a)$.

## Basic Definitions

Functions can be defined in many ways. For example,
1. By listing its values on domain elements, e.g. $f({\rm T})=1, f({\rm F})=0$
2. By giving an expression to evaluate $f(x) = x + (1/x)$
3. By explaining the association in words $f(n)$ is the $n$ prime number, for natural numbers $n\gt 0$
4. By giving a menu style definition

$$
f(p)=
\left\\{
\begin{array}{ll}
p &\text{if }p\gt 0 \\ 
-p &\text{otherwise}.
\end{array} 
\right.
$$

A function is a **total function** if it assigns a value to every element of its domain, otherwise it is a **partial function**.

For example the function $f:\mathbb{R} \rightarrow \mathbb{R}$ is defined by $f(x)=\sqrt{x}$, then $f$ is not defined for negative
numbers $x$ and so is a partial function, but $g(x) = x^2$ is a total function.

A function is **injective** if no two elements of $A$ get mapped to the same element of $B$, that is
* $\forall a_1 \forall a_2 (f(a_1)=f(a_2)) \rightarrow (a_1=a_2)$

A function is **surjective** if for every $b$ in $B$ there is an $a$ in $A$ with $f(a)=b$.
* $\forall b\in B \exists a\in A (f(a)=b$

A function is **bijective** if it is both injective and surjective.

## Exercise 1
Consider the following functions on the real numbers. 
For each function say if it is a total function or a partial function.
Also say if it is surjective or injective or both.
* $f(x)=x^2$  
* $g(x)=x^3$
* $h(x) = \sqrt(x)$

## Functions on subsets of a domain
We also can use $f:A\rightarrow B$ to define a function on subsets of $A$ to subsets of $B$ by
* $f(S) \ \\{f(x)| x \in S\\}$

We say that $f(S)$ is the image of $S$ under $f$, and if the domain of $f$ is $A$, then
we say that $f(A)$ is the range of $f$.

For example, if $f$ and $g$ are functions on $\mathbb{Z}$ defined by $f(x)=x+1$ and $g(x)=2x$,
and if $E$ is the set of even integers and $O$ is the set of odd integers$, then
* $g(\mathbb{Z}) = E$
* $f(E)=O$ and $f(O)=E$

## Exercise 2
Describe the 


