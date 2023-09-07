# Inference Rules for Propositional Calculus

We say that two formulas $F_1$ and $F_2$ are equivalent, writted $F_1\equiv F_2$ if they
hae the same values on all interpretations.

We can think of the Propositional Calculus as a kind of Algebra (called Boolean Algebra)
and we can apply operations on these formula that are very similar to the standard operations
in arithmetic. This page has some of the most common operation and they can easily be verified
to be correct by calculating their truth tables.

| Rule Name | Rule |
| --- | --- |
| Double Negation | $\neg \neg A \equiv A$ |
| DeMorgan's Law for AND| $\neg (A \vee B) \equiv \neg A \wedge \neg B$ |
| DeMorgan's Law for OR| $\neg (A \wedge B) \equiv \neg A \vee \neg B$ |
| Distributive Law of OR over AND| $A \vee (B \wedge C) \equiv (A\vee B) \wedge (A\vee C)$|
| Distributive Law of AND over OR | $A \wedge (B \vee C) \equiv (A\wedge B) \vee (A\wedge C)$|
| Commutativity of OR | $A \vee B \equiv B \vee A$|
| Commutativity of AND | $A \wedge B \equiv B \wedge A$|
| Associativity of OR | $A \vee (B \vee C) \equiv (A \vee B) \vee C$|
| Associativity or AND| $A \wedge (B \wedge C) \equiv (A \wedge B) \wedge C$|
| Implication definition| $A \rightarrow B \equiv \neg A \vee B$|
| XOR definition| $A\oplus B \equiv (A \vee B) \wedge \neg (A \wedge B)$|
| Identity rules | $True \vee A \equiv True$ |
| Identity rules | $False \vee A \equiv A$ |
| Identity rules | $True \wedge A \equiv A$ |
| Identity rules | $False \wedge A \equiv False$ |
| Identity rules | $A \wedge A \equiv A$ |
| Identity rules | $A \vee A \equiv A$ |
| Identity rules | $A \wedge \neg A \equiv False$ |
| Identity rules | $A \vee \neg A \equiv True$|
| Identity rules | $A\wedge B \ vee A \equiv A$ |
| Identity rules | $(A \vee B) \wedge A \equiv A$ |

Using these rules you can convert any boolean formula into a normal form called _Disjunctive Normal Form_ ( ***DNF*** )
which is a disjunction (ORs) of conjunctions (ANDs) or propositions or negated propositions.  We can easily
write downn the DNF of a formula by looking at its truth table, e.g. lets look at the truth table for
$(P \rightarrow \neg Q \wedge R $

| $P$ | $Q$ | $R$ |   $P \rightarrow \neg Q \wedge R $ |   
| --- | --- | --- | --- |
| T   | T   | T   | F   |
| T   | T   | F   | F   |
| T   | F   | T   | T   | 
| T   | F   | F   | F   | 
| F   | T   | T   | T   | 
| F   | T   | F   | T   | 
| F   | F   | T   | T   | 
| F   | F   | F   | T   | 

Note: for those who know Python, you can write a program to generate this truth table as follows:
``` python
def f(p,q,r):
    return (1-p)|((1-q)&r)
for p in [1,0]:
    for q in [1,0]:
        for r in [1,0]:
            print(p,q,r,f(p,q,r))
```

Anyway, this formula has four rows for which it is true, and each of those rows can be expressed as a conjunction of propositions or their negations, so 

$P \rightarrow \neg Q \wedge R$  is equivalent to

$(P \wedge \neg Q \wedge R) \vee (\neg P \wedge Q \wedge R) \vee (\neg P \wedge Q \wedge \neg R)  \vee (\neg P \wedge \neg Q \wedge R) \vee (\neg P \wedge \neg Q \wedge \neg R)$

A simpler DNF for the formula would be obtained by noticing that the formula is true when P is false or
when (P,Q,R) = (T,F,T)
so it is equivalent to the following simpler DNF:

$(P \wedge \neg Q \wedge R) \vee \neg P$

We can convert the formula $P \rightarrow \neg Q \wedge R$  to DNF in one step using the Boolean Algebra rules without
having to construct the truth table though by using the definition of implication:

$P \rightarrow \neg Q \wedge R \equiv$

$\neg P \vee \neg Q \wedge R$ 

