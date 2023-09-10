# Symbolic proofs

One of the main goals of this course is the help you learn how to write clear and convincing proofs of mathematical theorems. 

In this section, we put this into a formalism and we will show how to construct formal, symbolic proofs.

We will teach you some algorithms for constructing formal proofs of theorems in Propositional Logic (and later 
for theorems in the Predicate Calculus).

First some definitions.

An ___argument___ is a set of statements, one of which is the ___conclusion___ 
(usually the last) and the rest are the ___premises___

An argument is ___valid___ if the conclusion is true whenever the premises are true;
otherwise it is invalid.

An argument is invalid if there is an interpretation of the propositional variables which makes
all of the premises True and makes the conclusion False. Such an interpretation is called a
counterexample to the argument.

## Example 1
Here is an example of a valid argument
```
P
P implies Q
-----------
Q
```
where the premises are the statements above the dashed line and the conclusion is the statement after the dashed line.
This argument states that whenever P and P implies Q are true, then Q must also be true.

One way to prove this is to create Truth Tables for P and P implies Q and Q and to observe that for all interpretation
that make P and P implies Q true, they also make Q true. 

The Truth Table method will work to prove the validity of any argument, or to find a counter example, but
it could involve evaluating the formulas for $2^n$ interpretations if the argument contains $n$ propositional symbols.

We will present another method, called Truth Trees, which can always prove an argument is valid or find a counterexample 
and sometimes is much faster that the Truth Table method.

