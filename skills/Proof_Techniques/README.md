# Overview of Proofs

In this unit we discuss different proof techniques
and practice using these techniques to create clear and convincing arguments
of the truth of mathematical statements. These are fundamental skills for
Computer Scientists as there are many cases where we want to clearly explain why
our algorithms and programs are correct and efficient, and the best way to do that is with a
well-designed proof.

## Nomenclature
We often label the results that we prove as one of the following three kinds of statements:
* **Theorem** - this is a major result which is interesting in its own right
* **Proposition** - this is a true fact which is somewhat interesting, but mainly because it is used to prove a theorem
* **Lemma** - this is a true result, which is only interesting because it is used to prove other more interesting things.

There are usually many different ways we prove that an argument is valid.
We have seen that there are formal methods for proving validity, but these quickly
become too messy and complex when trying to prove interesting propositions, so we
will focus on "informal" proofs.

We will learn how to use the following proof techniques:
* **direct proof** - show that the conclusion follows from the premises by direct application of the premises
* **contrapositive proof** - to show that $A\rightarrow B$, prove the equivalent $\neg B \rightarrow \neg A$
    <br> $A\rightarrow B \equiv  \neg A \vee B \equiv \neg\neg B \vee \neg A \equiv \neg B \rightarrow \neg A$
* **proofs of iff statements** - to prove $A\leftrightarrow B$ we must prove $A\rightarrow B$ and $A\leftarrow B$
  to show that $A$ and $B$ are either both true or both false.
* **proof by contradiction** - assuming that the conclusion is false and using  the premises to generate a contradiction, which shows the conclusion can not be false
    <br> $(P\wedge \neg C)\rightarrow {\rm false} \equiv \neg (P \wedge \neg C) \equiv \neg P \vee C \equiv P \rightarrow C$
* **proof by cases** - showing that $a_1\rightarrow c$ and  $a_2\rightarrow c$ and $\ldots$ and $a_n\rightarrow c$ and  and at least one of a1, a2,...., an must be true, so $c$ must be true.
   <br> $(A_1\vee A_2\vee\ldots\vee A_n)$  <br>$(A_1\rightarrow C)$<br>$(A_2\rightarrow C)$
  <br>$\ldots$<br>$(A_n \rightarrow C)$<br>----------------------<br> $C$
* **proof by induction** - showing that some statement P(n) is true for every $n\ge 0$ by showing it is true for $n=0$ and
  showing that $\forall n (P(n) \rightarrow P(n+1))$, hence $P(0)$ is true and so is $P(1)$ and $P(2)$ and $P(3)$ etc....

  $P(0)$<br>
  $\forall n  (P(n) \rightarrow P(n+1))$
  <br>----------------------<br> 
  $\forall n P(n)$

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

**Lemma 1:** if $n$ is even, then $n^2$ must be even.

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
* $x*y$ is even if $x$ is even

## Proof by Contrapositive
Suppose we want to prove the following:
* if $n^2$ is odd then $n$ must be odd

This has the form $A\rightarrow B$ where $A$ is $n^2$ is odd, and $B$ is $n is odd.

Since $A\rightarrow B$ is logically equivalent to its contrapositive $\neg B \rightarrow \neg A$.
We can prove that instead, i.e.
* if $n$ is not odd, then $n^2$ is not odd

Remembering that $n$ is not odd is the same as saying $n$ is even, we must then prove
* if $n$ is even then $n^2$ is even

which we have already proved and which was fairly easy!

Let's have you prove the following:
* if $n^3$ is odd, then $n$ is odd
* if $n^3$ is even, then $n$ is even

## Proofs of iff statements
Often we want to prove that two logical statements are equivalent, e.g.
* $n^2$ is even if and only if $n$ is even

which has the form $A\leftrightarrow B$
* $A$ is $n^2$ is even, and
* $B$ is $n$ is even

To prove $A\leftrightarrow B$ there are a few ways to proceeed.
1. prove that $A\rightarrow B$ and $B\rightarrow A$
2. prove that $A\rightarrow B$ and $\neg A \rightarrow \neg B$, where we're proving the contrapositive of $B\rightarrow A$
3. find statements $A_1,A_2,\ldots,A_n$ and prove a chain of simpler iff's that starts with $A$ and ends with $B$
   * $A=A_1\leftrightarrow A_2\leftrightarrow\ldots\leftrightarrow A_n=B$


Let's try to use one of these methods to prove the following:

__Theorem.__  $n^2$ is even if and only if $n$ is even.

__Proof__.
First we prove that $n$ is even implies $n^2$ is even (which we have done above).
$n$ even means $n=2k$ for some integer $k$, so $n^2=(2k)^2 = 4k^2 = 2(2k^2)$ so $n^2$ is even.

