# The Truth Tree Method for First Order Logic

We have seen how to use the Truth Tree method to show that a set of Propositional formulas is unsatisfiable 
(if all of the branches are eventually closed) or to find a counter example, that is an interpretation that
makes all of the formulas true.

We used this to show that an argument is valid by showing their are no interpretations which all of the premises
true and make the conclusion false.  Thus, any interpretation which makes all of the premises true must also make
the conclusion true, and the argument is valid.

We can use a similar approach for arguments in the Predicate Calculus using the following steps.
1. negate the conclusion, as usual
2. simplify all of the premises and the negation of the conclusion

This leaves us with a set of formulas with the following properties
* the formulas only have universal quantifiers, and those appear at the beginning of the formula
* the only operators are $\wedge$ and $\or$ and any negations only appear directly in front of predicates

In making this simplification we may have added some constants $C$ and some function symbols $F$, so we let
$U$ be the collection of all terms that can be created using the constant symbols and function symbols, e.g.
if 
* $C = \{a,b\}$ and
* $F=\{f(x,y), g(z)\}$,

then $U$ contains terms like the following:

$a, b, g(a), g(b), g(g(a)), \ldots f(a,a), f(a,b), \ldots, f(g(a), b), \ldots$

We call $U$ the set of **ground terms**.

We can then extend the tree method by adding one new rule:

**Instantiation**: _Any formula with quantifiers can be used to create a formula with no quantifiers 
by replacing each quantified variable by a ground term._


