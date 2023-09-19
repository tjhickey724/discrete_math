# Simplification of Predicate Calculus Formulas

One of the goals of this course is to show you how to use formal methods to prove theorems in First Order Logic.
We will use an extension of the Truth Tree method that we learned for Propositional Calculus. As before, the
first step will be to simplify.

For First Order Logic formulas, we will show how to move the negation operators past the quantifiers and
replace the operators $\oplus, \rightleftarrow, \rightarrow$ with $\vee$ and $\wedge$ in the same way we
do with Propositional Logic.

## Negating Quantifiers
There are two rules for moving negation inside a quantified expression:

$\neg \forall x F(x) \equiv \exists x \neg F(x)$

$\neg \exists x F(x) \equiv \forall x \neg F(x)$

Notice that if the domain $D$ of discourse is a finite set, e.g. $D=\{a,b,c\}$,
then universal quantification is equivalent to a conjunction:

$\forall x F(x)$  $\equiv$ $F(a) \wedge F(b) \wedge F(c)$

and existential quantification is equivalent to a disjunction:

$\exists x F(x)$  $\equiv$ $F(a) \vee F(b) \vee F(c)$

So in this case, the negated quantifier rules are the same as the DeMorgan rules:

$\neg \forall x F(x)$  

$\equiv$ $\neg ( F(a) \wedge F(b) \wedge F(c))$

$\equiv$ $\neg F(a) \vee \neg F(b) \vee \neg F(c))$

$\equiv$ $\exists x \neg F(x)$



## 
