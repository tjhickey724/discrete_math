# Summary of Counting Methods

We have seen how to count four different kinds of sequences of elements from an ordered set $A$  of size $n$, e.g. $\\{a_1,\ldots,a_n\\}$

| name | definition | size |
| --- | --- | --- |
| sequence of size $k$: $A^k$ | $\\{(a_1,\ldots,a_k:\ a_i \in A\\}$ | $n^k$ |
| permutation of size $k$: $P(A,k)$ | $\\{(a_1,\ldots,a_k:\ a_i \in A, \ a_i {\rm distinct}\\}$ | $P(n,k)=\frac{n!}{(n-k)!}$ |
| combination of size $k$: $C(A,k)$ | $\\{(a_1,\ldots,a_k:\ a_i \in A, \ a_1\lt a_2 \lt \ldots \lt a_k\\}$ | $C(n,k)=\binom({n}{k}=\frac{n!}{k!(n-k)!}$ |
| mulltiset of size $k$: $M(A,k)$ | $\\{(a_1,\ldots,a_k:\ a_i \in A, \ a_1\le a_2 \le \ldots \le a_k\\}$ | $M(n,k)=\binom{n-k+1}{k} =\frac{(n+k-1)!}{k!}$ |

