# Parse Trees for First Order Logic
To fully understand the meaning of a formula in First Order Logic, it is important to be able to
draw its parse tree, as that clearly indicates the scope of the quantified variables. We could get the
same information using fully parenthesized expressions, but the parse tree is easier to visualize.

The simplest way to draw a parse tree for a formula in the Predicate Calculus is to add new nodes
for the universal and existential quantifiers. These nodes have one child, which is the formula that
is being quantified.

## Example 1
Draw the parse tree for 

$\forall x \exists y P(x,y) \rightarrow \exists z P(y,z)$

