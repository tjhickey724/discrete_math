# Overview of the Predicate Calculus

We will introduce the predicate calculus and we practice converting English statements into the Predicate Calculus.

We expand the language of Propositional calculus to include 

* predicates, which are boolean functions of one or more variables, P(x), Q(x,y,z). u=v, u<v
* boolean operators connecting formulas: P and Q, P xor Q, P or Q, not P, P implies Q, P iff Q, 
* quantifiers,where F is a predicate formula
  * $\exists x . F$
  * $\forall x . F$
  
* functions and constants, e.g.
  e.g. square(x),  x*y, 0, 1, etc.

In most math texts you will see forall written as an upside down A ($\forall$) and exists as a backwards E ($\exists$),
we will use that notation, but we will sometimes write them outs using ```forall x``` for $\forall x$ and ```exists x``` for $\exists x$


The Predicate Calculus is the language of Mathematics. In theory, anything that can be expressed in Mathematics can be expressed in this formalized language. A key skill is to be able to translate a statement in English into the Predicate Calculus. It will usually remove most of the ambiguity in the original English statement.  

For the Propositional Calculus, the propositions could be thought of as boolean variables which are either true or false, and a propositional formula was a boolean expression as we see in Python, Java, and all other modern imperative programming languages.

For the Predicate Calculus, the predicates are boolean functions over some domain D which we will usually specify ahead of time (e.g. the domain of integers, or real numbers, or strings of characters, or functions on the real numbers, etc.).  Some predicates we write in "infix" mode such as the comparison functions (=, <, >=, etc.). The Predicate calculus also allows functions from the domain D to itself, and constants (which are elements of the domain). This is a very expressive language and most people believe that any mathematical concept can be expressed in the Predicate Calculus.

Our goal is to help you begin to develop the skill of translating English statements to the Predicate Calculus and to assess your mastery using a quiz. If we have time, we'll also start to talk about formal methods for proving theorems in the propositional and predicate calculus, but we'll probably have to wait until next week for that.

## Translation Examples
Here are some examples over the domain of integers.

### A.  d is a divisor of n  
$\exists k . n = d*k$

### B.  p is prime
(i.e. the only positive divisors of p are 1 and itself)

$\neg \exists a \exists b  ((1 \lt a) \wedge (a\lt p) \wedge (p = a*b))$

or, if d is a positive divisor of p then d=1 or d=p

$\forall d (\exists a . p=ad) \rightarrow (d=1) \vee (d=p)$



and here are some for the domain of real numbers

### C. The quadratic formula over the domain R of real numbers

$\forall a,b,c,x . 
  a*x^2 + b*x + c = 0 \rightarrow 
       (  x = (-b + sqrt(b^2-4*a*c))/(2*a)
         \vee 
          x = (-b - sqrt(b^2-4*a*c))/(2*a)
       )$

where the implies could be replaced with an iff

### D. every two real numbers has a number between them
$\forall x. \forall y.  (x<y) \rightarrow \exists z. x<z and z<y$

Now let's let you do some translation:

### E. for any two real numbers they are either equal or one is bigger than the other

### F. there is a real number which is bigger than all other real numbers

### G.  x^2 is less than x if and only if x is less than 1

### H. for any two positive numbers a,b   a*b is less than or equal to (a+b)/2 squared

## More examples
Now lets use the domain of functions, where 
* $A(f)$ means f is always increasing
* $B(f,g)$  means f is always bigger than or equal to g
* $C(f,g,h)$ means f(x)+g(x) = h(x) for all x, i.e. f+g=h
* $E(f,g)$ means f and g are the same function

Try to convert these to predicate calculus
* every function f is always increasing or there is a bigger function which is always increasing
* if f is always increasing the so is 2f (i.e. f+f)
* if f and g are always increasing then so is f+g
* there does not exist a function f which is bigger than all increasing functions
* there is a function g such that f+g=f for all functions f
* if f is bigger than or equal to g and vice versa, then f is equal to g


