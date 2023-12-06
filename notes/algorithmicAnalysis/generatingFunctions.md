# Solving Divide And Conquer recurrences with Generating Functions

Today we will show how to solve recurrences that arise from analyzing divide and conquer algorithms by using Generating Functions.
The key idea is to 
1. convert the recurrence equations into an equation on the Generating Function for the series
and then
2. to use standard techniques to find the form of the answer, with unspecified variables a,b,c,... and finally
3. use "polynomial fitting" to generate linear equations for those variables which we can solve 
   using linear algebra techniques such as variable elimination

## Example 1 - converting divide-and-conquer recursions to inhomogeneous linear recurrences
We'll illustrate this with an example. Let's look at the formula that arises from an algorithm for multiplying 
two n-bit numbers usind divide and conquer:
* $T(1)=1  T(n) = 4 T(n/2) + 8n$

Our first step is to convert this into a linear recurrence relation by restricting to powers of 2.

Let's assume $n=2^k$ and lets solve this recurrence only for powers of 2. Let $S(k) = T(2^k)$, then we have
* $S(0) = T(2^0) = T(1) = 1$
* $S(k) = T(2^k) = 4*T(2^k/2) + 8 2^k = 4 * T(2^{k-1}) + 8 * 2^k = 4 S(k-1) + 8 * 2^k$

So we get a linear recurrence on S from the divide-and-conquer recurrence on T
* $S(k) = 4 S(k-1) + 8 * 2^k$

If we didn't have the last term $8 2^k$, this would be a simple linear recurrence and we know how to solve it
by finding the characteristic polynomial $x-4$ and using polynomial fitting for the form $s(k) = a*2^k$.

But we have this additional term which makes the recurrence into an **inhomogeneous** recurrence relation.
If we can find the general form of the solution, then we can use polynomial fitting to find the closed form.

We will use Generating Functions to find that general form.

## Generating Functions for Inhomogeneous Linear Recurrences
For a sequence S(k) on the natural numbers 0,1,2,... we can define a formal power series F by
* $F(x) = \sum_\limits{i=0}^\infty S(k) x^k$

If we have a linear recurrence on $S$ 
* $S(k) = a_1 S(k-1) + a_2 S(k-2) + .... + a_j S(k-j)$

then it can be transformed into a equation on $S$
* $(1 - (a_1 x + a_2x^2 + \ldots+ a_m x^j)) S = P(x)$

where $P$ is a polynomial in x of degree at most $j-1$. 

**Proof** We can see this by observing that
* $a_j x^j S(x) = \sum_\limits{k=0}^\infty S(k) x^{k+j}$
* $= \sum_\limits{k=j}^\infty  a_j S(k-j) x^{k}$

So 
* $( a_1 x + a_2x^2 + \ldots +a_m x^m) S = \sum_\limits{k=j}^\infty b_k x^{k}$
* where $b_k = \sum_\limits{i=1}^m a_j S(k-j)$ for $k \ge m$
* So $b_k = S(k)$ for $k\ge m$

**QED**

---

This implies that 
* $S(x) = P(x)/Q(x)$

where $Q(x) = 1 -a_1 x -a_2 x^2 - \ldots - a_m x^m$ and if we let $x = 1/y$ then $Q(1/y)$ is the characteristic polymomial.

If we factor $Q$ as $\prod_\limits{i=1}^r (x-\beta_i)^{r_i}$ where $r_i$ is the multiplicity of the root $\beta_i$,
then we can use the partial fractions approach to rewrite $S(x)$ as 

$$S(x) = \frac{R(x)}{Q(x)} = \sum_\limits{i-1}^r \frac{R_i(x)}{(1-\beta_i)^{r_i}}$$

where $R_i$ is a polynomial of degree less than $r_i$. 

## Handling the Inhomogeneous case
In the case where we have an inhomogeneous equation with polyomials $b_i$ and real (or complex) values $\gamma_i$
* $S(k) = a_1 S(k-1) + a_2 S(k-2) + .... + a_j S(k-j) + b_1(k)\gamma_1^k + \ldots + b_s(k) \gamma_s^k$

We can show the inhomogeneious part is also from a generating function of the form:

$$I(x) = \sum_\limits{i-1}^r \frac{G_i(x)}{(1-\gamma_i)^{ss_i}}$$

where $s_i$ is the degree of the polynomial $b_i$.

Hence our formula for $S$ in the inhomogenous case is
* $S(x) = (P(x) + I(x))/Q(x)$

and so the general form of the generating function is

$$S(k) = \sum_\limits{i=1}^m c_i(k)\beta_i^k + \sum_\limits{i=1}^r d_i(k)\gamma_i^k$$

and we can use polynomial fitting to find the coefficients of the polynomials $c_i$ and $d_i$.

## Example 1
Lets try this with the following Divide and Conquer recursion 
* $T(1)=1$  $T(n) = 4 T(n/2) + 8n$

Using $n=2^k$ this becomes a linear inhomogeneous recursion $S(k) = T(2^k)$
* $S(0) = 1$
* $S(k) = 4 S(k-1) + 4 * 2^k$

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
Let's try this with 
* $T(1)=1$  $T(n) = 3 T(n/2) + 15n$

and we'll find that the result is
* $S(k) = 31 * 3^k - 30 * 2^k$, and so with $n=2^k$
* $T(n) = 31 n^r - 30 n = O(n^r)$

where $r = \log_2(3) = 1.58...$ and $n^r = 2^{k \log_2(3)} = {2^{\log_2(3)}}^k = 3^k$

## Example 4
Let's try it with the merge sort recursion
* $T(n) = 2 T(n/2) + n$
* $S(k) = 2 S(k-1) + 2^k$

and we'll find that
* $S(k) = (k+1)2^k$ and so
* $T(n) = (\log_2(n) + 1) n = n\log_2(n) + n = O(\log_2(n))$
