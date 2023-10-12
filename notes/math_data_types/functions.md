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
* $\forall b\in B\ \exists a\in A \ \ (f(a)=b)$

A function is **bijective** if it is both injective and surjective.

### Exercise 1
Consider the following functions on the real numbers. 
For each function say if it is a total function or a partial function.
Also say if it is surjective or injective or both.
* $f(x)=x^2$  
* $g(x)=x^3$
* $h(x) = \sqrt{x}$


## Functions on subsets of a domain
We also can use $f:A\rightarrow B$ to define a function on subsets of $A$ to subsets of $B$ by
* $f_*(S) \ = \ \\{f(x)| x \in S\\}$

So $f_*:2^{A} \rightarrow 2^B$

Since it is usually clear by context whether we are referring to $f$ or $f_*$, we usually drop the
subscript and just write $f(S)$ for a subset $S$ of $A$ instead of $f_*(S)$.

We say that $f(S)$ is the **image** of $S$ under $f$, and if the domain of $f$ is $A$, then
we say that $f(A)$ is the **range** of $f$.

For example, if $f$ and $g$ are functions on $\mathbb{Z}$ defined by $f(x)=x+1$ and $g(x)=2x$,
and if $E$ is the set of even integers and $O$ is the set of odd integers$, then
* $g(\mathbb{Z}) = E$
* $f(E)=O$ and $f(O)=E$

## Inverse images
Let $f:A\rightarrow B$ be a function, and $S\subseteq B$ a subset of $B$, then we define the
inverse image of $S$ under $f$ to be

$f^{-1}(S) = \\{a \in A : \  f(a) \in S$

Note that $f$ is a function from the powerset of $B$ to the powerset of $A$.

$f:2^{B}\rightarrow 2^{A}$


### Exercise 2
* what is the range of the function $f(x)=2x+1$ defined on the integers $\mathbb{Z}$
* what is the range of $f$ on $\mathbb(R)$
* what is the image of the interval $[2,4]$ under $f$?
* what is the inverse image of the interval $[2,4]$ under $f$?

## Composition of functions
If $g:A\rightarrow B$ and $f:B \rightarrow C$ are functions, then their composition $f\circ g:A\rightarrow C$
is defined by first applying $g$ and then $f$:

$(f\circ g)(a) = f(g(a))$

That is it takes $a\in A$ and gets a $b=g(a)\in B$ and then applies $f$ to $b$ to get $c=f(b) =f(g(a))$.

$a \rightarrow g(a) \rightarrow f(g(a))$

For example, let
* $f(x) = x^2+2$
* $g(a,b) = a+b$

Then $g:\mathbb{R}^2 \rightarrow \mathbb{R}$ and $f:\mathbb{R} \rightarrow \mathbb{R}$ and the composition is 

$f(g(a,b)) = f(a+b) = (a+b)^2+2 = a^2 + 2ab + b^2 + 2$

### Exercise 3
Let $h(x) = (x^2+1, 2x)$ be a function from $\mathbb{R}$ to $\mathbb{R}^2$. Calculate the following functions:
* $g\circ h$
* $h\circ f$
* $g \circ h \circ f$

## Product of functions
Let $f:A\rightarrow C$ and $g:B\rightarrow D$ be functions, then $f\times g:A\times B \rightarrow C\times D$ is the function defined by

$(f\times g)(a,b) = (f(a), g(b))$

### Exercise 4
Let $j(x) = 2*x$ and $k(x)=x^2+1$, 
* what is the functions $j\times k$?
* What is $g\circ(j\times k)$?

### Exercise 5
Let $g:A\rightarrow B$ and $f:B\rightarrow C$ be functions
* Prove that if $g\circ f$ is surjective, then $g$ must be surjective.
* Prove that if $g\circ f$ is injective, then $f$ must be injective.
* Prove that $(f\circ g)^{-1} = (g^{-1})\circ (f^{-1})$
* Prove that $f(f^{-1}(S)) = S$ for every $S\subset C$ 



