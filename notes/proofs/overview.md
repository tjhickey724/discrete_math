# The Art of Writing Mathematical Proofs
In this unit we discuss different proof techniques
and practice using these techniques to create clear and convincing arguments
of the truth of mathematical statements. These are fundamental skills for
Computer Scientists as there are many cases where we want to clearly explain why
our algorithms and programs are correct and efficient, and the best way to do that is with a
well-designed proof.

There are usually many different ways we prove that an argument is valid.
We have seen that there are formal methods for proving validity, but these quickly
become too messy and complex when trying to prove interesting propositions, so we
will focus on "informal" proofs.

We will learn how to use the following proof techniques:
* **direct proof** - show that the conclusion follows from the premises by direct application of the premises
* **proof by contradiction** - assuming that the conclusion is false and using  the premises to generate a contradiction, which shows the conclusion can not be false
* **proof by cases** - showing that $a1\rightarrow c$ and  $a2\rightarrow c$ and $\ldots$ and $an\rightarrow c$ and  and at least one of a1, a2,...., an must be true, so $c$ must be true.
* **proof by induction** - showing that some statement P(n) is true for every $n\ge 0$ by showing it is true for $n=0$ and
  showing that $\forall n (P(n) \rightarrow P(n+1))$, hence $P(0)$ is true and so is $P(1)$ and $P(2)$ and $P(3)$ etc....

Ideally we want to find the simplest, clearest, most convincing argument that something is true, and we may need to
try different proof techniques to find the best one.

Let's look at some examples, and have you try to create your own proofs...

## Direct Proofs
Lets consider the domain of integers (0,1,2,..., -1,-2,...).
A number is even if it is a multiple of 2, that is
* $\forall x ({\rm even}(x) \leftrightarrow \exists d (x = 2d))$

otherwise it is odd, that is $x=2d+1$ for some d, that is
* $\forall x ({\rm odd}(x) \leftrightarrow \exists d (x = 2d+1))$

Let's prove that if $n$ is even then $n^2$ is even.

**Proof:** 
<br>
if n is even then n=2k for some integer k, 
<br>
so $n^2=(2k)^2 = 4k^2 = 2(2k^2)$, 
<br> so it $n^2$ a multiple of 2,
<br> hence it is even. Q.E.D.

The Q.E.D. stands for _Quod Erat Demonstrandum_ which is Latin for "what was to be shown"
and is often found at the end of a proof signalling that the proof is over.

Let's have you give a direct proof of the following:
* if $x$ is odd, then so is $x^2$.
* if $x$ and $y$ are even, then so is $x+y$
* $x*y$ is even if $x$ or $y$ is






