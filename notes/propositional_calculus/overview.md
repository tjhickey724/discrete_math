# Overview of Propositional Calculus

The Propositional Calculus is a formal language for expressing logical concepts. 

The primitives are propositions (typically named P, Q, R, ...) which are assumed to be either true or false. 
These are connected to form sentences using the logical connectors: and, or, not, and others. 

## Propositional Sentences
Sentences in the Propositional calculus are formed by primitives called propositions (typically named P, Q, R, ...)
joined together with logical operators (and, or, not, and others) to form sentences, which likewise are either true or false
(depending on the values of the primitive propositions).

The operators are usually written with special symbols (where P and Q are propositional sentences)


| Math | Text | Meaning |
| --- | ----  | --- |
| $\neg P$ |  not(P) |  This is the negation of P and is true precisely when P is false.|
| $P \wedge Q$ |  P AND Q | This is the conjuntion of P and Q and is true both P and Q are true|
| $P \vee Q$ | P OR Q |This is the disjunction of P and Q and is true if P or Q or both are true|
| $P \rightarrow Q$  | P IMPLIES Q <br>  P ONLYIF Q | This is the implication, if P then Q, and it is true when P is false or Q is true.|
| $P \leftarrow Q$  | P IF Q | This is the implication, Q implies P, if Q then P, and it is true when Q is false or P is true.|
| $P \iff Q$ | P IFF Q | This is true when P and Q have the same truth value, i.e. P is true IF AND ONLY IF Q is true.|
| $P \oplus Q$ |  P XOR Q | This is true if P or Q but not both are true, it is called the exclusive OR|


This language is also called Boolean Algebra and the sentences are formulas in Boolean algebra. 
Many of the familiar properties of high school algebra also hold true in Boolean Algebra.

Each sentence has a truth value (true or false) which can be obtained from the truth values of the propositions using a truth table.

 
## Definitions of some terms related to Propositional Calculus
An assignment of truth values $\\{T,F\\}$ to a set of variables is called an __interpretation__

e.g. $P\longrightarrow F$, $Q\longrightarrow T$. $R\longrightarrow F$

A formula which is true for all interpretations is called a __tautology__

The formula  $P \vee \neg P$ is a tautology.

A more complex tautology is $(P \rightarrow R) \wedge(Q\rightarrow R)) \leftrightarrow (P\vee Q \rightarrow R)$.

A formula is __satisfiable__ if there is at least one interpretation which makes it true.

If $\neg E$ is not satisfiable, then E is a tautology.

The formula  $\neg (P \wedge Q)$ is satisfiable, but is not a tautology.

The formula $P \wedge \neg P$ is not satisfiable.

How long does it take to test if a formula with N variables is a tautology using a truth table?



# Readings
Here are some chapters in free online textbooks covering these concepts
* DM-AOI Ch 0.2 http://discrete.openmathbooks.org/dmoi3/sec_intro-statements.html
* DM-AOI Ch 3.1 http://discrete.openmathbooks.org/dmoi3/sec_propositional.html
* MfCS Ch3-1-3.5 in  https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-spring-2015/readings/MIT6_042JS15_textbook.pdf
