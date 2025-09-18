# The Truth Tree Method for First Order Logic

We have seen how to use the Truth Tree method to show that a set of Propositional formulas is unsatisfiable 
(if all of the branches are eventually closed) or to find a counter example, that is an interpretation that
makes all of the formulas true.

We used this to show that an argument is valid by showing their are no interpretations which make all of the premises
true and make the conclusion false.  Thus, any interpretation which makes all of the premises true must also make
the conclusion true, and the argument is valid.

We can use a similar approach for arguments in the Predicate Calculus using the following steps.
1. negate the conclusion, as usual
2. simplify all of the premises and the negation of the conclusion

This leaves us with a set of formulas with the following properties
* the formulas only have universal quantifiers
* the only operators are $\wedge$ and $\vee$ and any negations only appear directly in front of predicates

In making this simplification we may have added some constants $C$ and some function symbols $F$, so we let
$U$ be the collection of all terms that can be created using the constant symbols and function symbols, e.g.
if 
* $C = \\{a,b\\}$ and
* $F = \\{f(x,y), g(z)\\}$,

then $U$ contains terms like the following:

$a, b, g(a), g(b), g(g(a)), \ldots f(a,a), f(a,b), \ldots, f(g(a), b), \ldots$

We call $U$ the set of **ground terms**.

We can then extend the tree method by adding one new rule:

**Instantiation**: _Any formula with quantifiers can be used to create a formula with no quantifiers 
by replacing each quantified variable by a ground term._

The problem is that there are infinitely many such instantiations, so any counter example will have an infinitely long branch
and so it is much harder to create counter examples with this approach.


## Example 1
Lets use the Tree Method to show the following is a valid argument

p1: $\exists x \forall y P(x,y)$

............................

c: $\forall y \exists x P(x,y)$

The first step is to simplify the premise and the negation of the conclusion, to get

p1: $\forall y P(a,y)$, we introduce the Skolem constant $a$ to replace the $\exists x$

not c: $\neg \forall y \exists x P(x,y)$

$\equiv \exists y \forall x \neg P(x,y)$

$\equiv \forall x \neg P(x,b)$, where we introduce the Skolem constant $b$ to replace the $\exists y$

So we now have two universally quantified formulas:

1. $\forall y P(a,y)$
2. $\forall x \neg P(x,b)$

For the first one, we can create a new formula by letting $y=b$ and fot the second let $x=a$, then we get two new formulas

3. $P(a,b)$, replacing $y=b$ in #1
4. $\neg P(a,b)$, replacing $x=a$ in $2$

and this says we must have $P(a,b)=True$ and $P(a,b)=False$ which is a contradiction, so we can close this branch,
and since this is the only branch the argument is valid.

This means that for any domain D and any predicate $P$ on that domain, if  $\exists x \forall y P(x,y)$ is true
then $\forall y \exists x P(x,y)$ must also be true!

Here is the Tree Method drawn out for this problem.

![FOL Tree Method 1](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/FOLtreeMethod1.jpg)

# Example 2
Here is a more complex example with a skolem constant and skolem function
[Truth Tree Example with FOL](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/Truth%20Tree%20Example%20with%20FOL.pdf))

# Example 3
If we try to test the validity of the converse argument


We get a Truth Tree with a single infinite branch and not contradictions... so if we blindly applied the instantiation rules
we would never stop and never find a counter example...

Here is what the tree looks like when you start it.

![FOL Tree method 2](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/FOLtreeMethod2.jpg)






