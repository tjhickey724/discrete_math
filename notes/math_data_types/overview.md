# Overview of Mathematical Data Types

Discrete Math deals with a number of Mathematical Data Types

The ones we will discuss here are:
* sets
* sequences
* functions
* relations

## Sets
A set is a collection of distinct elements.

Sets can be described using a list of items separated by commas inside curly braces, e.g.
* $\{ a, b, c\}$

We use the notation

$x\in A$ 

to express the predicate that the element $x$ is in the set $A$.

Some common sets of numbers have their own symbols
* $\emptyset$ = the empty set = $\{\}$
* $\mathbb{N}$ = the natural numbers = $\{0,1,2,\ldots \}$
* $\mathbb{Z}$ = the integers = $\{ \ldots, -2,-1,0,1,2,\ldots \}$
* $\mathbb{Q}$ = the rational numbers
* $\mathbb{R}$ = the real numbers
* $\mathbb{C}$ = the complex numbers

We can use a superscript '+' or '-' to indicate the positive or negative elements in the set
* $\mathbb{Z}^+$ = positive integers
* $\mathbb{R}^-$ = negative real numbers

## Set Comprehensions
Another way to express a set is to specify the set as a the elements of another set satisfying some relation, e.g.

* odds = $\\{ x\in \mathbb{Z} : \exists a\in \mathbb{Z} . (x = 2a+1)\\}$
