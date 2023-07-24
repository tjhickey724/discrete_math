# Overview of Propositional Calculus

The Propositional Calculus is a formal language for expressing logical concepts. 

The primitives are propositions (typically named P, Q, R, ...) which are assumed to be either true or false. 
These are connected to form sentences using the logical connectors: and, or, not, and others. 

## Propositional Sentences
Sentences in the Propositional calculus are formed by primitives called propositions (typically named P, Q, R, ...)
joined together with logical operators (and, or, not, and others)

The operators are usually written with special symbols (where P and Q are propositional sentences)
* $\neg P$. This is the negation of P and is true precisely when P is false.
* * $P \wedge Q$. This is the conjuntion of P and Q and is true both P and Q are true
* $P \vee Q$. This is the disjunction of P and Q and is true if P or Q or both are true
* $P \rightarrow Q$. This is the implication, P implies Q, and it is true when P is false or Q is true.

## Other connectors
* only if:  $P \leftarrow Q$. This is true when Q is false or P is true.
* if and only if: $P \iff Q$. This is true when P and Q have the same truth value.
* exclusive or:  $P \oplus Q$ is true if P or Q but not both are true

This language is also called Boolean Algebra and the sentences are formulas in Boolean algebra. Many of the familiar properties of high school algebra also hold true in Boolean Algebra.

Each sentence has a truth value (true or false) which can be obtained from the truth values of the propositions using a truth table.


# Readings
Here are some chapters in free online textbooks covering these concepts
* DM-AOI Ch 0.2 http://discrete.openmathbooks.org/dmoi3/sec_intro-statements.html
* DM-AOI Ch 3.1 http://discrete.openmathbooks.org/dmoi3/sec_propositional.html
* MfCS Ch3 https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-spring-2015/readings/MIT6_042JS15_textbook.pdf
