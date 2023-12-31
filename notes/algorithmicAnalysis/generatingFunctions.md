# Solving Divide And Conquer recurrences with Generating Functions

Today we will show how to solve recurrences that arise from analyzing divide and conquer algorithms by using Generating Functions. Almost all of the fast algorithms we know rely on divide and conquer techniques where a
problem of size $n$ is broken down into $b$ problems of size $n/b$  (typically 2 problems of size $n/2$) and
these are solved and their solutions joined together.  These algorithms always result in a particular kind of 
recurrence 

$$S(n) =  a S(n/b) + g(n)$$

where we reduce a problem of size $n$ into $a$ problems of size $n/b$ and $a$ and $b$ are integers (1,2,3....).
We will show how to solve such recurrences when $g$ is a sum of polynomials $p_i(n)$ times exponentials $\beta_i^n$:

$$g(n) = \sum_\limits{i=1}^m p_i(n) * \beta_i^n$$

The key idea is to 
1. convert the recurrence equations into an equation on the Generating Function for the series
and then
2. to use standard techniques to find the form of the answer, with unspecified variables a,b,c,... 
3. use "polynomial fitting" to generate linear equations for those variables which we can solve 
   using linear algebra techniques such as variable elimination, and finally
4. prove that the closed form is correct using induction.

## Example 0 - converting divide-and-conquer recursions to inhomogeneous linear recurrences
We'll illustrate this with an example. Let's look at the formula that arises from an algorithm for multiplying 
two n-bit numbers usind divide and conquer:
* $T(1)=1$
* $T(n) = 4 T(n/2) + 8n$
* $T(2) = 4 T(2/2) + 8 * 2 = 4 T(1) + 16 = 20$
* $T(4) = 4 T(4/2) + 8 * 4 = 4 T(2) + 32 = 112$
* $T(8) = 4 T(8/2) + 8 * 8 = 4 T(4) + 64 = 512$

Our first step is to convert this into a linear recurrence relation by restricting to powers of 2.

Let's assume $n=2^k$ and lets solve this recurrence only for powers of 2. Let $S(k) = T(2^k)$, then we have
* $S(0) = T(2^0) = T(1) = 1$
* $S(k) = T(2^k) = 4*T(2^k/2) + 8 * 2^k = 4 * T(2^{k-1}) + 8 * 2^k = 4 S(k-1) + 8 * 2^k$

So we get a linear recurrence on S from the divide-and-conquer recurrence on T
* $S(0)=1$
* $S(k) = 4 S(k-1) + 8 * 2^k$

If we didn't have the last term $8 * 2^k$, this would be a simple linear recurrence and we know how to solve it
by finding the characteristic polynomial $x-4$ and using polynomial fitting for the form $s(k) = a*4^k$.

But we have this additional term which makes the recurrence into an **inhomogeneous** recurrence relation.
If we can find the general form of the solution, then we can use polynomial fitting to find the closed form.

We will use Generating Functions to find that general form.

## Generating Functions for Inhomogeneous Linear Recurrences
For a sequence S(k) on the natural numbers 0,1,2,... we can define a formal power series $F_S$ by
* $F_S(x) = \sum_\limits{k=0}^\infty S(k) x^k$

**Theorem**
If we have a linear recurrence on $S$ 
* $S(k) = a_1 S(k-1) + a_2 S(k-2) + .... + a_j S(k-j)$

then it can be transformed into an equation on $S$
* $(1 - (a_1 x + a_2x^2 + \ldots+ a_m x^j)) F_S = P(x)$
* $F_S(x) = P(x)/Q(x)$ where $Q(x) = (1 - (a_1 x + a_2x^2 + \ldots+ a_m x^j))$

where $P$ is a polynomial in x of degree at most $j-1$. 

**Proof** We can see this by observing that
* $a_j x^j F_S(x) = \sum_\limits{k=0}^\infty S(k) x^{k+j}$
* $= \sum_\limits{k=j}^\infty  a_j S(k-j) x^{k}$

So 
* $( a_1 x + a_2x^2 + \ldots +a_m x^m) F_S = \sum_\limits{k=j}^\infty b_k x^{k}$
* where $b_k = \sum_\limits{i=1}^m a_j S(k-j)$ for $k \ge m$
* So $b_k = S(k)$ for $k\ge m$

**QED**

---

This implies that 
* $F_S(x) = P(x)/Q(x)$

where $Q(x) = 1 -a_1 x -a_2 x^2 - \ldots - a_m x^m$ and if we let $x = 1/y$ then $y^m Q(1/y)$ is the characteristic polymomial.

