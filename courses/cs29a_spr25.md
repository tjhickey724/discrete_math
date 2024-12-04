# CS29a Spring 2025 Discrete Structures 
## Instructor: Tim Hickey at Brandeis University

This file contains links to course notes and homework for CS29a in Spring 2025

## The Mastery Learning App
We will be using the Mastery Learning App [MLA](https://specsgradingapp.onrender.com)
for all work in this class including weekly exams and homework and daily in-class questions.
You can connect to the app using your Brandeis login and the following PIN ???????

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

---

# Lesson Notes

---
# Week 1: 1/14,17/25
### Motivation
This week we will give an overview of the course and start our first major topic
which is Propositional Logic and Boolean Algebra. 

Logic pervades all parts of computer
science from the boolean expressions in conditionals and loops, to proofs of the correctness
and efficiency of algorithms. This first week we will focus on the Propositional Logic which deals
with simple statements containing propositions that can be true or false. In the following two weeks
we will expand to first order logic that is the formal language of Mathematics. Every other section
of this course will rely on your ability to work with, and understand the meaning of, logical formulas.

### Homework - due Tuesday 1/14/25 before the first class
Read the following sections of two online books on Discrete Math
* DM-AOI Ch 0.2 http://discrete.openmathbooks.org/dmoi3/sec_intro-statements.html
* DM-AOI Ch 3.1 http://discrete.openmathbooks.org/dmoi3/sec_propositional.html
* MfCS [Ch3.1-3.5](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session4/)
and try some of the problems at the end of the sections. We will go over some of them in class on Monday.

## Lesson 1 Tue 1/14/2023  <br> _Intro and overview_

* We begin with
  - an overview of the course and
  - a discussion of why Math might be useful in CS, and what kinds of math would be most useful
* We ask everyone to connect to the [Mastery Learning App](https://mastery.cs.brandeis.edu) with PIN ???????
* We introduce Boolean Algebra and the Propositional Calculus  
  - We introduce the boolean operators AND, OR, NOT, IMPLIES, IFF, XOR, ONLYIF in this
    [overview of Propositional Logic](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/overview.md)
  - We get some practice in [converting between English and the Propoaitional Calculus](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/PropCalTranslation.md)




## Lesson 2 Fri 1/17 <br> _Propositional Calculus and Boolean Algebra_

* Next we show how to find the value of a propositional formula for particular values of its variables
  To do this we need to [create a parse tree for a formula, and then use that tree to evaluate the formula](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/PropCalcParseTree.md)
* We show how to [create a truth table](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TruthTables.md)
  for a formula, this shows its value for all possible interpretations of its variables.
* and we see [a few more examples of truth tables](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TruthTablePractice.md)
* We also show how to [use a Parse Tree to evaluate a Boolean formula on an interpretation](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/PropCalcParseTree.md)
* We show how to [estimate how long it would take to prove a formula is a tautology with the Truth Method](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/ComplexityOfSat.md)

---

# Week 2: 1/24  
(Tuesday is a Brandeis Monday)

### Homework - due Friday 1/24 before class
Read 
* [Chapter 3.6: Predicate Formulas](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session5/) in MfCS
* Chapter 2 of PDM
* Chapter 8 of MFLP
  
Connect to the MLA homework site and do all of the problems in the following problem sets:
* Translation to Propositional Logic
* Evaluation of Propositional Formulas
* Truth Tables

## Lesson 3 Fri 1/24 <br> _Inference_
* We review the [inference rules for Propositional Logic](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/InferenceRules.md) from
  [Chapter 3.4 of MfCS](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session4/)
and we show that every formula can be reduced to
  [Disjunctive Normal Form](https://en.wikipedia.org/wiki/Disjunctive_normal_form)
  and also to
  [Conjunctive Normal Form](https://en.wikipedia.org/wiki/Conjunctive_normal_form)
* We also show that conjunction and disjunction exhibit [a specific kind of duality](https://en.wikipedia.org/wiki/Conjunction/disjunction_duality)
* We practice [simplifying formulas](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/SimplifyingFormulas.md) in general and  [simplifying negated formulas](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/SimplifyingNegations.md)  in particular.

---
  
# Week 3: 1/28,1/31
### Motivation
This week we learn a graphical method for proving theorems in Propositional Logic.
Next week we'll show how to do this for First Order Logic.

### Homework - due Tuesday (Brandeis Monday) 1/28 before class
Read 
* [Chapter 3.2: Proofs of DM-AOI](https://discrete.openmathbooks.org/dmoi3/sec_logic-proofs.html)
* [Chapter 1.1-1.6: What is a Proof of MfCS](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session1/) and [Chapter 1.7-1.9: Proof by Cases](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session2/)

Connect to the MLA Homework site with PIN 731541 and do all of the Week 3 problems

## Lesson 4 Tue 1/28 <br> _The Truth Tree Method for Propositional Logic_
* We give an introduction to [arguments, formal proofs, and counterexamples](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/SymbolicProofs.md)
* We give example of using the [Truth Tree method](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TruthTreeMethod.md) to prove Theorems and to find counter-examples and we describe the steps of the Truth Tree method and explain why they work
* We give examples showing that [Truth Trees can be very efficient, or very inefficient!](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TruthTreePerformance.md)
* We work through [examples combining translation to English with Truth Trees](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TranslateAndInfer.md)







## Lesson 5 Fri 1/31 <br> _The Predicate Calculus_
* We give [an introduction to the Predicate Calculus](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/overview.md) as the language of Mathematics
* We look at [some examples of predicate calculus formulas in epidemiology](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/covid_examples.md)
* We show how to [draw parse trees for First Order Formulas](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/parseTree.md).
* We show [how to evaluate a First Order Formula given an Interpretation](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/FOLinterpretations.md).
---

# Week 4: 2/4, 2/7
### Motivation
This week we complete our study of logic by learning how to use the Tree Method to prove that
a formula follows from a set of assumptions, or to find a counter example.

### Homework
To be announced


## Lesson 6 Tue 2/4 <br> _Inference in First Order Logic_
* We give an overview of [the simplification rules in First Order Logic](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/simplification.md)
* We give [an example of translating an argument to the predicate calculus and simplifying the resulting argument](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/FOLtreemethodExample1.md).
* We introduce the notion of [inference and valid arguments in the Predicate Calculus](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/inference.md)
* We show [how the Truth Tree method can be used in First Order Logic](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/truthTrees.md)

## Lesson 7 Fri 2/7 <br> _More Truth Trees for Predicate Calculus_
* We get more practice using the Truth Tree method to show arguments are valid
  * using [these examples from the Logic Notes Book](https://users.cecs.anu.edu.au/~jks/LogicNotes/exercises3.html)
  * and looking at [the Peano Axiomatization of Arithmetic](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/peanoAxioms.md).




# Week 5: 2/11, 2/14

### Homework
* Read Chapters 0.3 Sets and 0.4 Functions in [Discrete Math: An Open Introduction](https://discrete.openmathbooks.org/dmoi3/dmoi.html)
* Read Chapter 4: Mathematical Data Types of [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf)
* Optional Reading: Chapter 1: Sets of [Problems in Discrete Math](https://itk.ilstu.edu//faculty/chungli/DIS300/dis300v1.pdf)

## Lesson 8 Tue 2/11 <br> _Intro to Proofs_
* We give an overview of [the art of writing mathematical proofs](https://github.com/tjhickey724/discrete_math/blob/main/notes/proofs/overview.md)
* We review [the features of a "good" proof](https://github.com/tjhickey724/discrete_math/blob/main/notes/proofs/goodProofFeatures.md) as explained in MfCS


## Lesson 9 Fri 2/14 <br> _Mathematical Notation_
* We first complete our overview of proof techniques by giving an interesting proof by cases
* We introduce some of the [standard mathematical notation](https://github.com/tjhickey724/discrete_math/blob/main/notes/proofs/mathNotation.md) used in Mathematica for Computer Science
* And we look at expressing [sums and products](https://github.com/tjhickey724/discrete_math/blob/main/notes/proofs/mathSumsProds.md) with this notation.

# Vacation Week 2/17-2/21

# THE REST OF THIS PAGE HAS NOT YET BEEN PROCESSED

# Week 6: 2/25, 2/28

### Homework
* Read Chapter 1 on Counting in [Discrete Math: An Open Introduction](https://discrete.openmathbooks.org/dmoi3/dmoi.html)


## Lesson 15 Thu 10/5 <br> _Well Ordering Principle and more notation_
* We begin by looking at the [Well Ordering principle](https://github.com/tjhickey724/discrete_math/blob/main/notes/proofs/wellOrdering.md) for proofs by contradiction
* Then we continue giving [more examples of proofs](https://github.com/tjhickey724/discrete_math/blob/main/notes/proofs/moreProofs.md), some using this new notation.



## Lesson 16 Wed 10/11 <br> _Sets and Sequences_
* We begin with an introduction to the [mathematical data types](https://github.com/tjhickey724/discrete_math/blob/main/notes/math_data_types/overview.md) including Sets and Sequences

## Lesson 17 Thu 10/12/<br> _Functions and Relations_
* We continue our investigation fo [mathematical data types](https://github.com/tjhickey724/discrete_math/blob/main/notes/math_data_types/overview.md) with Sets and Sequences

# Week 7: 10/16-20 

### Homework
* read Chapter 1 on Counting in [Discrete Math: An Open Introduction](https://discrete.openmathbooks.org/dmoi3/dmoi.html)
* read Chapter 14 on Counting in  MfCS: [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf) by _Lehman, Leighton, and Meyer_
* complete the new problems on the MLA Homework site

## Lesson 18 Mon 10/16 <br> _Functions, and Counting_
* We continue our investigation fo [mathematical data types](https://github.com/tjhickey724/discrete_math/blob/main/notes/math_data_types/overview.md)

## Lesson 19: Wed 10/18 <br> _Binary Representation and Countability_
* First we look at [binary numbers](https://github.com/tjhickey724/discrete_math/blob/main/notes/math_data_types/binaryNumbers.md)
* Then we learn about [countable and uncountable infinite sets](https://github.com/tjhickey724/discrete_math/blob/main/notes/math_data_types/countableSets.md)

## Lesson 20: Thu 10/19 <br> _Counting_
* First we complete our introduction to [countable and uncountable infinite sets](https://github.com/tjhickey724/discrete_math/blob/main/notes/math_data_types/countableSets.md)
* then we begin our study of [counting and combinatorics](https://github.com/tjhickey724/discrete_math/blob/main/notes/counting/overview.md)

# Week 8: 10/23-27
### Homework due 10/29
* Complete the new MLA homework problems on Counting
* Read [Chapter 2 of  Discrete Math: An Open Introduction by Oscar Levin](https://discrete.openmathbooks.org/dmoi3/ch_sequences.html)

## Lesson 21: Mon 10/23 <br> _Combinations and Permutations_
* we continue our study of [counting and combinatorics](https://github.com/tjhickey724/discrete_math/blob/main/notes/counting/overview.md)

## Lesson 22: Wed 10/25 <br> _Counting Practice;  Stars and Bars_
* we continue our study of [counting and combinatorics](https://github.com/tjhickey724/discrete_math/blob/main/notes/counting/overview.md)

## Lesson 23: Thu 10/26 <br> _Stars and Bars_
* we continue our study of [counting and combinatorics](https://github.com/tjhickey724/discrete_math/blob/main/notes/counting/overview.md)

# Week 9: 10/30-11/3

### Howework due 11/6
* Read Chapters 15 _Generating Functions_, Chapter 16 _Events and Probability Spaces_ and Chapter 17 _Conditional Probability_ from [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf) by _Lehman, Leighton, and Meyer_
* Read [Chapter 5.1 from  Discrete Math: An Open Introduction by Oscar Levin](https://discrete.openmathbooks.org/dmoi3/sec_addtops-genfun.html)
* Complete the Homework assignments on MLA which are due on 11/6

## Lesson 24: Mon 10/30 <br> _Polynomial Sequences_
* we begin our investigation of [sequences](https://github.com/tjhickey724/discrete_math/blob/main/notes/sequences/overview.md)
  by looking at [polynomial sequences](https://github.com/tjhickey724/discrete_math/blob/main/notes/sequences/polynomial_sequences.md)

## Lesson 25: Wed 11/1 <br> _Exponential Sequences_
* we begin our investigation of [sequences](https://github.com/tjhickey724/discrete_math/blob/main/notes/sequences/overview.md)
  by looking at linear [recurrence relations and exponential sequences](https://github.com/tjhickey724/discrete_math/blob/main/notes/sequences/exponential_sequences.md).

## Lesson 26: Thu 11/2 <br> _Induction_
* We introduce the concept of Proof by [Induction](https://github.com/tjhickey724/discrete_math/blob/main/notes/sequences/induction.md)
   and use it to prove closed form expression for series elements defined recursively are correct.

# Week 10: 11/6-10 - Probability

### Homework - due Monday 11/13/2023 before class
Skim the following sections of two online books on Discrete Math
* [DM-AOI Ch 4](https://discrete.openmathbooks.org/dmoi3/ch_graphtheory.html)
* [MfCS Ch9](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session4/)

and complete the homework problems on the MLA due on Monday.

## Lesson 27: Mon 11/6 <br> _Induction and Generating Functions_
* We finish up our study of [sequences](https://github.com/tjhickey724/discrete_math/tree/main/notes/sequences)
* We give some examples of recursion equations that arise in the study of algorithms (Priority Queues and AVL Trees)
* We give a brief introduction to Generating Functions

## Lesson 28: Wed 11/8 <br> _Probability and the 4 step method_
* We begin our study of [probability](https://github.com/tjhickey724/discrete_math/blob/main/notes/probability/overview.md)

## Lesson 29: Wed 11/9 <br> _Conditional Probability, Expected Values, and Random Variables_
* We conclude our study of [probability](https://github.com/tjhickey724/discrete_math/blob/main/notes/probability/overview.md)

# Week 11: 11/13-17 - Graph Theory

## Lesson 30: Mon 11/13 <br> _Prob Review_
* We review Question 20 on exam 8 about Advanced Counting
* We show how to calculate the expected number of rolls in a game of Craps (3.37575...)
  
## Lesson 31: Wed 11/15 <br> _Graphs_
* We begin our study of [Graph Theory ](../notes/graph_theory/overview.md)

## Lesson 32: Thu 11/16 <br> _More Graphs_
* We continue our study of [Graph Theory ](../notes/graph_theory/overview.md)

# Week 12: 11/27-12/1 - Number Theory

## Lesson 34 Cryptography
[Crypto](../notes/cryptograph/overview.md)

## Lesson 35 RSA
[Crypto](../notes/cryptograph/overview.md)

## Lesson 36 more RSA
[Crypto](../notes/cryptograph/overview.md)

# Week 13: 12/4-12/8
## Lesson 37 and 38
[Analysis of Algorithms](../notes/algorithmicAnalysis/overview.md)

## Lesson 39
[Quicksort Analysis](../notes/algorithmicAnalysis/quicksort.md)