Then we prove that if $n^2$ is even then $n$ is even. This we prove by proving the contrapositive,
if $n$ is not even the $n^2$ is not even. So if $n$ is not even, then it is odd, so $n=2k+1$ for some integer k. Hence $n^2 = 4k^2 +4k+1 = 2(2k^2+2k) + 1 = 2j+1$ for some integer $j$, and so is odd by definition.

__Q.E.D.__


## Proofs by cases
This is a very common approach. Suppose we want to prove that some statement $C$ is true.
If we can find statements $A$ and $B$ such that at least one of them is true, and we can show that each implies $C$
(i.e. we show $C$ is true in each of these two cases), then we know $C$ must always be true.
* $(A\vee B) \wedge (A\rightarrow C) \wedge (B\rightarrow C) \rightarrow C$

Let's use this to prove that $n^2 + n$ is always even, by looking at the two cases $n$ is even and $n$ is odd.

__Theorem.__ for any integer $n$, the value $n^2+n$ is even.

__Proof:__
We will prove this by considering two cases: $n$ is even or $n$ is odd.

* case 1: assume $n$ is even, then $n=2k$ so $n^2+n = (2k)^2 + 2k = 4k^2+2k = 2(2k^2+k)$ is a multiple of 2, hence even.
* case 2: assume $n$ is odd, then $n=2k+1$ so $n^2 +n = 4k^2 + 4k + 1 + 2k +1 = 4k^2 + 6k + 2 = 2(2k^2+3k+1)$ is a multiple of 2, hence even.

Since $n$ must either be even or odd, and in both cases $n^2+n$ is even, we see that $n^2+n$ is even for all $n$. __Q.E.D.__

Note: we could prove this directly by noting that $n^2+n = n(n+1)$ and since either $n$ or $n+1$ must be even, so must their product!

Here is another example of a proof by cases. 

__Theorem__  Assume we paint a square 1x1 panel with 2 colors (say black and white), then there must be 2 points which are exactly 1 unit apart.

Here is an example of such a panel:

![2 color painting](https://nukeart.com/cdn/shop/files/abstract-painting-bound-by-opposites-484947.jpg?v=1724032326&width=100)

__Proof__ pick two adjacent corners of the square.
* Case 1. The colors of the two corners are the same.  In this case we are done as they are 1 unit apart.
* Case 2. The colors are different.  In this case there is a point P inside the square which makes an equilateral triangle with the two corners. Since the two corners have different colors, one is black and the other is white. So we again have two cases, depending on the color of the point P.
   *  if the point P is black, then it is 1 unit a way from the black corner, and
   *  if it is white, then it is one unit away from the white corner,
so in either case there are two points of the same color exactly 1 unit apart.

We have shown in both cases that there are two points with the same color exactly one unit apart, so the Theorem is true. __Q.E.D.__


## Proof by contradiction
This is the method we've been using in our formal proofs. To prove that $A \rightarrow B$, assume $A$ is true but $B$ is false and show this generates a contradication and hence can't be true.  Thus whenever $A$ is true, $B$ can't be false, so $B$ must also be true.

Let's use this to prove that $n^2$ is odd implies $n$ is odd.

**Proof:**
Suppose that $n^2$ is odd, but $n$ is not odd. Then $n$ must be even.
<br>
So $n=2k$ for some integer $k$, so $n^2 = (2k)^2 = 2(2k^2)$ is a multiple of 2 and hence is even.
<br>
This contradicts our premise that $n^2$ is odd, so $n$ can not be even, so it must be odd.
<br>
**QED**

## Interesting Application.
Let's use these techniques to prove something more interesting, that the square root of 2 is irrational, that is, can't be expressed as a fraction $a/b$ where $a$ and $b$ are integers.

**Theorem**  $\sqrt{2}$ is an irrational number.

**Proof**
We will prove this by contradiction. Assume $\sqrt{2} = a/b$ for integers $a$ and $b$.

We know that we can remove any common factors of $a$ and $b$ to put the fraction in lowest terms (why??)

so we can assume that they are not both even (why?)

so $\sqrt{2}=a/b$ iff $2 = (a/b)^2$ iff $2=a^2/b^2$ iff $2b^2 = a^2$. So $a^2$ is even, and hence by our results above $a$ must be even.

Hence $a=2k$ for some integer $k$.

Thus $2b^2=a^2$ iff $2b^2=(2k)^2$ iff $2b^2 = 4k^2$ iff $b^2=2k^2$ by factoring 2 out of both sides.

So $b^2$ is even, hence by our results above $b$ must be even.

But we chose $a$, $b$ so that $a/b$ was in lowest terms and hence they can't both be divisible by $2$.

This contradiction shows that $\sqrt{2}$ can not be a rational number, hence it is irrational.

**QED**
