# Parse Trees for First Order Logic
To fully understand the meaning of a formula in First Order Logic, it is important to be able to
draw its parse tree, as that clearly indicates the scope of the quantified variables. We could get the
same information using fully parenthesized expressions, but the parse tree is easier to visualize.

The simplest way to draw a parse tree for a formula in the Predicate Calculus is to add new nodes
for the universal and existential quantifiers. These nodes have one child, which is the formula that
is being quantified.

## Example 1
Let's draw the parse tree for 

$\forall x \exists y P(x,y) \rightarrow \exists z P(z,x)$

Notice that the $\exists y$ only quantifies $P(x,y)$. In general, the convention is to make the scope of a quantifier
as small as possible.

![FOL parse tree #1](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/FOLparseTree1.jpg)

## Example 2
If we want a larger scope, we can indicate that with parentheses, for example, let's draw the parse tree for the following
similar formula:

$\forall x \exists y ( P(x,y) \rightarrow \exists z P(z,x))$

Notice that the $\exists y$ now quantifies the whole implication

![FOL parse tree #2](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/FOLparseTree2.jpg)

One could ask whether these two formulas are "logically equivalent" but we'll have to wait until we define what that
means for the Predicate Calculus.

## Try some yourself
Draw the parse trees for the following formulas

1. $\exists y \forall x P(x,y) \rightarrow \forall x \exists y P(x,y)$
2. $\exists x P(x) \rightarrow \forall y \exists z P(y) \wedge Q(y,z)$
3. $\exists x P(x) \rightarrow \forall y \exists z Q(y,z) \wedge P(y)$
4. $\forall x \forall y x<y \rightarrow \exists z x<z \wedge z<y$

   
