# Simplifying the negation of a formula

On this page we give some examples of simiplifying the negation of a formula
by using using the DeMorgan rules to move the negation symbols all the way in to the formula
so the only negations are those on primitive propositional symbols.

## Example 1
Let's simplify $\neg(P\wedge Q \rightarrow R)$
The first step is to replace the implication $A\rightarrow B$ with an equivalent disjunction $\neg A \vee B$, so

$\neg(P\wedge Q \rightarrow R) \equiv \neg(\neg(P\wedge Q) \vee R)$

then we apply DeMorgan to either the outer disjunction or the inner conjuction. Let simpify the inner negation first:

$\neg(\neg(P\wedge Q) \vee R) \equiv \neg ( \neg P \vee \neg Q \vee R)$

Now we can simplify the outer negation:

$\neg ( \neg P \vee \neg Q \vee R) \equiv P \wedge Q \wedge \neg R$

Notice were using a slight generalization of the DeMorgan Law wich states that the negation of a disjunction 
is the conjunction of negations of its elements. We have shown than

$\neg(P\wedge Q \rightarrow R) \equiv  P \wedge Q \wedge \neg R$

## Example 2



