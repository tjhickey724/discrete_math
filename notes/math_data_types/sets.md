# Sets
A set is a collection of distinct elements.

Sets can be described using a list of items separated by commas inside curly braces, e.g.
* $\{ a, b, c\}$

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

We can use a superscript '+' or '-' to indicate the positive or negative elements in the set
* $\mathbb{Z}^+$ = positive integers
* $\mathbb{R}^-$ = negative real numbers

# Set Comprehensions
Another way to express a set is to specify the set as a the elements x of another set S satisfying some relation P(x). Here is the notation
$\\{x \in S | P(x) \\}$ or $\\{x \in S : P(x) \\}$
the ":" or "|" can be read "such that" or "for"

* odds = $\\{ x\in \mathbb{Z} : \exists a\in \mathbb{Z} . (x = 2a+1)\\}$
  the set of all integers x such that x = 2a+1 for some integer a
* odds = $\\{ 2x+1 | x \in \mathbb{Z} \\}$
  the set of numbers of the form 2x+1 for all integers x

## Relations on sets
* $A\subseteq B \equiv \forall x.  (x\in A) \rightarrow (x\in B)$
* $A\subset B \equiv A\ne B \wedge \forall x.  (x\in A) \rightarrow (x\in B)$

## Set Operations
The fundamental operations on sets $A$ and $B$ are
* union -  
  $A\cup B = \\{x | (x\in A) \vee (x\in B) \\}$
* intersection -  
  $A\cap B = \\{x | (x\in A) \wedge (x\in B) \\}$
* difference -  
  $A-B = \\{x | (x\in A) \wedge \neg (x\in B) \\}$
* complement -  
  $\bar{A} = \\{x\in \cal{U} | \neg(x\in A) \\}$  
  where $\cal{U}$ is some universal domain that contains $A$ and $B$.
  and is usually clear by context. We also write it using the superscript "c" -
  $A^c = \bar{A}$
* powerset -  
  ${\cal P}(A)$ = the set of all subsets of A including the empty set $\emptyset$ and the set $A$ itself.
  We sometimes write the powerset as $2^{A}$ since if $A$ has $n$ elements then ${\cal P}(A)$ has $2^n$ elements.

## Exercise 1
Let 
* $A=\\{1,2,3,4,5,6\\}$,
* $B=\\{5,6,7,8,9,0\\}$
* $C=\\{1,3,5,7,9\\}$,
* ${\cal U}=\\{0,1,2,3,4,5,6,7,8,9\\}$

What is
* $A\cup B$
* $A\cap B$
* $\bar{C}$
* $A\cap C$
* $A\cap B$
* $C \cap (A\cup B)$
* $C \cup (A \cap B)$

## Exercise 2
Describe the following sets in English and list a few of their elements, if they aren't empty
1. A = $\\{x\in \mathbb{Z} | \exists y\in \mathbb{Z} \ (x=y^2)\\}$
2. B = $\\{x \in \mathbb{Z} | \sqrt{x}\in \mathbb{Q}\\}$
3. C = $\\{x \in \mathbb{R} | x^2 \lt 9 \\}$
4. D = $\\{x \in \mathbb{N} | 10 - x \in \mathbb{N} \\}$
5. Is $A \subseteq B$?
6. What would it mean if $A=B$? (Is it true?)
7. What is $\bar{C} \cap D$?
8. Let $E = \\{0,1,2\\}$, what is the powerset ${\cal P}(E)$ of $E$. Write down its elements.
   
