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
* R $\forall x (x=x)$, i.e. equality is reflexive
* S $\forall x \forall y ((x=y) \rightarrow (y=x))$, equality is symmetric
* T $\forall x \forall y \forall z ((x=y) \wedge (y=z) \rightarrow (x=z))$  equality is transitive

and the axioms for addition and multiplicaiton are
1. $\forall x (x+0=x)$
2. $\forall x \forall y (x+s(y)) = s(x+y)$  i.e. x+(y+1) = (x+y)+1
3. $\forall x (x*0=0)$
4. $\forall x \forall y (x * s(y) = x * y + x)$
5. $\forall x \forall y (x=y) \rightarrow (s(x)=s(y))$,
6. $\forall x \forall y \forall z (x=y) \rightarrow (x+z = y+z) \wedge (z+x=z+y)$
7. $\forall x \forall y \forall z (x=y) \rightarrow (x*z = y*z) \wedge (z*x=z*y)$

Let's use these axioms to prove that 1+1=2, i.e.
* $s(0)+s(0) = s(s(0))$


We can give a direct proof as follows:
* $s(0) + 0 = s(0)$, by (1) with x = s(0)
* $s(0) + s(0) = s(s(0)+0)$, by (2) with x=s(0) y=0
* $s(s(0)+0) = s(s(0))$ by (5) with x=s(0)+0 and y=s(0)
* $s(0)+s(0) = s(s(0))$ by (T)

  
