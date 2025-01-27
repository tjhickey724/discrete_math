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
We also use the $\models$ operand to express this property:
$E_1,\ldots,E_n \models C$ and we say that $C$ is a logical consequence of $E_1,\ldots,E_n$.

## An Example of using the Truth Tables to prove a logical inference
Below we have an example of using the Truth Tree Method to prove that

$A\rightarrow C,  B\rightarrow C,  A\vee B  \models  C$

Here is how we prove this is true using Truth Tables.  
We create the truth tables for each of $A\rightarrow C, B\rightarrow C, A\vee B$
and then show that for each of the three interpretations where all three are true
(ABC = TTT, TFT, FTT),we also see that $C$ is true.
![TruthTableExample1](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TruthTableInference.jpg)






## Truth Tree Operations
Next we will look at another approach to proving that a conclusion is a logical consequence of a set of premises.
This approach can be faster that the truth table method in some cases. The idea is to generate a tree where
each "open" branch corresponds to a set of interpretations which make the premises and the negation of the conclusion true. If there are no open branches, then there are no interpretations which make all of the premises true and the negation of the conclusion true, i.e. the conclusion false.  Hence every interpretation which makes the premises true, must also make the conclusion true, and hence the argument is valid!

The Truth Tree method is a graphical approach to searching for counterexamples, that is interpretations which make E1,...,En true
but which make C false.  If no such counterexamples can be found, the C must be true whenever E1,...,En are true.

The first step is to write down the formulas E1,...,En, and the negation of the conclusion C
```
E1
E2
...
En
-C
```
We then apply the following rules which simplify the formulas in the tree.

The rules are shown in the following image:
![Truth Tree Operations](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TruthTreeOperations.jpg)

For the cases where there is branching, this corresponds to looking at the different cases, e.g. if $E \vee F$ is true, then we can look at two cases:
1) the case where $E$ is true
2) the case where $F$ is true

Each of the two branches correspond to different cases...

The argument for the other operators is similar. For example $E \rightarrow F$ is true precisely when
$\neg E$ is true or $F$ is true, and this gives us two cases to explore.

Since the formulas get simpler when we check them off, we see that this process will eventually end and the only unchecked formulas on the branches will be propositions (e.g. $A$, $B$) or their negations $\neg A$, $\neg B$).  Branches that contain a contradiction (i.e. both $A$ and $\neg A$) are closed. Open branches, correspond to counterexamples, which make all of the premises True and the conclusion False, and so demonstrate that the argument is not valid.



## Example of using the Truth Tree Method to prove that logical inference

![TruthTreeExample1](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TreeMethodExample1.jpg)

Let's walk through the steps of creating this tree and interpreting its results.

The first step is to write down the premises and the negation of the conclusion.
Next we apply the Truth Tree Method rules by choosing an unchecked formula, and the expanding the tree using that formula.
If any branch contains both a proposition $P$ and it negation $\neg P$, the we mark that branch as "closed" using an asterisk.
Since all branches are closed, there are no counterexamples to this argument.

Note that when we use one of Truth Tree Method operations, we have to apply it on every open branch in the tree, after which we can
mark it with a check mark indicating it has been handled.

## An example of using the Truth Tree Method to find a counterexample to an argument
Next lets use the Truth Tree Method to investigate the argument of whether

$A\rightarrow C, B\rightarrow C \models C\rightarrow A \vee B$

Here is what we get if we apply the Truth Tree Method to this argument
(note we negate the conclusion and simplify it to move the negations inward before continuing).

![TruthTreeExample2](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TreeMethodExample2.jpg)

Note that first we simplify the negation of the conclusion then we apply the rules for implication, on each branch. None of the
branches are closed and they all have the same interpretation $\neg A, \neg B, C$ (that is A=B=False, C=True) which satisfies the premises but not the conclusion,
so the argument in not valid!





