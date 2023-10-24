# Multisets
Another important kind of counting problem is to count the number of multisets of size k from a set of size n.
A multiset is a set where you allow multiple elements, e.g. the multisets of size 3 from {a,b,c} is
```
aaa
aab
aac
abb
abc
acc
bbb
bbc
bcc
ccc
```
The other way to look at this is a the number of solutions to the equation x1+x2+x3=3
with x1,x2,x3 >=0, and we can also associate to each such solution as combination of stars (*) and bars (|)
where * represents an element of the set and a bar (|) where each bar indicates switching to the next element of the set
and each * represents an element of that set.
```
300    aaa  ***||
210    aab  **|*|
201    aac  **||*
120    abb  *|**|
102    acc  *||**
111    abc  *|*|*
030    bbb  |***|
021    bbc  |**|*
012    bcc  |*|**
003    ccc  ||***
```
Lets use the notation M(n,k) to denote the number of multisets of size k from a set of size n.

---

**Theorem.** $M(n,k) = \binom{n+k-1}{k-1}$

**Proof:** 
We will show that $M(n,k)$ can be seen as choosing $k-1$ positions from the sequence $1,2,...,n$.
As we can see in the table above, each multiset can be specified either by listing the elements in the multiset
(e.g. aab) or by a sequence of natural numbers specifying how many times $x_i$ each element $a_i$ is in the set (e.g. 210)
or by a string of k stars and n-1 bars (e.g. '**|*|'), where the n-1 bars divide the k stars into n groups, and $x_i$ is the number of stars 
in the $i$ th group.

Using this 1-1 correspondence, we see that $M(n,k) = \binom{n+k-1}{n-1}$. **QED**

---