If we factor $Q$ as $\prod_\limits{i=1}^r (x-\beta_i)^{r_i}$ where $r_i$ is the multiplicity of the root $\beta_i$,
then we can use the partial fractions approach to rewrite $S(x)$ as 

$$F_S(x) = \frac{R(x)}{Q(x)} = \sum_\limits{i-1}^r \frac{R_i(x)}{(1-\beta_i)^{r_i}}$$

where $R_i$ is a polynomial of degree less than $r_i$. 

## Handling the Inhomogeneous case
In the case where we have an inhomogeneous equation with polyomials $b_i$ and real (or complex) values $\gamma_i$
* $S(k) = a_1 S(k-1) + a_2 S(k-2) + .... + a_j S(k-j) + b_1(k)\gamma_1^k + \ldots + b_s(k) \gamma_s^k$

We can show the inhomogeneious part is also from a generating function of the form:

$$I(x) = \sum_\limits{i-1}^r \frac{G_i(x)}{(1-\gamma_i)^{ss_i}}$$

where $s_i$ is the degree of the polynomial $b_i$.

Hence our formula for $F_S$ in the inhomogenous case is
* $F_S(x) = (P(x) + I(x))/Q(x)$

and so the general form of the generating function is

$$S(k) = \sum_\limits{i=1}^m c_i(k)\beta_i^k + \sum_\limits{i=1}^r d_i(k)\gamma_i^k$$

and we can use polynomial fitting to find the coefficients of the polynomials $c_i$ and $d_i$.

## Example 1
Lets try this with the following Divide and Conquer recursion for multiplying 2 n-bit binary numbers
* $T(1)=1$
* $T(n) = 4 T(n/2) + 8n$

Using $n=2^k$ this becomes a linear inhomogeneous recursion $S(k) = T(2^k)$
* $S(0) = 1$
* $S(k) = 4 S(k-1) + 4 * 2^k$
* so $(1-4x) F_S = 4/(1-2x) - 3 = (1+6x)/(1-2x)$
* so $F_S = (1+6x)/((1-4x)(1-2x))$

From our observations above this means that the general form of the solution will be
* $S(n) = a * 4^n + b * 2^n$

and we can use the first few values of $S(n)$ to generate linear equations in $a$ and $b$
* $S(1) = 4 * S(0) + 4 * 2^1 = 4 * 1 + 8 = 12$
* $S(2) = 4 * S(1) + 4 * 2^2 = 4 * 12 + 4 * 4 = 64$

So 
* $1 = S(0) = a * 4^0 + b * s^0 = a+b$
* $12 = S(1) = a * 4^1 + b * 2^1 = 4a+2b$

Which gives us $2a = 10$ so $a=5$ and $b=-4$ and
* $S(k) = 5 * 4^k - 4 * 2^k$

and letting $k=\log_2(n)$, i.e. $n = 2^k$ we get
* $T(n) = 5 n^2 - 4n = O(n^2)$

when $n$ is a power of $2$.

## Example 2
Let's try this with the smart multiplication of 2 n-bit binary numbers using the identity
* $(A_1 * 2^n + A_0) * (B_1 * 2^n + B_0) =$
* $A_1B_1 (2^{2n} + 2^n) + (A_1-A_0) * (B_0-B_1) * 2^n + A_0 B_0 (1 + 2^n)$

which uses only 3 n-bit multiplications instead of the usual four with
$A_1B_1 2^{2n} + (A_1B_0 + A_0 B_1) 2^n + A_0 B_0$

though it has many more additions and shifts (15 compared to 4)

The Recursive Equation for this is 
* $T(1)=1$
* $T(n) = 3 T(n/2) + 15n$

and we'll find that the result is
* $S(k) = 31 * 3^k - 30 * 2^k$, and so with $n=2^k$
* $T(n) = 31 n^r - 30 n = O(n^r)$

where $r = \log_2(3) = 1.58...$ and $n^r = 2^{k \log_2(3)} = (2^{\log_2(3)})^k = 3^k$

## Example 4
Let's try it with the merge sort recursion
* $T(1) = 1$
* $T(n) = 2 T(n/2) + n$
* $S(0)=1$
* $S(k) = 2 S(k-1) + 2^k$

and we'll find that
* $S(k) = (k+1)2^k$ and so
* $T(n) = (\log_2(n) + 1) n = n\log_2(n) + n = O(n\log_2(n))$
