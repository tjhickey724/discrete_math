# Example of using the Tree Method in Predicate Calculus

Let's try to formally determine if the following argument is valid or not
by translating it into the predicate calculus and then using the Tree method.

Consider the following argument

* P1: if a is a close contact of b, then b is a close contact of a
* P2: every close contact of someone who tests positive is quarantined
* P3: everyone has a close contact who is a soccer player
* P4: no soccer players are in quarantine
---
Conclusion: No one has tested positive.

## Step 1: Determine the predicates

* $C(x,y)$ means x is a close contact of y
* $P(x)$ means x tests positive
* $S(x)$ means x is a soccer player
* $Q(x)$ means x is in quarantine
* $a$ is some person (we assume the domain is non-empty)


## Step 2: Translate the argument to predicate calculus
* P1: $\forall x \forall y (C(x,y) \rightarrow C(y,x)))$
* P2: $\forall x \forall y P(x)\wedge C(x,y) \rightarrow Q(y)$
* P3: $\forall x \exists y C(x,y)\wedge S(y)$
* P4: $\forall x S(x) \rightarrow \neg Q(x)$
* Conclusion: $\neg \exists x P(x)$

## Step 3: negate the conclusion and simplify the formulas

## Step 4: instantiate the formulas and try to close all branches


#
