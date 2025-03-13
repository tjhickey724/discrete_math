# F12: Sets - Syntax and Semantics 
## Skill definition
```
Ability to work with modern set notation.
In particular, the ability to perform calculations using
the union, intersection, and complement of sets.
```

What we are looking for in this skill is a basic understanding of the standard set notation.

A set is a collection of distinct elements.

Sets can be described using a list of items separated by commas inside curly braces, e.g.

$\\{ a, b, c\\}$

We use the notation

$x\in A$ 

to express the predicate that the element $x$ is in the set $A$.

Some common sets of numbers have their own symbols
* $\emptyset$ = the empty set = $\\{\\}$
* $\mathbb{N}$ = the natural numbers = $\\{0,1,2,\ldots \\}$
* $\mathbb{Z}$ = the integers = $\\{ \ldots, -2,-1,0,1,2,\ldots \\}$
* $\mathbb{Q}$ = the rational numbers
* $\mathbb{R}$ = the real numbers
* $\mathbb{C}$ = the complex numbers
* $\mathbb{F}_n = {0,1,\ldots,n-1}$ the natural numbers less than $n$
  We will also write this as ${\cal F}_n$

We can use a superscript '+' or '-' to indicate the positive or negative elements in the set
* $\mathbb{Z}^+$ = positive integers
* $\mathbb{R}^-$ = negative real numbers

## Set Comprehensions
Another way to express a set is to specify the set as a the elements x of another set S satisfying some relation P(x). Here is the notation

$\\{x \in S | P(x) \\}$ or $\\{x \in S : P(x) \\}$

the ":" or "|" can be read "such that" or "for"

* odds = $\\{ x\in \mathbb{Z} : \exists a\in \mathbb{Z} . (x = 2a+1)\\}$
  the set of all integers x such that x = 2a+1 for some integer a
* odds = $\\{ 2x+1 | x \in \mathbb{Z} \\}$
  the set of numbers of the form 2x+1 for all integers x

## Intervals
We use the following notation to represent intervals in the integers, rationals, or reals:

$[a,b] = \\{x : a\le x\le b]$

$[a,b) = \\{x : a\le x\lt b]$

$(a,b] = \\{x : a\lt x\le b]$

$(a,b) = \\{x : a\lt x\lt b]$

The bracket or parenthesis indicates that the endpoint is  or is not in the set.
Note we can write $\mathbb{F}_n$ as $[0,n)$ or $[0,n-1]$. For example, 
* $[2,5] = \\{2,3,4,5\\}$
* $[0,7) = \\{0,1,2,3,4,5,6\\}$

# Sample Problems 
Let $N=\\{0,1,2,\ldots\\}$ be the natural numbers, and let
$F_3 = \\{0,1,2\\}$

Each of the sets below contains a (small) finite number of elements. 
List the elements explicitly. For example, for 
$U = \\{x \in N: x < 5\\}$ then answer would be $U=\\{0,1,2,3,4\\}$.

1. List the elements of $A = \\{3x+1 : x\in N \wedge x\in [2,4]\\}$
2. List the elements of $B = P(F_3)$
3. List the elements of $C = \\{(a,S) \in F_2 \times P(F_2) : a\not\in S \\}$
4. List the elements of $C = \\{(n,S) \in F_3 \times P(F_2) : n \ne \vert S \vert \\}$


