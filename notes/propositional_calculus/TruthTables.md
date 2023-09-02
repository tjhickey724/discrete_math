# Truth Tables

A Truth Table is a way of determining the value of a Propositional formula
for all possible values for the variables in the formula. 

Here are the Truth Tables for the standard operators

## negation: not(P)

| $P$ | $\neg P$ |
| --- | --- |
| T | F |
| F | T |

## disjunction: P or Q

| $P$ | $Q$ | $P\vee Q$ |
| --- | --- | --- |
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

## conjunction: P and Q

| $P$ | $Q$ | $P\wedge Q$ |
| --- | --- | --- |
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

## implication: P IMPLIES Q

| $P$ | $Q$ | $P\rightarrow Q$ |
| --- | --- | --- |
| T | T | T |
| T | F | T |
| F | T | F |
| F | F | T |

## equivalence: P iff Q

| $P$ | $Q$ | $P\leftrightarrow Q$ |
| --- | --- | --- |
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

## exclusive or: P xor Q

| $P$ | $Q$ | $P \oplus Q$ |
| --- | --- | --- |
| T | T | F |
| T | F | T |
| F | T | T |
| F | F | F |

# Truth Tables for expressions
To create the truth table for an expression you need to create a table 
with a column for each variable and a column for each subexpression (i.e. operator)
e.g.

## Truth table for $\neg (P \wedge Q)$

| $P$ | $Q$ |  $P \wedge Q$ | $\neg (P \wedge Q)$  |
| --- | --- | --- | --- |
| T | T | T | F |
| T | F | F | T |
| F | T | F | T |
| F | F | F | T |


## Truth table for $(P \rightarrow R) \wedge(Q\rightarrow R)) \leftrightarrow (P\vee Q \rightarrow R)$

| $P$ | $Q$ | $R$ |  $P \rightarrow R$ | $Q \rightarrow R$  | $(P \rightarrow R) \wedge (Q \rightarrow R)$ | $(P \vee Q)$ | $P \vee Q \rightarrow R$ |      $(P \rightarrow R) \wedge (Q \rightarrow R)  \leftrightarrow (P \vee Q \rightarrow R)$
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T   | T   | T   | T   | T   | T   | T   | T   | T   |
| T   | T   | F   | F   | F   | F   | T   | F   | T   |
| T   | F   | T   | T   | T   | T   | T   | T   | T   |
| T   | F   | F   | F   | T   | F   | T   | F   | T   |
| F   | T   | T   | T   | T   | T   | T   | T   | T   |
| F   | T   | F   | T   | F   | F   | T   | F   | T   |
| F   | F   | T   | T   | T   | T   | F   | T   | T   |
| F   | F   | F   | T   | T   | T   | F   | T   | T   |


## Definitions of terms related to Propositional Calculus
An assignment of truth values to a set of variables is called an _interpretation_

A formula which is true for all interpretations is called a _tautology_
The formula  $(P \rightarrow R) \wedge(Q\rightarrow R)) \leftrightarrow (P\vee Q \rightarrow R)$ is a tautology.

A formula is _satisfiable_ if there is at least one interpretation which makes it true.

The formula  $\neg (P \wedge Q)$ is satisfiable, but is not a tautology.

The formaula $P \wedge \neg P$ is not satisfiable.

How long does it take to test if a formula with N variables is a tautology using a truth table?

