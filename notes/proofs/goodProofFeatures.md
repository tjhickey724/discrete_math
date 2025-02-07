# Features of a Good Proof
Here we summarize the points from Chapter 1.9 for Mathematics for Computer Science
about how to write a good proof.

0. Clearly state what you are going to prove
   * you may want to label it as a Proposition or a Theorem
   * after you state what you will prove, then go to a new line and clearly label the beginning of the proof
1. State your game plan
   * tell the reader how you are going to prove the statement, by contradiction, by cases, etc.
   * more involved proofs will require a bigger proof sketch
2. Keep a linear flow
   * the reader should expect a well organized sequence of arguments where each step is well motivated
3. A proof is an essay, not a calculation.
   * Use complete sentences, and for longer proofs, use paragraphs with topic sentences
   * Write as if you are telling a story which will explain why the thing you are proving is true
4. Avoid excessive symbolism
   * If you can explain a concept without introducing a lot of notation, that will usually make it clearer and easier to read.
5. Revise and simplify
   * Just as with programming, or writing fiction stories, or term papers, it is always a good idea to revise your proof
and make it as simple as you can
6. Structure long proofs
   * For long proofs you will need to introduce Propositions and Lemmas to break the argument into understandable pieces.
7. Be wary of the "obvious"
   * It is tempting to say "this is clearly true" when you suspect it is true but you don't know how to prove it, don't do that!
8. Finish
   * Long proofs will need a concluding paragraph which recaps the proof.
   * Shorter proofs can simply end with "QED"
   * In all cases, let the user know the proof is complete

## Structure of a Proof
So a proof should have the following structure:
```
Theorem.  statement of the thing to be proved.

Proof: An introductory sentence (or paragraph) explaining how you will prove it.

One or more sentences (or paragraphs) telling the story of why this statement is true in clear and compelling prose
with formulas and equations intermixed as needed.

A concluding sentence (or pargraph) stating that the proof is complete and explaining why, if needed.
```

## Examples of proofs
Let's now look at some proofs and see how they are structured.
* [Chapter 1.1-1.6 of MfCS](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session1/)
has several good examples of proofs, as does
* [Chapter 1.7-1.9 of MfCS](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_session2/)

We'll look at some of these and then have you practice writing some proofs using the exercises at the end of Chapter 1.

* Theorem 1.5.1 on page 12, an example of a direct proof
  * now you use the same approach to prove that $n^3-3n^2+2n$ is divisible by 3 for all integers $n$
* Theorem 1.5.2 on page 13, a proof by contradiction
  * now you prove that the $n$ th root of any irrational number $r$ is irrational, for all $n>0$
* Theorem 1.6.1 on page 14, a proof by chain of iff's
* Theorem 1.7 on clubs and groups, a proof by cases...
  [Here](https://github.com/tjhickey724/discrete_math/blob/main/notes/proofs/groupsAndStrangers.jpg) is a link to a figure showing six people with their connections (either they know each other (red) or not (black))
* Theorem 1.8.1, a proof by contradiction
  * now you prove that the nth root of any integer m is either an integer or is irrational, for all n>0 and m>0
  * similarly we can prove that a root of any monic polynomial with integer coefficients, is either an integer or is irrational
 
