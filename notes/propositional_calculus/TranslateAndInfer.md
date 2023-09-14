# Examples of Translation and Inference
Let's look at how to use the Propositional Calculus to reason about systems.
The idea will be to take an argument, in English, convert it to the Propositional Calculus,
and then use inference tools to verify that the argument (as translated) is valid,
or to find a counter example and translate that back to English.

## First example
Let's see if the following is a valid argument about a program which contains two function definitions,
among other things, and which runs on a system which could have a high load or a low load.

```
Premise1: If the load is high then at least one of the functions throws an error
Premise2: The program keeps running (i.e. doesn't crash) only if both functions work correctly (i.e. neither function throws an error)
.............
Conclusion: If the load is high then the program crashes.
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

Premise1: $H \rightarrow E1\vee E2$

Premise2: $\neg C \rightarrow \neg E1 \wedge \neg E2$

.....................

Conclusion:  $H \rightarrow C$

An easy way to see this is true is to replace Premise2 with its contrapositive version which is logically equivalent.
That is $(A \rightarrow B) \equiv (\neg B \rightarrow \neg A$ which you can easily verify by simplification or using truth tables or truth trees, so we get

Premise2a: $E1 \vee E2 \rightarrow C$

and since $H \rightarrow E1\vee E2$ and $E1\vee E2 \rightarrow C$, we can conclude that $H \rightarrow C$, by
the transitivity of implication, that is $(A\rightarrow B) \wedge (B\rightarrow C) \rightarrow (A \rightarrow C)$.

More formally we can use the TruthTree method to verify this:
![TranslateAndInfer1](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/translateAndInfer!.jpg)


## Example 2
Let's try this one, with the same propositional symbols as above.

```
Premise1: If the load is high then at least one of the functions throws an error
Premise2: The program keeps running (i.e. doesn't crash) only if both functions work correctly (i.e. neither function throws an error)
.............
Conclusion: If the load is low, then both functions throw an error
```

Translating into logic we get

We can now translate this English argument into formal logic:

Premise1: $H \rightarrow E1\vee E2$

Premise2: $\neg C \rightarrow \neg E1 \wedge \neg E2$

.....................

Conclusion:  $\neg H \rightarrow E1 \wedge E2$

We can now use the Truth Tree Method and we see this has a counter example:

![TranslateAndInfer2](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/translateAndInfer2.jpg)

The counter example is $C \wedge \neg H \wedge \neg E1$, which translates back into English as:

```
Counter example:
When the program crashes and the load is not high and function 1 does not throw an error,
the premises are both true, but the conclusion is false.
```
