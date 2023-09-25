# Example of using the Tree Method in Predicate Calculus

We'll give an example here of solving a "word problem" by converting it to
a formal argument in First Order Logic and then using formal methods to
determine if the argument is valid or not. 

Let's try to formally determine if the following argument is valid or not
by translating it into the predicate calculus and then using the Tree method.

Consider the following argument
* P1: if a is a close contact of b, then b is a close contact of a
* P2: every close contact of someone who tests positive is quarantined
* P3: everyone has a close contact who is a soccer player
* P4: no soccer players are in quarantine
---
* Conclusion: No one has tested positive.

You might first try to determine, informally, if this is a valid argument.
Suppose the domain is all students at the University and all of the premises are true,
does it follow that no students have tested positive? Why or why not?

Just because you find one interpretation that makes all of the premises true
and makes the conclusion true, doesn't show it is a valid argument. You need to
show that for any interpretation (with any non-empty domain), if the premises
are true then the conclusion will also be true!

---

## Step 1: Determine the predicates
To formalize this problem we first have to determine the First Order Language
we will translate this argument in to. There are many ways to do this, but
here is one way.

* $C(x,y)$ means x is a close contact of y
* $P(x)$ means x tests positive
* $S(x)$ means x is a soccer player
* $Q(x)$ means x is in quarantine
* $a$ is some person (we assume the domain is non-empty)

---

## Step 2: Translate the argument to predicate calculus
The next step is to translate the argument into this first order language.
There are many ways to translate each formula into the predicate calculus,
but ideally any two different translations will be logically equivalent
unless the statement is naturally ambiguous.

* P1: $\forall x \forall y (C(x,y) \rightarrow C(y,x)))$
* P2: $\forall x \forall y P(x)\wedge C(x,y) \rightarrow Q(y)$
* P3: $\forall x \exists y C(x,y)\wedge S(y)$
* P4: $\forall x S(x) \rightarrow \neg Q(x)$
* Conclusion: $\neg \exists x P(x)$

## Step 3: negate the conclusion and simplify the formulas
Let's apply the simplification rules to the premises and the negation of the conclusion
to get a set of universally quantified formulas containing only $\wedge$ and $\vee$
and predicates or their negations.

* P1: $\forall x \forall y (\neg C(x,y) \vee C(y,x)))$
* P2: $\forall x \forall y \neg P(x)\vee \neggC(x,y) \vee Q(y)$
* P3: $\forall x C(x,f(x))\wedge S(f(x)))$, where $f(x)$ is a soccer player who is a close contact of x
* P4: $\forall x \neg S(x) \vee \neg Q(x)$
* Negation of Conclusion: $\exists x P(x) \equiv  P(a)$, where $a$ is the person who tested positive

Lets say, explicitly, what the skolem functions are for the interpretation 
where the domain is students at the University.


## Step 4: instantiate the formulas and try to close all branches
If we can close all of the branches using the Tree Method rules, then
we know that there is no interpretation that makes all of the premises
true and makes the conclusion false, so the conclusion must always be
true for any interpretation which makes all of the premises true!

If we can't close all of the branches, then applying the rules will generate
an infinitely tall tree, and that tree must have an infinite branch with 
no contradictions, and the predicates on that branch provide a model.

This is a problem though as it is non-trivial to determine whether the
the tree method is going to eventually stop or whether it continues forever.
In fact, we can show that there is no computer program that can determine
if a particular tree method problem will continue forever. 

If you suspect that the branches won't close though you can look for a 
counterexample, that is an interpretation which makes the premises true
and the conclusion false!


#
