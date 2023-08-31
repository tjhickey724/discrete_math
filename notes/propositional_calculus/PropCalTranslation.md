# Practice Converting English into Propositional Calculus

This question will assess your ability to translate English statements into logic. 
Assume we have a program P with two functions F1 and F2 that are operating either with a high load or a low load. 

We will assume the following propositions are either true or false:
```
E1: function 1 throws an error
E2: function 2 throws an error
H: the load is high
C: the program crashes
```

You will translate English statements to propositional logic using only the logical connectives 
```
   NOT, AND, XOR, OR, IMPLIES, and IFF
```
and the four propositions above (E1,E2,H,C)

Assume that 
* the precedence of the operators is as listed above (i.e. AND binds tightest and IFF binds weakest) and that 
* all operators are right associative (i.e.
```
   A implies B implies C
means 
   A implies (B implies C).
```

## Convert the following statements to propositional logic:

A. Both functions throw an error

B. If the load is high then at least one of the functions throws an error

C. The program craahes if two conditions hold: (1) the load is high and (2) one (or both) of the functions throws an error.

D. Two things are true: (1) If the load is high the function 1 throws an error, and (2) if the load is low then the program crashes only if function 2 throws an error

E. The program keeps running (i.e. doesn't crash) only if both functions work correctly (i.e. neither function throws an error)

F. If the load is low, then the program crashes only if both functions throw an error

G. The program crashes if and only if function 1 throws an error when the load is high and function 2 throws an error when the load is low

H. If the program crashes then exactly one of the two functions throws an error
