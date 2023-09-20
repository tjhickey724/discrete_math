# Interpretations in First Order Logic

One of the main differences between Propositional Logic and First Order Logic is that an interpretation $I$
for First Order Logic requires that we specify 
* a domain $D$ and
* for each constant symbol $a$ an element $I(a)$ of that domain, and
* for each function symbol $f$ a function $I(f)$ on that domain, and
* for each predicate symbol $P$ a boolean function $I(P)$ on that domain

Once we have specified an interpretation we can determine the truth or falsity of any formula 
without quantifiers my first evaluate the truth values for each predicate in the formula, then
we use the usual rules for propositional logic to evaluate the truth value of the entire formula.

Let's get some practice with that..

## Example 1.
Suppose $I$ is the usual interpretation of the language of integer arithmetic, so the domain is the
integers (positive, zero, and negative), and the predicates are $a\lt b, a=b, a\le b$ etc with their
usual meaning and the constants are $0,1,2,..., -1,-2,...$ with their usual meaning, and the functions
are $a+b, a-b, a*b$ with their usual meaning. We don't include division as it doesn't always return an integer
and is sometimes undefined, e.g. $1/0 = ???$

What then is the truth value for the following formula where we also define
$I(a)=4$, $I(b)=7$ and $I(c)=0$

$(a+b \lt c) \wedge (b\le c \rightarrow (a\gt c)$

To evaluate this we first replace all of the constants $a,b,c$ with their values under $I$

$(4+7 \lt 0) \wedge (7\le 0 \rightarrow (4\gt 0)$

Then we evaluate the predicates

$11\lt 0 = F$, $7 \le 0 = T$, $4 \gt 0$ = T

and finally evaluate the result boolean formula:

$F \wedge (F \rightarrow T)$
$\equiv F \wedge T$
$\equiv F$

## Example 2.
Lets try a different example. Let $D$ be the domain consisting of the digits $\{1,2,3,4\}$
and let $P$ be the predicate defined by the following table, where the rows are "x" and the columns are "y"
```
         y
P(x,y) 1 2 3 4
     1 F F T F
 x   2 F T T T
     3 T T T T
     4 F T F T
```

Given this predicate which of the following are true?
Explain why or why not...
1. $\forall x \exists y P(x,y)$
2. $\exists y \forall x P(x,y)$
3. $\forall y \exists x P(x,y)$
4. $\exists x \forall y P(x,y)$
5. $\forall x \forall y \neg P(x,y)$
6. $\forall x \neg \forall y P(x,y)$
7. $\neg \forall x \forall y P(x,y)$

For (1), it is saying that for each x in the domain (1,2,3,4) there must be some y in the domain
which makes P(x,y) true. In other words, in each row there must be some column which is True.
Let's check it
* for x=1 P(1,3) is true
* for x=2 P(2,3) is true (as is P(2,2) and P(2,4))
* for x=3 P(3,*) is true for all columns
* for x=4 P(4,2) and P(4,4) are true

So formula (1) is true.

For (2), it is saying that there is a column y such that P(x,y) is true for all rows x,
but we can see this isn't true; each column contains at least one F. So (2) is false

Try the others!

## Example 3
Let $I$ be the usual interpretation for integer arithmetic, and extend it so that
* $I(f)$ is the increment function $s(x)=x+1$ and
* $I(g)$ is also the increment function
* $I(a)=10$ and $I(b)=20$
* $I(P)$ is the "less than" predicate, that is  $P(x,y) \equiv (x\lt y)$
What are the truth values of the following formulas:

1. $\neg P(g(a),a) \wedge P(a,f(a))$
2. $\forall x \neg P(g(x),x) \wedge P(x,f(x))$

For (1), we first evaluate the functional expressions $a=10$, $g(a)=11$, $f(a)=11$
and then substitute them into the formula:

$\neg P(g(a),a) \wedge P(a,f(a))$

$\equiv \neg P(11,10) \wedge P(10,11)$, then replace P with $\lt$

$\equiv \neg(11<10) \wedge 10<11$, then evaluate the predicates and the formula

$\equiv \neg F \wedge T \equiv T$

For (2), we can replace the $P$ by $\lt$ and the $f$ and $g$ by the increment function:

$\forall x \neg P(g(x),x) \wedge P(x,f(x))$

$\equiv \forall x \neg P(x+1,x) \wedge P(x,x+1)$

$\equiv \forall x \neg (x+1\lt x) \wedge (x\lt x+1)$, and since we know that $x\lt x+1$ for all x, 

$\equiv \forall x \neg F \wedge T \equiv \forall x T \equiv T$

Try the following yourself. Are they true or false, and explain why...

1. $P(a,b) \rightarrow P(g(a),f(b)$
2. $\exists x P(a,x) and P(x,a)$
3. $\forall x \exists y  P(x,y)$
4. $\exists x \forall y  P(x,y)$



