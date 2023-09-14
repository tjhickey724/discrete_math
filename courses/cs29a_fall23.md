# CS29a Fall23 Brandeis University
This file contains links to course notes and homework for sections 1 and 2 of CS29a in Fall 2023

---

# Lesson Notes
We will provide notes on each lesson below.
---
# Week 0

## Lesson 1 Thu 8/31/2023  _Intro and overview_
* We begin with
  - an overview of the course and
  - a discussion of why Math might be useful in CS, and what kinds of math would be most useful
* We ask everyhone to connect to the [Mastery Learning App](https://mastery.cs.brandeis.edu) with PIN 5074577
* We introduce Boolean Algebra and the Propositional Calculus  
  - We introduce the boolean operators AND, OR, NOT, IMPLIES, IFF, XOR, ONLYIF in this
    [overview of Propositional Logic](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/overview.md)
  - We get some practice in [converting between English and the Propoaitional Calculus](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/PropCalTranslation.md)
---
# Week 1

## Lesson 2 Wed 9/6/2023 __Propositional Calculus and Boolean Algebra__
* We begin with a review of the [syntax of formulas in the propositional calculus]( https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/overview.md)
* Next we get [more practice converting propositional calculus to English and vice versa](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/PropCalTranslation.md)
* Next we show how to find the value of a propositional formula for particular values of its variables
  To do this we need to [create a parse tree for a formula, and then use that tree to evaluate the formula](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/PropCalcParseTree.md)



## Lesson 3 Thu 9/7/2023 - Truth Tables
* We show how to [create a truth table](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TruthTables.md)
  for a formula, this shows its value for all possible interpretations of its variables.
* and we see [a few more examples of truth tables](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TruthTablePractice.md)
* We also show how to [use a Parse Tree to evaluate a Boolean formula on an interpretation](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/PropCalcParseTree.md)
* We show how to [estimate how long it would take to prove a formula is a tautology with the Truth Method](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/ComplexityOfSat.md)
---

# Week 2

## Lesson 4 Mon 9/11/2023 - Inference
* We review the [inference rules for Propositional Logic](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/InferenceRules.md) from
  [Chapter 3.4 of MfCS](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session4/)
and we show that every formula can be reduced to
  [Disjunctive Normal Form](https://en.wikipedia.org/wiki/Disjunctive_normal_form)
* We practice [simplifying formulas](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/SimplifyingFormulas.md) in general and  [simplifying negated formulas](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/SimplifyingNegations.md)  in particular.
  

## Lesson 5 Wed 9/13/2023 - The Truth Tree Method for Propositional Logic
* We give an introduction to [arguments, formal proofs, and counterexamples](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/SymbolicProofs.md)
* We give example of using the [Truth Tree method](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TruthTreeMethod.md) to prove Theorems and to find counter-examples and we describe the steps of the Truth Tree method and explain why they work

## Lesson 6 Thu 9/14/2023 - More Truth Tree Method Practice
* We give examples showing that [Truth Trees can be very efficient, or very inefficient!](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TruthTreePerformance.md)
* We work through [examples combining translation to English with Truth Trees](https://github.com/tjhickey724/discrete_math/blob/main/notes/propositional_calculus/TranslateAndInfer.md)


---

# Homework
Homework will consist of readings (sometimes with reflections) and Mastery Learning App (MLA) problems.
The MLA Homework site is https://mastery.cs.brandeis.edu  with PIN 731541

## Readings
Most of our readings will come from the follwoing online books:
* DM-AOI: Discrete Math: An Open Intorduction by _Oscar Levin_
  available at https://discrete.openmathbooks.org/dmoi3/dmoi.html
* MfCS: Mathematics for Computer Science (from MIT) by _Lehman, Leighton, and Meyer_
  available at as a pdf at https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf
  or in an online form as https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/
* PDM: Problems in Discrete Math by _Chung-Chih Li and Kishan Mehrotra_
  https://itk.ilstu.edu//faculty/chungli/DIS300/dis300v1.pdf
* MFLP: A Modern Formal Logic Primer by _Paul Teller_:
  https://tellerprimer.ucdavis.edu/

### Week 1 - due Wednesday 9/6/2023 before class
Read the following sections of two online books on Discrete Math
* DM-AOI Ch 0.2 http://discrete.openmathbooks.org/dmoi3/sec_intro-statements.html
* DM-AOI Ch 3.1 http://discrete.openmathbooks.org/dmoi3/sec_propositional.html
* MfCS [Ch3.1-3.5](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session4/)
and try some of the problems at the end of the sections. We will go over some of them in class on Monday.

### Week 2 - due Monday 9/11/2023 before class
Read 
* [Chapter 3.6: Predicate Formulas](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session5/) in MfCS
* Chapter 2 of PDM
* Chapter 8 of MFLP
  
Connect to the https://mastery.cs.brandeis.edu site with PIN 731541 and do all of the problems in the following problem sets:
* Translation to Propositional Logic
* Evaluation of Propositional Formulas
* Truth Tables

### Week 3 - due Monday 9/18/2023 before class
Read 
* [Chapter 3.6: Predicate Formulas](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session5/) in MfCS

Connect to the [MLA](https://mastery.cs.brandeis.edu) Homework site with PIN 731541 and do all of the problems due 9/18
