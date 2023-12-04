# Analysis of Algorithms

In this section we give an overview of techniques for analyzing the performance of algorithms.

## Big-Oh, Big-Omega, and Big-Theta notation
The first step is to define some families of functions that we use to classify algorithms by their
performance...  Rather than find the exact time a program will take we want a rough classification
that allows us to compare different programs and we're especially interested on large data inputs
and not too interested on the speed of the particular computer... This leads naturally to these three
families of sets...

We will consider sequences $s(0), s(1_, ..., s(n), \ldots$ where $s(i)$ is the "time" that the program
takes on inputs of size $i$.  In practice, there may be many inputs of size $i$ so we would have to 
specify if we are talking about the worst case time (i.e. the one with the longest runtime), or the
best case, or the average case. Typically we consider the worst case unless otherwise specified.

We will then classify such sequences by their growth rates...

### Linear programs
We say that $s$ is a linear sequence if the following is true
* $\exists c \exists k \ \forall n\gt k s(n)\lt c*n$

and we let $O(n)$ be the set of all such sequences. If $s$ is in $O(n)$ we say that $s$ is "big-Oh" n.




