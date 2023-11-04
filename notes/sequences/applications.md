# Applications of Sequences

The techniques we've used for solving recursive equations have many applications in Computer Science.
In this note, we will show how a variation of the fibonacci sequence has applications in finding the
performance of certain algorithms for quickly storing and looking up data.

A full binary tree of height k is a tree in which every node has exactly two children and the every leaf
has exactly k+1 ancestors. The image below shows the binary trees of heights 1,2,3,...
![Full Binary Trees](BinaryTrees.jpg)

If B(k) is the number of nodes in a binary tree of height k, then $B$ satisfies the following recursion equation:
* $B(1)=1$
* $B(k) = 2*B(k-1) + 1$
and we can prove by induction that this means $B(k) = 2^k-1$

The fibonacci trees can be defined recursively as follows:
* $F_1$ is a single node
* $F_2$ is a tree where the root has one child on the left and none on the right
* $F_k$ for $k>2$ is a tree whose left child is $F_{k-2}$ and whose right child is $F_{k-1}$


