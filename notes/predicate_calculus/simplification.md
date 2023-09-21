# Simplification of Predicate Calculus Formulas

One of the goals of this course is to show you how to use formal methods to prove theorems in First Order Logic.
We will use an extension of the Truth Tree method that we learned for Propositional Calculus. As before, the
first step will be to simplify.

For First Order Logic formulas, we will show how to move the negation operators past the quantifiers and
replace the operators $\oplus, \leftrightarrow, \rightarrow$ with $\vee$ and $\wedge$ in the same way we
do with Propositional Logic.

## Negating Quantifiers: DeMorgan rules for First Order Logic
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



## Renaming Quantifed variables
Another important simplification is to make sure that each quantifier has its own unique variable so there is no
confusion. Consider the formula

$\forall x \forall y  P(x,y) \rightarrow \exists x Q(x,y)$

The $x$ that appears in $Q(x,y)$ is bound by the existential quantifier and so it isn't the same $x$ as in $P(x,y)$.

To remove this confusion, it is better just to pick a new variable for the existential quantifier and replace all of its bound
instances with that new variable. This gives us the following:

$\forall x \forall y  P(x,y) \rightarrow \exists z Q(z,y)$

which is much easier to understand.

### Step 1 of Simplification: replace operators by disjunctions and conjunctions
The first step is to rename any quantified variables which appear in 2 or more quantifiers. Then we use the usual rules
to replace all operators with $\vee$ or $\wedge$

$A \rightarrow B \equiv \neg A \vee B$

$A \oplus B \equiv A\wedge \neg B \vee \neg A \wedge B$

$A \leftrightarrow B \equiv A\wedge B \vee \neg A \wedge \neg B$

### Step 2 move negation inwards
Next we use the DeMorgan rules to move the negations all the way in so they only appear in front of predicates

$\neg (A \wedge B) \equiv \neg A \vee \neg B)$

$\neg (A \vee B) \equiv (\neg A \wedge \neg B)$

$\neg \forall x F(x) \equiv \exists x \neg F(x)$

$\neg \exists x F(x) \equiv \forall x \neg F(x)$


### Step 3: Skolemization
The last step is to introduce new function symbols for each existential quantifier.

If there are no universal quantifier "in front" of the existential quantifier, then we our formula looks like:

$\exists x P(x)$

and if this is true, then it means there is some element $x$ in the domain which makes $P(x)$ true. So we can
pick such an element and assign it to a new constant symbol, say $a$, and replace this formula with

$P(a)$

If we have an interpretation which makes the original formula $\exists x P(x)$ true, then we can extend that interpretation to give a value
for $a$ which makes $P(a)$ true.

It gets a little trickier if the existential quantifier has one or more universal quantifiers "above" it.

The idea is to think about the formula

$\forall x \exists z P(x,z)$

what this means is that for each $x$ in the domain $D$ we can find a $z$ in the domain $D$ such that $P(x,z)$ is true.
That means we can define a function $f$ on $D$ by letting $f(x)=z$, so we have

$\forall x \exists z P(x,z) \equiv \forall x P(x,f(x))$

and if there are multiple universal quantifers above the existential quantifer, then we include each of those universally
quantified variables in the function, e.g.

$\forall x \forall y \forall z \exists w P(x,y,z,w) \equiv \forall x \forall y \forall z P(x,y,z,g(x,y,z))$

We need a new function name for each quantifier we remove..

If we are given an interpretation for the formula in a first order language, 
this shows us how extend that intepretation to a new language containing the new function symbols. 
So the original formula had an interpretation that makes it true if and only if the new skolemized formula does.

### Step 4: move the quantifers to the front
Since all of the quantifed variables are unique, and we only have universal quantifiers, we can now move them all to the front.
This is called "prenex" form.

# Examples
Let's try this out!

## Example 1: Simplify the following
Simplify: $\forall x \forall y ( P(x,y) \rightarrow \exists x Q(x,y) ) $

$\forall x \forall y ( P(x,y) \rightarrow \exists x Q(x,y) ) $, first we rename the $\exists x$ variable

$\forall x \forall y ( P(x,y) \rightarrow \exists z Q(z,y) ) $, then we replace the implication with a $\vee$

$\forall x \forall y ( \neg P(x,y) \vee \exists z Q(z,y))$, then we introduce a skolem function f(x,y) for z

$\forall x \forall y ( \neg P(x,y) \vee Q(f(x,y),y))$, and we are done since the quantifiers are already at the front


## Example 2: Simplify the following: 
Simplify: $\forall x( (\forall y  P(x,y)) \rightarrow \exists y Q(x,y) )) $

$\forall x( (\forall y  P(x,y)) \rightarrow \exists y Q(x,y) )) $, first we rename the $\exists y$

$\forall x ((\forall y  P(x,y)) \rightarrow \exists z Q(x,z) ) )$, then we replace the implication with a disjunction

$\forall x( \neg (\forall y  P(x,y)) \vee \exists z Q(x,z) )) $, then we apply DeMorgan's rule

$\forall x ((\exists y  \neg P(x,y)) \vee \exists z Q(x,z) )) $, then we introduce the Skolem functions to remove the $\exists y$ and $\exists z$

$\forall x (\neg P(x,f(x)) \vee Q(x,g(x)))$ and we are done!

Notice how the $\forall y$ became a $\exists y$ after we removed the implication and applied DeMorgan's rules



