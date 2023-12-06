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
* $S(k) = 4 S(k-1) + 8 2^k$

If we didn't have the last term $8 2^k$, this would be a simple linear recurrence and we know how to solve it
by finding the characteristic polynomial $x-4$ and using polynomial fitting for the form $s(k) = a*2^k$.

But we have this additional term which makes the recurrence into an **inhomogeneous** recurrence relation.
If we can find the general form of the solution, then we can use polynomial fitting to find the closed form.

We will use Generating Functions to find that general form.

