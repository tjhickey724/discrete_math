# Inference and Validity of Arguments

In propositional logic we have the notion of a **tautology**, also known as a **valid formula**.
This is a formula which evaluates to True for every interpretation. 

More generally, we have the
notion of a valid argument which consists of a set of premises and a conclusion with the property
that every interpretation which makes all of the premises true, also must make the conclusion true.

We can use exactly the same definition for a valid argument in the Predicate Calculus.

An **argument** is a sequence for first order formulas called the premises together with a first
order formula called the conclusion. We assume that all variables in the formulas are quantified
so there are no free variables.

An argument is **valid** if every interpretation that makes the premises true, also makes the conclusion true.

This is a very powerful statement!

Different interpretations have different domain sets, and a valid argument is telling us that for any interpretation,
with any domain set, if the premises are true, then so is the conclusion!

In particular, if an argument is valid, and we have a particular interpreation in mind which satisfies all of the premises,
then we know the comclusion must hold for that interpretation too.

Conversely, if an argument is not valid, then there must be an interpretation which makes the premises true, 
but makes the conclusion false...  

We will see that if an argument is valid, then the Tree Method (and other inference methods) are guaranteed to finish
and show that the argument is valid.  If it is not valid, the Tree Method might generate an infinite tree, and we might
now know that it the tree will be infinite, so there is no way of knowing for sure with these methods that the formula isn't valid!

## Examples
Lets consider some simple arguments and see if we can show they are valid or find a counter example.

### Example 1.
$\exists x \forall y P(x,y)$
...................
$\forall y \exists x P(x,y)$




