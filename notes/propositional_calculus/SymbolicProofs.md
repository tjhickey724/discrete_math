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
Here is an example of a valid argument (which is called ___modus ponens___)
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

Use the Truth Table method to show that the following is a valid argument:
```
P implies R
Q impiles R
P or Q
------------
R
```
This is the rule for dividing a problem into cases.  If you can prove that P or Q has to be true,
and that if P is true then R is true,   and if Q is true then R is true.  Then you can conclude that R is true.

The Truth Table method will work to prove the validity of any argument, or to find a counter example, but
it could involve evaluating the formulas for $2^n$ interpretations if the argument contains $n$ propositional symbols.

We will present another method, called Truth Trees, which can always prove an argument is valid or find a counterexample 
and sometimes is much faster that the Truth Table method.

# Example 2
Another way to prove validity is to apply "inference rules" to the premises to find other statements that are true, and
to continue this process, until we can infer the conclusion.  Once we have proven that an argument is valid, we can
use it an an inference rule.

```
P implies Q
Q implies R
P
-----------
R
```
to prove this argument is valid, we can apply modus ponens to infer that Q is true from P implies Q and P.

```
1.  P implies Q
2.  Q implies R
3.  P
4.  Q   by modus ponens on 1 and 3
5.  R   by modus ponens on 4 and 2
```
and we have shown that R is true whenever statements 1,2,3 are true. We can now use this rule
as an inference rule. 


