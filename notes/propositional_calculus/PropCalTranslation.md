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

answer: $E1 \wedge E2$   <br>  ```E1 AND E2```

B. If the load is high then at least one of the functions throws an error

answer: $H \rightarrow (E1 \vee E2)$   <br> ```H IMPLIES ( E1 OR E2)```

C. The program craahes if two conditions hold: (1) the load is high and (2) one (or both) of the functions throws an error.

D. Two things are true: (1) If the load is high the function 1 throws an error, and (2) if the load is low then the program crashes only if function 2 throws an error

E. The program keeps running (i.e. doesn't crash) only if both functions work correctly (i.e. neither function throws an error)

F. If the load is low, then the program crashes only if both functions throw an error

G. The program crashes if and only if function 1 throws an error when the load is high and function 2 throws an error when the load is low

H. If the program crashes then exactly one of the two functions throws an error

## Convert the following statements to English

I.  Translate to English: $E1 \wedge H \rightarrow E2 \wedge C$

J. Translate to English: $\neg C \rightarrow \neg (E1 \vee E2)$

K. Translate to English: $C \leftarrow E1 \vee (E2 \wedge H))$

___

# Translate to Logic

Suppose we have the following Propositions;
S = the shift key is pressed
X = the X key is pressed
E = the form is in edit mode
A = an alert box pops up

Translate the following statements to Propositional Logic using only the propositions S, X, E, A and the following logical connectives: 
  not, and, xor, or, implies, iff. 
Use parentheses if you need them. Remember that the precedence of the operators is as listed above (not binds tightest) and the operators are right associative 
so A => B => C means  A => (B => C)

A. the shift key and the X key are both pressed

B. if X is pressed and it is not in edit mode then an alert pops up

C. the alert box pops up only if the shift key is pressed

D. if the form is not in edit mode and the X key is pressed, then an alert pops up

E. the alert box pops up when an X is typed if and only if the form is not in edit mode

F. Either the shift key is pressed or the x key is pressed, but not both

G. the form is in edit mode only if the shift key and the X key are pressed

H. if the alert box pops up when the X key is pressed, then the form is not in edit mode
