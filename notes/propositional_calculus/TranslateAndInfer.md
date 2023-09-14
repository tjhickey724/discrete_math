# Examples of Translation and Inference
Let's look at how to use the Propositional Calculus to reason about systems.
The idea will be to take an argument, in English, convert it to the Propositional Calculus,
and then use inference tools to verify that the argument (as translated) is valid,
or to find a counter example and translate that back to English.

## First example
Let's see if the following is a valid argument about a program which contains two function definitions,
among other things, and which runs on a system which could have a high load or a low load.

```
P1: If the load is high then at least one of the functions throws an error
P2: The program keeps running (i.e. doesn't crash) only if both functions work correctly (i.e. neither function throws an error)
.............
C: If the load is high then the program crashes.
```
The first step is to identify the primitive propositions. We have already seen this problem in the homework,
so we can use those propositions:
```
H: the load is high
C: the program crashes
E1: function 1 throws an error
E2: function 2 throws an error
```
We can now translate this English argument into formal logic:

P1: $H \rightarrow E1\vee E2$

P2: $\neg C \rightarrow \neg E1 \wedge \neg E2$

.....................

C:  $H \rightarrow C$

