# Covid Examples
Next let's look at how the Predicate Calculus can be used to reason about 
domains which are not purely mathematical, for example, in epidemiology.

Consider the domain $D$ of some group of people (perhaps Brandeis students)
and the following predicates
on that domain:
* S(x) == x is sick with covid
* F(x) == x has a fever
* C(x,y) == x is a close contact of y
* R(x,y) == x and y are roommates
* V(x) == x had the covid vaccine
* I(x) == x has influenza

Let's translate the following formulas to predicate calculus

1. Everyone that has a fever either has covid or influenza or both.
   
   $\forall x F(x) \rightarrow S(x) \vee I(x)$
   
2. Whenever people are roommates,  they are also close contacts.

   $\forall x \forall y . R(x,y) \rightarrow C(x,y)$
   
3. Some people are close contacts but aren't roommates.

   $\exists a \exists b . C(a,b) \wedge \neg R(a,b)$
 
4. Everyone that has covid has a close contact with covid.
5. If someone has a roommate with covide and they don't have covide then they are vaccinated.
6. If everyone is vaccinated then noone has covid.
7. If someone has covid then all of their close contacts who are not vaccinated have covid.

Let's have you think up some statements to convert to this first order language...

How would you translate the following formulas in plain English (where a and b are constants, i.e. refer to
individuals like "Andy" and "Bohan"
1. $\forall x . F(x) \wedge V(x) \rightarrow I(x)$
2. $P(a) \wedge R(a,b) \wedge \neg V(b) \wedge F(b)$
3. $\forall x \exists y . C(x,y)$
4. $\exists y \forall x . C(x,y)$
5. $\forall x \forall y . C(x,y) \rightarrow C(y,x)$

   
