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

$\neg \exist x F(x) \equiv \forall x \neg F(x)$


