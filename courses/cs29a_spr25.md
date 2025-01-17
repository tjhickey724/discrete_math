# CS29a Spring 2025 Discrete Structures 
## Instructor: Tim Hickey at Brandeis University

This file contains links to course notes and homework for CS29a in Spring 2025

---

# Lesson Notes
* [Course Overview](#course-overview)
* [Week 1](#week-1)
  * [Week 1 Homework 1](#Homework01)
  * [Lesson 1: Tue 1/14 Intro and Overview](#lesson-1) [F01](#F01) [F02](#F02) [F03](#F03)
  * [Lesson 2: Fri 1/17 Propositional Calculus and Boolean Algebra](#lesson-2) [F01](#F01) [F02](#F02) [F03](#F03)
* [Week 2](#week-2)
  * [Week 1 Homework 2](#Homework02)
  * [Lesson 3: Fri 1/25 Inference](#lesson-3) [F04](#F04)
* [Week 3](#week-3)
  * [Lesson 4: Tue 1/28 The Truth Tree Method for Propositional Logic](#lesson-4) [G01](#G01)
  * [Lesson 5: Fri 1/31 The Predicate Calculus](#lesson-5)  [F04](#F04) [F05](#F05) [F06](#F06)
* Later Weeks (4-14)
  * [Lesson 6: Inference in First Order Logic - F07](#lesson-6)
  * [Lesson 7: Truth Trees for Predicate Calculus - G02](#lesson-7)
  * [Lesson 8: Intro to Proofs - F08,F09,F10,F11](#lesson-8)
  * [Lesson 9: Mathematical Notation - F08](#lesson-9)
  * [Lesson 10: Well-Ordering Principle - F09,G03](#lesson-10)
  * [Lesson 11: Sets, Sequences, and Countability - F12,F13,F14,F22,G03](#lesson-11)
  * [Lesson 12: Functions and Relations - F15,F16,F17](#lesson-12)
  * [Lesson 13: Counting - F18](#lesson-13)
  * [Lesson 14: Combinations, Permutations, and PIE - F19,F20](#lesson-14)
  * [Lesson 15: Advanced Methods, Pigeons, Isomorphisms - F21,G06](#lesson-15)
  * [Lesson 16: Polynomial and Exponential Sequences - F23](#lesson-16)
  * [Lesson 17: Induction and Generating Functions- F11,G04,G05](#lesson-17)
  * [Lesson 18: Probability and the 4 Step Method - F24](#lesson-18)
  * [Lesson 19: Expected Values - F25](#lesson-19)
  * [Lesson 20: Advanced Counting - G06](#lesson-20)
  * [Lesson 21: Graph Theory - F26,G07,G08](#lesson-21)
  * [Lesson 22: Number Theory - F27,G09](#lesson-22)
  * [Lesson 23: Cryptography - F27](#lesson-23)


We will reserve the last few lessons (24,25,26) as slack space so we can spend more time on 
earlier lessons if needed.


# Course Overview
## The Mastery Learning App
We will be using the Mastery Learning App [MLA](https://masterylearningapp.onrender.com)
for all work in this class including weekly exams and homework and daily in-class questions.
When you register for the course you will be added to the app;

## Textbooks 
Most of our readings will come from the follwoing online books:
* DM-AOI:
  [Discrete Math: An Open Introduction](https://discrete.openmathbooks.org/dmoi3/dmoi.html) by _Oscar Levin_
* MfCS: [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf) by _Lehman, Leighton, and Meyer_
   <br> also available as a 
  [website](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/)
  
## Additional Texts
* PDM: [Problems in Discrete Math](https://itk.ilstu.edu//faculty/chungli/DIS300/dis300v1.pdf)
  by _Chung-Chih Li and Kishan Mehrotra_
* MFLP: [A Modern Formal Logic Primer](https://tellerprimer.ucdavis.edu/)
  by _Paul Teller_ 
* TLN: [The Logic Notes](https://users.cecs.anu.edu.au/~jks/LogicNotes/index.html)
  by _John Slaney_
* LibreTexts: [Free and Open Source Discrete Math Textbooks](https://math.libretexts.org/Bookshelves/Combinatorics_and_Discrete_Mathematics)

---



---
# Week 1
### 1/14,17/25
#### Motivation
This week we will give an overview of the course and start our first major topic
which is Propositional Logic and Boolean Algebra. 

Logic pervades all parts of computer
science from the boolean expressions in conditionals and loops, to proofs of the correctness
and efficiency of algorithms. This first week we will focus on the Propositional Logic which deals
with simple statements containing propositions that can be true or false. In the following two weeks
we will expand to first order logic that is the formal language of Mathematics. Every other section
of this course will rely on your ability to work with, and understand the meaning of, logical formulas.

### Homework01
#### due Tuesday 1/21/25 
Read the following sections of two online books on Discrete Math
* DM-AOI Ch 0.2 http://discrete.openmathbooks.org/dmoi3/sec_intro-statements.html
* DM-AOI Ch 3.1 http://discrete.openmathbooks.org/dmoi3/sec_propositional.html
* MfCS [Ch3.1-3.5](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session4/)
and try some of the problems at the end of the sections. We will go over some of them in class.

Then answer the Week 1 problems on the MLA Homework site

## Lesson 1
### Tue 1/14/2023  <br> _Intro and overview_

* We begin with
  - an overview of the course and
  - a discussion of why Math might be useful in CS, and what kinds of math would be most useful
* We ask everyone to connect to the [Mastery Learning App](https://masterylearningapp.onrender.com), if you have registered for the course you will see the CS29a appear on the MLA when you log in with your Brandeis ID.
* We introduce Boolean Algebra and the Propositional Calculus  
  - We introduce the boolean operators AND, OR, NOT, IMPLIES, IFF, XOR, ONLYIF in this
    [overview of Propositional Logic](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/overview.md)
* We show how to [create a truth table](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TruthTables.md)
  for a formula, this shows its value for all possible interpretations of its variables.
* and we see [a few more examples of truth tables](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TruthTablePractice.md)
* We get some practice in [converting between English and the Propositional Calculus](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/PropCalTranslation.md)


## Lesson 2 
### Fri 1/17 <br> _Propositional Calculus and Boolean Algebra_

* Next we show how to find the value of a propositional formula for particular values of its variables
  To do this we need to [create a parse tree for a formula, and then use that tree to evaluate the formula](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/PropCalcParseTree.md)
* We also show how to [use a Parse Tree to evaluate a Boolean formula on an interpretation](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/PropCalcParseTree.md)
* We show how to [estimate how long it would take to prove a formula is a tautology with the Truth Method](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/ComplexityOfSat.md)
* We review the [inference rules for Propositional Logic](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/InferenceRules.md) from
  [Chapter 3.4 of MfCS](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session4/)
and we show that every formula can be reduced to
  [Disjunctive Normal Form](https://en.wikipedia.org/wiki/Disjunctive_normal_form)
  and also to
  [Conjunctive Normal Form](https://en.wikipedia.org/wiki/Conjunctive_normal_form)
---

# Week 2
### Fri 1/24 (Tuesday is a Brandeis Monday)

### Homework02
#### due Friday 1/24 before class
Read 
* [Chapter 3.6: Predicate Formulas](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session5/) in MfCS
* Chapter 2 of PDM
* Chapter 8 of MFLP
  
Connect to the MLA homework site and do all of the Week 2 problems.


## Lesson 3 
### Fri 1/24 <br> _Inference_
* We also show that conjunction and disjunction exhibit [a specific kind of duality](https://en.wikipedia.org/wiki/Conjunction/disjunction_duality)
* We practice [simplifying formulas](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/SimplifyingFormulas.md) in general and  [simplifying negated formulas](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/SimplifyingNegations.md)  in particular.
* We give an introduction to [arguments, formal proofs, and counterexamples](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/SymbolicProofs.md)
* We give example of using the [Truth Tree method](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TruthTreeMethod.md) to prove Theorems and to find counter-examples and we describe the steps of the Truth Tree method and explain why they work

---
  
# Week 3
### 1/28,1/31
#### Motivation
This week we learn a graphical method for proving theorems in Propositional Logic.
Next week we'll show how to do this for First Order Logic.

### Homework - due Tuesday (Brandeis Monday) 1/28 before class
Read 
* [Chapter 3.2: Proofs of DM-AOI](https://discrete.openmathbooks.org/dmoi3/sec_logic-proofs.html)
* [Chapter 1.1-1.6: What is a Proof of MfCS](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session1/) and [Chapter 1.7-1.9: Proof by Cases](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session2/)

Connect to the MLA Homework site with PIN 731541 and do all of the Week 3 problems

## Lesson 4 
### Tue 1/28 <br> _The Truth Tree Method for Propositional Logic_
* We give examples showing that [Truth Trees can be very efficient, or very inefficient!](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TruthTreePerformance.md)
* We work through [examples combining translation to English with Truth Trees](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TranslateAndInfer.md)







## Lesson 5 
### Fri 1/31 <br> _The Predicate Calculus_
* We give [an introduction to the Predicate Calculus](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/overview.md) as the language of Mathematics
* We look at [some examples of predicate calculus formulas in epidemiology](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/covid_examples.md)
* We show how to [draw parse trees for First Order Formulas](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/parseTree.md).
* We show [how to evaluate a First Order Formula given an Interpretation](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/FOLinterpretations.md).
---

# Week 4
### 2/4, 2/7

#### Motivation
This week we complete our study of logic by learning how to use the Tree Method to prove that
a formula follows from a set of assumptions, or to find a counter example.

### Homework
To be announced


## Lesson 6 
### Tue 2/4 <br> _Inference in First Order Logic_
* We give an overview of [the simplification rules in First Order Logic](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/simplification.md)
* We give [an example of translating an argument to the predicate calculus and simplifying the resulting argument](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/FOLtreemethodExample1.md).
* We introduce the notion of [inference and valid arguments in the Predicate Calculus](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/inference.md)
* We show [how the Truth Tree method can be used in First Order Logic](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/truthTrees.md)

## Lesson 7 
### Fri 2/7 <br> _More Truth Trees for Predicate Calculus_
* We get more practice using the Truth Tree method to show arguments are valid
  * using [these examples from the Logic Notes Book](https://users.cecs.anu.edu.au/~jks/LogicNotes/exercises3.html)
  * and looking at [the Peano Axiomatization of Arithmetic](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/peanoAxioms.md).




# Week 5
### 2/11, 2/14

### Homework
* Read Chapters 0.3 Sets and 0.4 Functions in [Discrete Math: An Open Introduction](https://discrete.openmathbooks.org/dmoi3/dmoi.html)
* Read Chapter 4: Mathematical Data Types of [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf)
* Optional Reading: Chapter 1: Sets of [Problems in Discrete Math](https://itk.ilstu.edu//faculty/chungli/DIS300/dis300v1.pdf)

## Lesson 8 
### Tue 2/11 <br> _Intro to Proofs_
* We give an overview of [the art of writing mathematical proofs](https://github.com/tjhickey724/discrete_math/blob/main/notes/proofs/overview.md)
* We review [the features of a "good" proof](https://github.com/tjhickey724/discrete_math/blob/main/notes/proofs/goodProofFeatures.md) as explained in MfCS
* Then we complete our overview of proof techniques by giving an interesting proof by cases

## Lesson 9 
### Fri 2/14 <br> _Mathematical Notation_
* We introduce some of the [standard mathematical notation](https://github.com/tjhickey724/discrete_math/blob/main/notes/proofs/mathNotation.md) used in Mathematica for Computer Science
* And we look at expressing [sums and products](https://github.com/tjhickey724/discrete_math/blob/main/notes/proofs/mathSumsProds.md) with this notation.
* Next we look at [binary numbers](https://github.com/tjhickey724/discrete_math/blob/main/notes/math_data_types/binaryNumbers.md)


# Vacation Week 2/17-2/21

# Week 6
### 2/25, 2/28

### Homework
* Read Chapter 1 on Counting in [Discrete Math: An Open Introduction](https://discrete.openmathbooks.org/dmoi3/dmoi.html)


## Lesson 10
###  2/25 _Well Ordering Principle and more notation_
* We begin by looking at the [Well Ordering principle](https://github.com/tjhickey724/discrete_math/blob/main/notes/proofs/wellOrdering.md) for proofs by contradiction
* Then we continue giving [more examples of proofs](https://github.com/tjhickey724/discrete_math/blob/main/notes/proofs/moreProofs.md), some using this new notation.



## Lesson 11 
###  2/28 _Sets, Sequences, and Countability_
* We begin with an introduction to the [mathematical data types](https://github.com/tjhickey724/discrete_math/blob/main/notes/math_data_types/overview.md) including Sets and Sequences
* Then we learn about [countable and uncountable infinite sets](https://github.com/tjhickey724/discrete_math/blob/main/notes/math_data_types/countableSets.md)

# Week 7
### 3/4,3/7 

### Homework
* read Chapter 1 on Counting in [Discrete Math: An Open Introduction](https://discrete.openmathbooks.org/dmoi3/dmoi.html)
* read Chapter 14 on Counting in  MfCS: [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf) by _Lehman, Leighton, and Meyer_
* complete the new problems on the MLA Homework site

## Lesson 12 
### Thu 3/4/<br> _Functions and Relations_
* We continue our investigation fo [mathematical data types](https://github.com/tjhickey724/discrete_math/blob/main/notes/math_data_types/overview.md) with Functions and Relations


## Lesson 13
### Thu 3/7 <br> _Counting_
* First we complete our introduction to [countable and uncountable infinite sets](https://github.com/tjhickey724/discrete_math/blob/main/notes/math_data_types/countableSets.md)
* then we begin our study of [counting and combinatorics](https://github.com/tjhickey724/discrete_math/blob/main/notes/counting/overview.md)


# Week 8
### 3/11-14
### Homework due 10/29
* Complete the new MLA homework problems on Counting
* Read [Chapter 2 of  Discrete Math: An Open Introduction by Oscar Levin](https://discrete.openmathbooks.org/dmoi3/ch_sequences.html)

## Lesson 14
### Tue 3/11 <br> _Combinations, Permutations, Principle of Inclusion and Exclusion_
* we continue our study of [counting and combinatorics](https://github.com/tjhickey724/discrete_math/blob/main/notes/counting/overview.md)

## Lesson 15
### Fri 3/14 <br> _Advanced Methods, Pigeon Hole Principle, Isomorphism_
* we continue our study of [counting and combinatorics](https://github.com/tjhickey724/discrete_math/blob/main/notes/counting/overview.md)

# Week 9
### 3/18-21

### Howework due 11/6
* Read Chapters 15 _Generating Functions_, Chapter 16 _Events and Probability Spaces_ and Chapter 17 _Conditional Probability_ from [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf) by _Lehman, Leighton, and Meyer_
* Read [Chapter 5.1 from  Discrete Math: An Open Introduction by Oscar Levin](https://discrete.openmathbooks.org/dmoi3/sec_addtops-genfun.html)
* Complete the Homework assignments on MLA which are due on 11/6

## Lesson 16
### Tue 3/18 <br> _Polynomial and Exponential Sequences_
* we begin our investigation of [sequences](https://github.com/tjhickey724/discrete_math/blob/main/notes/sequences/overview.md)
  by looking at [polynomial sequences](https://github.com/tjhickey724/discrete_math/blob/main/notes/sequences/polynomial_sequences.md)
* next we look at linear [recurrence relations and exponential sequences](https://github.com/tjhickey724/discrete_math/blob/main/notes/sequences/exponential_sequences.md).

## Lesson 17
### Fri 3/21 <br> _Induction_
* We introduce the concept of Proof by [Induction](https://github.com/tjhickey724/discrete_math/blob/main/notes/sequences/induction.md)
   and use it to prove closed form expression for series elements defined recursively are correct.

# Week 10
### 3/25-28 - Probability

### Homework - due Monday 11/13/2023 before class
Skim the following sections of two online books on Discrete Math
* [DM-AOI Ch 4](https://discrete.openmathbooks.org/dmoi3/ch_graphtheory.html)
* [MfCS Ch9](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session4/)

and complete the homework problems on the MLA due on Monday.

## Lesson 18
### Tue 3/25 <br> _Induction and Generating Functions_
* We finish up our study of [sequences](https://github.com/tjhickey724/discrete_math/tree/main/notes/sequences)
* We give some examples of recursion equations that arise in the study of algorithms (Priority Queues and AVL Trees)
* We give a brief introduction to Generating Functions

## Lesson 19
### Fri 3/28 <br> _Probability and the 4 step method_
* We begin our study of [probability](https://github.com/tjhickey724/discrete_math/blob/main/notes/probability/overview.md)

# Week 11
### 4/1-4 - Graph Theory

## Lesson 20
### Tue 4/1 <br> _Advanced Counting_
* We show how to calculate the expected number of rolls in a game of Craps (3.37575...)
  
## Lesson 21
### Fri 4/4 <br> _Graphs_
* We begin our study of [Graph Theory ](../notes/graph_theory/overview.md)


# Week 12
### 4/8-11 - Number Theory

## Lesson 22 Cryptography
[Crypto](../notes/cryptograph/overview.md)

## Lesson 23 RSA
[Crypto](../notes/cryptograph/overview.md)


# Week 13
### 4/22-25

## Lesson 24
[Analysis of Algorithms](../notes/algorithmicAnalysis/overview.md)

## Lesson 25
[Quicksort Analysis](../notes/algorithmicAnalysis/quicksort.md)

# Week 14
## 4/29

# Skills
## F01
### Propositional Logic: Syntax and Semantics 
Ability to evaluate a propositional formula given a True/False interpretation for the propositions in the formula. This also requires the ability to recognize whether a formula is syntactically correct and to be able to draw a parse tree for an expression and evaluate the truth value at every node. We assume that the grammar uses the standard logical operators: AND, OR, NOT, IMPLIES, IFF, XOR both in English and in traditional Mathematical notation.
## F02
### Propositional Logic: Truth Tables and Satisfiability 
Ability to determine if a Propositional formula is a tautology, or is satisfiable, or is unsatisfiable by creating a Truth Table with a column for each variable and operator in the formula.

## F03
### Propositional Logic: Translation to/from English 
Ability to translate English statements into Propositional Formulas and to translate Propositional formulas into plain English.

## F04
### Propositional Logic: Boolean Algebra 
The ability to apply the rules of boolean algebra to transform propositional formulas into equivalent formulas. In particular, to be able to * convert a formula to Conjunctive Normal Form or Disjunctive Normal Form * move all negations down to the propositional symbols * convert a formula so it only uses and, or, and not.

## F05
### Predicate Calculus: Syntax and Semantics 
Ability to understand the basic syntax and semantics of first order logic. In particular, to be able to * draw a parse tree of a first order sentence or show it is not syntactically correct * evaluate the truth or falsity of a first order sentence for a specific model of the language and either give a counterexample or explain why it is true

## F06
### Predicate Calculus: Translation to/from English 
The ability to translate English statements about a particular model into First Order Logic, and vice versa.

## F07
### Predicate Calculus: Simplification Rules 
The ability to apply simplification rules to produce logically equivalent first order sentences. In particular, the ability to * move negation inwards * move formulas in and out of the scope of quantifiers as appropriate * move quantifiers to the beginning of the sentences

## F08
### Proof Techniques: Direct and ContraPositive Proofs 
Ability to write a well-structured proof of a Theorem, Proposition, Lemma or Corollary using one of the standard proof techniques: * direct proof * proof of contrapositive

## F09
### Proof Techniques: Proof by Contradiction 
Ability to write a well-structured proof of a Theorem, Proposition, Lemma or Corollary using a proof by contradiction.

## F10
### Proof Techniques: Proof by Cases 
Ability to write a well-structured proof of a Theorem, Proposition, Lemma or Corollary by dividing it into cases which are proved individually.

## F11
### Proof Techniques: Induction 
Ability to write a well-structured proof of a Theorem, Proposition, Lemma or Corollary using induction.

## F12
### Sets: Syntax and Semantics 
Ability to work with modern set notation. In particular, the ability to perform calculations using the union, intersection, and complement of sets.

## F13
### Sets: Algebra 
Ability to using Boolean algebra to reason about sets. In particular, * to simplify formulas using boolean algebra laws * to prove (or disprove) logical inferences about set formulas

## F14
### Sets: Categorical Operations 
The ability to work with the sum, product and powerset operators on sets. In particular * to calculate the sizes of sets formed using these operators * to verify if a particular element is a member of such a set (e.g. P(XxY^2) for finite sets X,Y)

## F15
### Functions: Syntax and Semantics 
Ability to use and understand mathematical notation for functions. In particular, * to calculate values of compositions of given functions * to compute the images and inverse images of a given function on subsets of the domain or codomain * to work with function defined by cases, or by mathematical formulas, or both

## F16
### Functions: Composition 
The ability to compute and reason about compositions of functions In particular, * to calculate the values of a function formed by composing functions on products, powersets, sums, etc. * to calculate the image and inverse image of sets defined by compositions

## F17
### Functions: Properties 
The ability to categorize functions and prove properties of functions. In particular, * to show that a given function is (or is not) partial/total, injective, surjective, bijective * to prove properties of compositions and inverses of functions based on properties of the individual functions * to show that two sets are isomorphic by defining a bijection between them

## F18
### Combinatorics: Addition and Multiplication Principles 
Ability to apply the addition and multiplication principles to find the sizes of specified sets.

## F19
### Combinatorics: Permutations and Combinations 
Counting the sizes of sets defined using permutations and combinations of elements

## F20
### Combinatorics: Principle of Inclusion and Exclusion 
Ability to count the sizes of sets defined intersections and unions of larger sets.

## F21
### Combinatorics: Pigeonhole Principle 
Ability to prove that a function is not an injection by calculating the sizes of the domain and codomain.

## F22
### Sequences: Syntax and Semantics 
The ability to calculate sequences defined with mathematical notation. In particular, to calculate the n-th element of * a linear sequence * a polynomial sequence * a geometric sequence * a sequence defined by a sum of products or polynomials and exponentials * to calculate the first N terms of a sequence defined by recursion equations.

## F23
### Sequences: Polynomial Fitting and Difference Tests 
The ability to use the difference test and polynomial fitting for sequences. In particular, * to show that a sequence is not polyomial of degree d using the difference test * to use polynomial fitting to find the coefficients of a polynimial sequence of degree d.

## F24
### Probability: Events and Probability Spaces 
Ability to calculate the probability of some event using the "4 step method" This involves * finding the probability space (typically drawing an event tree) * find the events of interest * find the probability of each event * summing the probabilities of the events of interest

## F25
### Probability: Expected Value 
The ability to calculate the expected value of some function on a probability space.

## F26
### Graph Theory: Basic Properties 
Ability to convert between different representations of graphs and to understand basic graph vocabulary.

## F27
### Number Theory: Congruence 
Ability to do computations in the rings Z/nZ and to prove properties of such rings

## G01
### Propositional Logic: Inference: Truth Trees 
Ability to use the Truth Tree Method to determine if a logical inference is valid, or to find a counter example if not. References: * Teller Logic Primer, Chapters 8,9 https://tellerprimer.ucdavis.edu/logic-primer-files

## G02
### Predicate Calculus: Inference: Truth Trees 
The ability to verify that a first order sentence is a logical consequence of a set of first order sentences by using the Tree Method. In particular, to be able to * skolemize a set of formulas while preserving satisfiability * apply the truth tree method to show that a set of sentences is unsatisfiable in any model

## G03
### Proof Techniques: Combinations 
Ability to write a well-structured proof of a Theorem, Proposition, Lemma or Corollary using a combination of the following basic techniques: * direct proof * proof of contrapositive * proof by contradiction (possibly using the well-ordering principle) * proof by cases * proof by induction

## G03
### Sets: Countability 
The ability to prove that an infinite set is, or is not, countable.

## G04
### Sequences: Closed Forms for Linear Recurrences 
The ability to find a closed form for a homogenous linear recurrence with constant coefficients. This involves find and solving the characteristic equation and using polyomial fitting.

## G05
### Sequences: Closed Forms using Generating Functions 
The ability to use Generating Functions to find closed form solutions to recurrence equations.

## G06
### Combinatorics: Advanced 
Ability to determine the size of a set using a combination of the techniques covered in this course.

## G07
### Graph Theory: Digraphs, DAGs and Equivalence Relations 
Ability to calculate the equivalence classes of a relation defined by a digraph D and form the related DAG D'

## G08
### Graph Theory: DFAs, NFAs, and Regular Languages 
Ability to convert an NFA to a DFA and to use DFAs and NFAs to recognized regular languages.

## G09
### Number Theory: RSA 
Ability to understand and apply the RSA algorithm to create public/private keys and to encrypt/decrypt.
