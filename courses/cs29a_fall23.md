# CS29a Fall23 Brandeis University
This file contains links to course notes and homework for sections 1 and 2 of CS29a in Fall 2023

Homework will consist of readings (sometimes with reflections) and Mastery Learning App (MLA) problems.
The MLA Homework site is https://mastery.cs.brandeis.edu  with PIN 731541

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
# Week 0: 8/28-9/1

### Homework - due Wednesday 9/6/2023 before class
Read the following sections of two online books on Discrete Math
* DM-AOI Ch 0.2 http://discrete.openmathbooks.org/dmoi3/sec_intro-statements.html
* DM-AOI Ch 3.1 http://discrete.openmathbooks.org/dmoi3/sec_propositional.html
* MfCS [Ch3.1-3.5](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session4/)
and try some of the problems at the end of the sections. We will go over some of them in class on Monday.

## Lesson 1 Thu 8/31/2023  <br> _Intro and overview_

* We begin with
  - an overview of the course and
  - a discussion of why Math might be useful in CS, and what kinds of math would be most useful
* We ask everyhone to connect to the [Mastery Learning App](https://mastery.cs.brandeis.edu) with PIN 5074577
* We introduce Boolean Algebra and the Propositional Calculus  
  - We introduce the boolean operators AND, OR, NOT, IMPLIES, IFF, XOR, ONLYIF in this
    [overview of Propositional Logic](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/overview.md)
  - We get some practice in [converting between English and the Propoaitional Calculus](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/PropCalTranslation.md)

---

# Week 1: 9/4-9/8

### Homework - due Monday 9/11/2023 before class
Read 
* [Chapter 3.6: Predicate Formulas](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session5/) in MfCS
* Chapter 2 of PDM
* Chapter 8 of MFLP
  
Connect to the https://mastery.cs.brandeis.edu site with PIN 731541 and do all of the problems in the following problem sets:
* Translation to Propositional Logic
* Evaluation of Propositional Formulas
* Truth Tables

## Lesson 2 Wed 9/6/2023 <br> _Propositional Calculus and Boolean Algebra_
* We begin with a review of the [syntax of formulas in the propositional calculus]( https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/overview.md)
* Next we get [more practice converting propositional calculus to English and vice versa](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/PropCalTranslation.md)
* Next we show how to find the value of a propositional formula for particular values of its variables
  To do this we need to [create a parse tree for a formula, and then use that tree to evaluate the formula](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/PropCalcParseTree.md)



## Lesson 3 Thu 9/7/2023 <br>  _Truth Tables_
* We show how to [create a truth table](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TruthTables.md)
  for a formula, this shows its value for all possible interpretations of its variables.
* and we see [a few more examples of truth tables](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TruthTablePractice.md)
* We also show how to [use a Parse Tree to evaluate a Boolean formula on an interpretation](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/PropCalcParseTree.md)
* We show how to [estimate how long it would take to prove a formula is a tautology with the Truth Method](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/ComplexityOfSat.md)

---

# Week 2: 9/11-9/15

### Homework - due Monday 9/18/2023 before class
Read 
* [Chapter 3.6: Predicate Formulas](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session5/) in MfCS

Connect to the [MLA](https://mastery.cs.brandeis.edu) Homework site with PIN 731541 and do all of the problems due 9/18

## Lesson 4 Mon 9/11/2023 <br> _Inference_
* We review the [inference rules for Propositional Logic](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/InferenceRules.md) from
  [Chapter 3.4 of MfCS](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session4/)
and we show that every formula can be reduced to
  [Disjunctive Normal Form](https://en.wikipedia.org/wiki/Disjunctive_normal_form)
* We practice [simplifying formulas](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/SimplifyingFormulas.md) in general and  [simplifying negated formulas](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/SimplifyingNegations.md)  in particular.
  

## Lesson 5 Wed 9/13/2023 <br> _The Truth Tree Method for Propositional Logic_
* We give an introduction to [arguments, formal proofs, and counterexamples](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/SymbolicProofs.md)
* We give example of using the [Truth Tree method](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TruthTreeMethod.md) to prove Theorems and to find counter-examples and we describe the steps of the Truth Tree method and explain why they work

## Lesson 6 Thu 9/14/2023 <br> _More Truth Tree Method Practice_
* We give examples showing that [Truth Trees can be very efficient, or very inefficient!](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TruthTreePerformance.md)
* We work through [examples combining translation to English with Truth Trees](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TranslateAndInfer.md)

---

# Week 3: 9/18-9/22

### Homework - due Tuesday (Brandeis Monday) 9/26/2023 before class
Read 
* [Chapter 3.2: Proofs of DM-AOI](https://discrete.openmathbooks.org/dmoi3/sec_logic-proofs.html)
* [Chapter 1.1-1.6: What is a Proof of MfCS](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session1/) and [Chapter 1.7-1.9: Proof by Cases](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session2/)

Connect to the [MLA](https://mastery.cs.brandeis.edu) Homework site with PIN 731541 and do all of the problems due 9/25

## Lesson 7 Mon 9/18/2023 <br> _The Predicate Calculus_
* We give [an introduction to the Predicate Calculus](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/overview.md) as the language of Mathematics
* We look at [some examples of predicate calculus formulas in epidemiology](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/covid_examples.md)

## Lesson 8 Wed 9/20/2023 <br> _Simplification of First Order Formulas_
* We show how to [draw parse trees for First Order Formulas](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/parseTree.md).
* We show [how to evaluate a First Order Formula given an Interpretation](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/FOLinterpretations.md).



## Lesson 9 Thu 9/21/2023 <br> _Inference in First Order Logic_
* We give an overview of [the simplification rules in First Order Logic](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/simplification.md)
* We give [an example of translating an argument to the predicate calculus and simplifying the resulting argument](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/FOLtreemethodExample1.md).

---

# Week 4: 9/25-9/29

### Homework
To be announced

## Lesson 10 Tue 9/26/2023 <br> _Truth Trees for Predicate Calculus_
* We introduce the notion of [inference and valid arguments in the Predicate Calculus](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/inference.md)
* We show [how the Truth Tree method can be used in First Order Logic](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/truthTrees.md)

## Lesson 11 Wed 9/27/2023 <br> _More Truth Trees for Predicate Calculus_
* We get more practice using the Truth Tree method to show arguments are valid
  * using [these examples from the Logic Notes Book](https://users.cecs.anu.edu.au/~jks/LogicNotes/exercises3.html)
  * and looking at [the Peano Axiomatization of Arithmetic](https://github.com/tjhickey724/discrete_math/blob/main/notes/predicate_calculus/peanoAxioms.md).

## Lesson 12 Thu 9/28/2023 <br> _Intro to Proofs_
* We give an overview of [the art of writing mathematical proofs](https://github.com/tjhickey724/discrete_math/blob/main/notes/proofs/overview.md)


# Week 5: 10/2-10/6

### Homework
* Read Chapters 0.3 Sets and 0.4 Functions in [Discrete Math: An Open Introduction](https://discrete.openmathbooks.org/dmoi3/dmoi.html)
* Read Chapter 4: Mathematical Data Types of [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf)
* Optional Reading: Chapter 1: Sets of [Problems in Discrete Math](https://itk.ilstu.edu//faculty/chungli/DIS300/dis300v1.pdf)

## Lesson 13 Mon 10/2/2023 <br> _Practice with Proof Techniques_
* We complete the overview of [the art of writing mathematical proofs](https://github.com/tjhickey724/discrete_math/blob/main/notes/proofs/overview.md)
* We review [the features of a "good" proof](https://github.com/tjhickey724/discrete_math/blob/main/notes/proofs/goodProofFeatures.md) as explained in MfCS


## Lesson 14 Wed 10/4 <br> _Mathematical Notation_
* We first complete our overview of proof techniques by giving an interesting proof by cases
* We introduce some of the [standard mathematical notation](https://github.com/tjhickey724/discrete_math/blob/main/notes/proofs/mathNotation.md) used in Mathematica for Computer Science
* And we look at expressing [sums and products](https://github.com/tjhickey724/discrete_math/blob/main/notes/proofs/mathSumsProds.md) with this notation.

## Lesson 15 Thu 10/5 <br> _Well Ordering Principle and more notation_
* We begin by looking at the [Well Ordering principle](https://github.com/tjhickey724/discrete_math/blob/main/notes/proofs/wellOrdering.md) for proofs by contradiction
* Then we continue giving [more examples of proofs](https://github.com/tjhickey724/discrete_math/blob/main/notes/proofs/moreProofs.md), some using this new notation.

# Week 6: 10/8-12

### Homework
* Read Chapter 1 on Counting in [Discrete Math: An Open Introduction](https://discrete.openmathbooks.org/dmoi3/dmoi.html)

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


