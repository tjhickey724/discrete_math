# Truth Tree Performance
We know that the Truth Table method can take $2^n$ steps to determine if a formula with $n$ propositions is a tautology.
We first show that in some cases the Truth Tree method can solve very large problems with many propositions quickly.

For example, consider the following:

$A_1$

$A_1 \rightarrow A_2$

$A_2 \rightarrow A_3$

$A_3 \rightarrow A_4$

$\ldots$

$A_{999} \rightarrow A_{1000}$

_________

$A_{1000}$

With the Truth Table method this would take at lesat $2^{1000}$ steps which is about $10^{300}$ and hence
is impossible.

But with the Truth Tree Method we see that the tree has a simple form and can be processed in about $1000$ steps.
Likewise, the more general problem with $n$ premises and $n$ propositional symbols could be done in $n$ steps instead of $2^n$.

![ImplicationChaining](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TruthTreeForimplicationChain.jpg)

Note however, that if we instead chose to use the OR-rule on the implications $A{2n}\rightarrow A_{2n+1}$ we would
get a tree with an exponential number of branches, so the order really does matter ...

![TruthTree Exponential Growth](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/exponentialTruthTreeGrowthExample.jpg)



