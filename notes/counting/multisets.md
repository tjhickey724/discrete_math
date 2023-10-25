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
Note we are including aab in this list but not aba or baa. 

There are several other ways we can think about multisets:

* as ordered sequences of elements from a set.
* another way to look at this is a the number of solutions to the equation x1+x2+x3=3
with x1,x2,x3 >=0, and
* we can also associate to each such solution as combination of stars (*) and bars (|)
where * represents an element of the set and a bar (|) where each bar indicates switching to the next element of the set
and each * represents an element of that set.

Here we see the same set of multisets represented in these three different ways:
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
Let's use the notation M(n,k) to denote the number of multisets of size k from a set of size n.

---

**Theorem.** $M(n,k) = \binom{n+k-1}{k}$

**Proof:** 
We will show that $M(n,k)$ can be seen as choosing $k-1$ positions from the sequence $1,2,...,n$.
As we can see in the table above, each multiset can be specified either 
* by listing the elements in the multiset (e.g. aab) or
* by a sequence of natural numbers specifying how many times $x_i$ each element $a_i$ is in the set (e.g. 210) or
* by a string of k stars and n-1 bars (e.g. '**|*|'), where the n-1 bars divide the k stars into n groups, and $x_i$ is the number of stars 
in the $i$ th group.

For the stars and bars arrangements we have k stars and n-1 bars for a total of n+k-1 characters, and we can specify such
an arrangement by specifying which k of the n+k-1 characters are stars. There are n+k-1 choose k such arrangements.
Thus, using this 1-1 correspondence, we see that $M(n,k) = \binom{n+k-1}{k}$. **QED**

---

## Applications
### Cookies
Suppose we have 5 cookies that we want to distribute among our three friends {Amy, Bohan, and Carlos). 
We already ate too many cookies, so we won't get any.
How many ways are there to distribute those cookies?

Each outcome here is a multi-set saying how many cookies we give to Amy, Bohan, and Carlos
so this is a sequence of three integers a,b,c that sum to 5; or a multiset of size 5 taken from {a,b,c}.
By our theorem we know this is $\binom{3+5-1}{2} = 7 * 6/(1 * 2) = 21$ and we could write them all down:

```
aaaaa aaaab aaabb aabbb abbbb
aaabc aabbc aabcb aabcc aaccc
abbbb abbbc abbcc abccc acccc
bbbbb bbbbc bbbcc bbccc bcccc
ccccc
```
or equivalently looking at sequences that sum to 5, multisets of length 5 and k stars with n-1 bars we get
```
ABC
005  ccccc  ||*****
014  bcccc  |*|****
023  bbccc  |**|***
032  bbbcc  |***|**
041  bbbbc  |****|*

050  bbbbb  |*****|
104  acccc  *||****
113  abccc  *|*|***
122  abbcc  *|**|**
131  abbbc  *|***|*

140  abbbb  *|****|
203  aaccc  **||***
212  aabcc  **|*|**
221  aabbc  **|**|*
230  aabbb  **|***|

302  aaacc  ***||**
311  aaabc  ***|*|*
320  aaabb  ***|**|
401  aaaac  ****||*
410  aaaab  ****|*|

500  aaaaa  *****||
```

### non-decreasing phone numbers
Suppose we are interested in the number of phone numbers where each digit is at least as big as the previous one,
e.g. 011-2669  or 222-3466
How many such phone numbers are there?
We see that if we have a multiset of size 7 from the digits {0,1,2,3,4,5,6,7,8,9} we can get such a phone number, and vice versa,
just by putting a dash between the 3rd and 4th digits. Thus the number of such phone numbers is

$$
\binom{10+7-1}{7} = \binom{16}{7} = \frac{16 * 15 * 14 * 13 * 12 * 11 * 10}{1 * 2 * 3 * 4 * 5 * 6 * 7} = 11440
$$

# Summary

Here are the three main counting formulas we've discussed.  
Let $A$ be a set with $n$ elements, then

1. The number of sequences of length $k$ with elements from $A$ is $n^k$
2. The number of subsets of A of size $k$ is $\binom nk = \frac{n!}{(n-k)!}$
3. The number of multisets of A of size $k$ is $\binom {n+k-1}{k}$



