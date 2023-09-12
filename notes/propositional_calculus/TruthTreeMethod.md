# The Truth Tree Method
In this slide we introduce the Truth Tree Method which is a technique proving that a conclusion formula $C$ in Propositional Logic
is a logical consequence of a set $S$ of premises, or finding a counterexample if it is not a logical consequence. 

We can easily test for logical equivalence using Truth Tables, but if there are $n$ propositions, the Truth Table method will take
$2^n$ steps to prove logical consequence, and the Truth Tree method can sometimes be faster. We will show that this method can be
extended to work with the Predicate Calculus 
(where we add parameters to the Propositions as well as function and constant symbols and universal and existential quantifiers).

## Overview
The goal of this approach is to see if a conclusion $C$ is true when ever every element of a set of premises $E_1,\ldots,E_n$ is true.
In such a case, we say that $C$ is a logical consequence of $E_1,\ldots,E_n$, and we write it as follows:

```
E1
E2
...
En
---
C
```
The Truth Tree method is a graphical approach to searching for counterexamples, that is interpretations which make E1,...,En true
but which make C false.  If not such counterexamples can be found, the C must be true whenever E1,...,En are true.

The first step is to write down the formulas E1,...,En, and the negation of the conclusion C
```
E1
E2
...
En
-C
```
We then apply the following rules which simplify the formulas in the tree.

## Truth Tree Operations
The rules are shown in the following image:
![Truth Tree Operations](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TruthTreeOperations.jpg)


