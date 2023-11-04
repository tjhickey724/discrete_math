# Applications of Sequences to AVL trees

The techniques we've used for solving recursive equations have many applications in Computer Science.
In this note, we will show how a variation of the fibonacci sequence has applications in finding the
performance of certain algorithms for quickly storing and looking up data.

In this note we will sketch out the proof that the basic operations of an AVL tree (defined below)
can be done in time about $\log_2(n)$.  These operations are to insert or remove an element from the tree
and to find whether a given element is in the tree. The main point we want to illustrate here is the
way in which recursion equations like the ones we've been studying arise when analyzing the execution time
of interesting (and important) programs.

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
* $F_k$ for $k>2$ is a tree whose left child is $F_{k-1}$ and whose right child is $F_{k-2}$

Below we see the first few Fibonacci trees

![FibonacciTrees](FibonacciTrees.png)

The number of $F(k)$ in the fibonacci tree of height k satisifies the following recursion equation:
* $F(1)=1$
* $F(2)=2$
* $F(k) = 1+ F(k-1)+F(k-2)$ for all $k\ge 3$ where the $1$ corresponds to the root of the tree and the other terms to the two children

and if we let $f = (1,1,2,3,5,8,13,21,34,...)$ be the usual fibonacci sequence then we can prove the following theorem by induction

**Theorem.$$ $F(k) = f_{k+2}$ for all $k\ge 0$.

We leave the proof to you as an exercise!

We have already seen that $f_n$ is $(\beta_1^n - \beta_2^n)/\sqrt{5}$ which is about $1.618^n/\sqrt{5}$ since $\beta_2 = -0.618...$ so $\beta_2^n$ is always between -1 and 1.

## AVL Trees
One of the most important data structures we learn about in a Data Structures and Algorithms class is the AVL tree. This is a tree whose nodes
contain important information and there are algorithms that can search for a value in an AVL tree, or add a new value or remove a value, and the time
of these operations is proportional to the height of the tree.  The key property of the AVL tree is the following:
* the heights of the two children of any node in the tree are either the same or differ by 1

Because of the AVL property, the number $N$ of nodes in an AVL tree is always between $B(k)$ and $F(k)$ as the most dense AVL tree of height k is a full binary tree
and the least dense is the Fibonacci tree. 
* $2^k-1 \le N \le \beta^{n+2}/\sqrt{5} = \beta^n * c$ where $c = (\beta^2/\sqrt{5}) = 1.17...$ and $\beta = 1.618...$ is the golden ratio.

This gives us a bound o the height $H$ of an AVL tree with $n$ nodes
* $ \log_2(n) \le H \le \log_\beta(n/c) < $\log_\beta(n)$

and $\log_\beta(n) = \log_2(n)/\log_2(\beta) = 1.44... \log_2(n)$

This gives us a bound on the efficiency of the AVL operations.

---

**Theorem** The time $T(n)$ it takes to search for an element in an AVL tree of size n, or to insert or remove an element satisfies
* $\log_2(n) \lt a*T(n) \lt \log_2(n)$ for some constant a depending on the speed of the computer.

**Proof.** Here we are assuming that these operations take time $h/a$ proportional to the height $h$ of the tree for some number $a\gt 0$
and we know from our recursion equations that the height is between $\log_2(n)$ and $1.45 \log_2(n)$.  The constants $a$ and $b$ give the proportions... **QED**

---



