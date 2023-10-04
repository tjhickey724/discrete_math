# More Examples of Proofs

## Lets prove that the log, base 2, of 3 is an irrational number!

We will use the following Lemma which we will prove later.

---

**Lemma** if $p$ is a prime and $n>1$ and $s>0$ are integers,
then $p$ divides $n^s$  if and only if $p$ divides $n$.

---

**Theorem** $\log_2(3)$ is irrational.

**proof**
We will prove this by contradiction.
Let's assume that $x = \log_2(3)$ is a rational number.
Then x = $r/s$ where r and s are integers.
We can further assume that it is in lowest terms, so that
r and s have no common factor.  We will use this to get
a contradiction by showing they have to have a common factor.

What does $\log_2(3)=x$ mean?
It means that raising 2 to the power x gives you 3:

$2^x=3$

so substituting $x=r/s$ we get

$2^(r/s) = 3$

Now raising both sides to the power $s$ we get

$(2^{\frac{r}{s}})^s = 3^s$

and since $(a^b)^c = a^(bc)$ for any numbers a,b,c, we get

$2^{\frac{r}{s}*s} = 3^s$

So simplifying $\frac{r}{s}*s=r$ we get

$2^r = 3^s$

So $3^s = 2*2^{r-1}$ which implies 2 divides $3^s$
by our Lemma, this implies 2 divides 3, which is false.

This contradiction proves that $\log_2(3)$ can not be rational, and hence is an irrational number.

**QED**

---



