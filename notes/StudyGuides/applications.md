# Examples of Applications of the Discrete Math topics taught in CS29a Fall25

Why should a computer scientist learn discrete math? What is it good for?
Here are some examples.

Propositional Logic is used to define logic gates in CPUs, and to define theoretical complexity of functions. It is also used in optimizing 
conditional expressions in programming languages and database queries. [Here](http://intrologic.stanford.edu/extras/circuits.html) is an example of defining the key component in a CPU addition circuit - the half adder. Logic can be used to define the circuit, simulate it with various inputs, verify that it works correctly, or diagnose any mistakes in the design.

Predicate Calculus is the language of mathematics and proof. It is used to precisely define what a program or algorithm does. There is considerable interest in developing systems that can automatically prove that an algorithm meets a particular formal logic specification. LLM-AIs might be able to help us write programs in a few years which can automatically be verified to be correct! [Dafny](https://en.wikipedia.org/wiki/Dafny) is an example of a programming language which requires first order logic statements describing its correctness, and which tries to automatically verify that the assertions are true.

Sets and Functions: these are the fundamental building blocks of Data Structures and so are a fundamental part of Discrete Mathematics.

Proof Techniques: now that LLMs are able to generate code it is more important than ever that developers can prove that the programs they are writing with help from an AI are correct. This includes the algorithms they use and the general structure of the program. A Proof is a strongly convincing argument that a mathematical statement is true. So we need to express the correctness properties in Mathematics and the prove they are correct. Learning how to write convincing proofs is both a skill and an art.

Combinatorics: this is the Science of counting the sizes of sets defined by specific properties. It plays a key role in many correctness proofs as well as in developing algorithms that are efficient as well as correct.

Sequences: the goal here is to define a sequence of numbers by some kind of recursive rules and then find a simple mathematical expression for the nth element of that sequence. One important examples is calculating the runtime of a program in terms of the size $n$ of its input, or the maximum amount of space that an algorithm will require on inputs of size n.

Probability: some of the most effective programs are only efficient in the average case, we need to understand probability to determine the average case execution time of a program. There are other programs which rely on probability and produce a correct result most of the time where the probability it is wrong is very small. When we study number theory and cryptography the last week of class we will present a probabilistic prime test where the probability of error is $2^{-n}$ and $n$ is a parameter the programmer chooses and larger values of $n$ mean the program takes longer to run, so you trade accuracy for execution time.

Graph Theory: one of the key abstractions in Computer Science is the notion of a data structure and most data structures can be thought of as Mathematical graphs, we will see graphs everywhere in this course -- as parse trees, proof trees, probability diagrams, sets of trees, equivalence relations, directed acyclic graphs, finite state machines, etc.

Number Theory: most of modern cryptography is based on properties of integer arithmetic, we will learn how the Public Key SSL systems work. It is possible that quantum computing will allow us to break all of these codes.
