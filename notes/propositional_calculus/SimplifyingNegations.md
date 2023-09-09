# Simplifying the negation of a formula

On this page we give some examples of simiplifying the negation of a formula
by using using the DeMorgan rules to move the negation symbols all the way in to the formula
so the only negations are those on primitive propositional symbols.

Being able to accurately perform these simplifications is important in proving properties of logical formulas!

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

You can test the equivalence of these with Truth Tables if you want.

## Example 2
Now let's simplify $\neg (P \rightarrow (Q \rightarrow P))$

First we replace the implications $A\rightarrow B$ with disjunctions $\neg A \vee B$:

$\neg (P \rightarrow (Q \rightarrow P)) \equiv \neg (P \rightarrow (\neg Q \vee P)) \equiv \neg (\neg P \vee (\neg Q \vee P))$

Using DeMorgan we get

$\neg (\neg P \vee (\neg Q \vee P)) \equiv \neg\neg P \wedge \neg(\neg Q \vee P)$

Next we apply DeMorgan again to get 

$\neg\neg P \wedge \neg(\neg Q \vee P) \equiv \neg\neg P \wedge \neg\neg Q \wedge \neg P$

Since double negation is the identity, $\neg\neg P\equiv P$, we get 

$\neg\neg P \wedge \neg\neg Q \wedge \neg P \equiv P \wedge Q \wedge \neg P$

but $P \wedge \neg P \equiv False$ and $False \wedge Q \equiv False$, so the entire formula
simplifes to False, and we have shown that

$\neg (P \rightarrow (Q \rightarrow P)) \equiv False$

In other words $$\neg (P \rightarrow (Q \rightarrow P)) $ is unsatisfiable, 
and by negating both sides we see also that

$P \rightarrow (Q \rightarrow P) \equiv True$

So $P\rightarrow (Q \rightarrow P)$ is a valid formula, i.e. a taugology.
