# Covid Examples
Next let's look at how the Predicate Calculus can be used to reason about 
domains which are not purely mathematical, for example, in epidemiology.

Consider the domain $D$ of some group of people (perhaps Brandeis students)
and the following predicates
on that domain:
* P(x) == x has covid
* F(x) == x has a fever
* C(x,y) == x is a close contact of y
* R(x,y) == x and y are roommates
* V(x) == x had the covid vaccine
* I(x) == x has influenza

Let's translate the following formulas to predicate calculus

1. Everyone that has a fever either has covid or influenza or both.
   
   $\forall x F(x) \rightarrow P(x) \vee I(x)$
   
3. Whenever people are roommates,  they are also close contacts.
   $\forall x \forall y . R(x,y) \rightarrow C(x,y)$
   
5. Some people are close contacts but aren't roommates.

   $\exists a \exists b . C(a,b) \wedge \neg R(a,b)$
   
7. Everyone that has covide has a close contact with covid.
8. If someone has a roommate with covide and they don't have covide then they are vaccinated.
9. If everyone is vaccinated then noone has covid.
10. If someone has covid then all of their close contacts who are not vaccinated has covid.
   
