# The Peano Axioms

Let's look at a simple axiomatization of Integer Arithmetic.
the domain will be the non-negative integers 0,1,2,...

The language has 
* the predicate "x=y"
* the constant 0
* the function successor function s(x) = x+1
* the addition function (x,y) => x+y
* the multiplication function (x,y) => x*y

The axioms for "=" are
* $\forall x (x=x)$, i.e. equality is reflexive
* $\forall x \forall y (x=y \rightarrow y=x)$, equality is symmetric
* $\forall x \forall y \forall z (x=y \wedge y=z \rightarrow x=z)$  equality is transitive

and the axioms for addition and multiplicaiton are
* $\forall x (x+0=x)$
* $\forall x \forall y (x+s(y)) = s(x+y)$  (i.e. x+(y+1) = (x+y)+1
* $\forall x x*0=0$
* $\forall x \forall y (x*s(y) = x*y + x$

Let's use these axioms to prove that 1+1=2, i.e.
* $s(0)+s(0) = s(s(0))$



