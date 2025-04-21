# Correctness and Efficiency of the RSA algorithm

In these notes we will show how to implement RSA and sketch a proof of each step.
You can see a complete treatment of RSA in Chapter 8.11 of 
[Mathematics for Computer Science by Lehman, Leighton, and Meyer](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/)

We assume you've already read about [Congruences](F26.md) and an [overview of RSA](G09.md).


# Fast probabalistic test for primality
We can use Fermat's little theorem to quickly test if a number is "probably" prime.
I won't prove it here, but if $p$ is not prime then 
* the probability that $x^p=x$ mod p is less than 1/2

Actually there are some non-primes (called Carmichael numbers) that satisify Fermat's Little Theorem,
RSA still works with Carmichael primes but it is 
[somewhat less secure:](https://link.springer.com/content/pdf/10.1007/BFb0024472.pdf)

So one way to test if a number $p$ is prime is to repeatedly generated random numbers $x$
and test to see if $p$ divides $x^p-x$. If it ever fails, then you know $p$ is not prime.
If it doesn't fail after $N$ attempts, then the probability that $p$ is not prime is less than $1/2^N$.
Picking $N=100$, the probability is less than $10^{-30}$.

# Fast exponentiation
But how can we raise an number $x$ to such a large power mod p quickly?

Below is an algorithm for doing this:
``` python
def power(x,n,m):
    ''' return x^n mod m
        We introduce a variable p, initially 1
        with the invariant on (p,x,n,m) that (p*x^n)%m is constant
        at the top of the loop. When n=0 we return p%m which
        is equal to (x^n)%m
    '''
    p=1
    while n>0:
        # invariant on (p,x,n,m) is p* x^n mod m at top of the loop
        if n%2==0:
            #p*x^n= p*x^(2r)=p*(x^2)*r
            x = (x*x)%m
            n = n//2
        else:
            # p*x^n = p*x^(2r+1) = (p*x)*(x^2)^r
            p = (p*x)%m
            x = (x*x)%m
            n = (n-1)//2
    
    return p
```
## Loop Invariants and Correctness Proofs
Next we show that the "power" function defined above is correct using the "loop invariant" technique.
This is the most common way to prove that algorithms containing loops are correct. The idea is to find some
function which is true before the loop, and whose value isn't changed by the body of the loop, and hence
it must also be true at the end of the loop.

**Proposition** The "power" algorithm above correctly computes $x^n$ % $m$ in at most $\log_2(n)$ steps.

**Proof**
We will show that the value $v(p,x,n) = (p * x^n)$ % $m$ is a loop invariant at the top of the loop. That means
this formula 
* $v(p,x,n) = p * x^n$ % $m$

always has the same value. The first time through the loop $p=1$ and so $v(1,x,n)$ has
the value $x^n$ % $m$ that we want to compute.  After the loop is over, $n=0$ and so
* $v(p,x,n) = p * x^0 = p$

and since the value of v is invariant, $p$ will have the value $x^n$ % $m$ after the loop is over.

There are three cases, and we omit the "% $m$" to keep the notation simpler.
* $n=0$, in this case the loop is over and $v(p,x,n)=p*x^0 = p$ which is the value we return
* if $n$ is even, then $n = 2k$ for some k, and so $v(p,x,n) = p * x^{2k} = p * (x^2)^k = p * (x^2)^{n/2} = v(p,x^2,n/2)$
* if $n$ is odd, then $n = 2k+1$ for some k, and so $v(p,x,n) = p * x^{2k+1} = p * x * (x^2)^k = v(p*x,x^2,(n-1)/2)

This shows that the value of v(p,x,n) is the same at the top of the loop as at the bottom and hence it is the same
before the loop and after the loop, so $p has the value $x^n$ % $m$  when the function returns.

Notice that each time $n$ is reduced by at least a factor of 2, so if there are $j$ iterations of the loop
then n must be at least $2^j$, so  $n \ge 2^j$ so $j\le \log_2(n)$

**QED**

We can also raise $x$ to a power mod $m$ using a recursive function as follows:
``` python
def powerfn(t,x,n,m):
    ''' returns t * x^n mod m
    '''
    if (n==0):
        return t
    else:
        if n%2==0:
            return powerfn(t,(x*x)%m,n//2)
        else:
            return powerfn(t*x,(x*x)%m,(n-1)//2)
```
To prove the correctness of this function we have to show it terminates in at most $\log_2(n)$ calls, which is easy
because $n$ is reduced by at least $2$ in each call and never gets below 1. We also need to show that
the value $t * x^n$ % $m$ is preserved by the function and that proof is the same as the one for the iterative power function above.


## Primality Testing

We can now use this power function to test primality and to generate large primes efficiently as follows
``` python
def prime_test(p,n):
    ''' return true p passes prime test n times '''
    for i in range(n):
        x = randint(2,p-1)
        if power(x,p-1,p)!=1:
            return False
    return True

def generate_prime(d):
    ''' return next probable prime with d digits '''
    n = randint(10**d,10**(d+1)) # generate a random number with d+1 decimal digits
    while not prime_test(n,100):
        n=n+1
    return n
```

## Proving the Correctness of RSA
We can now see how to generate two large primes $p$ and $q$ and form 
* their product $n=pq$, and
* the product $m=(p-1) * (q-1)$
  
which is the first step in the RSA algorithm.

The next step is to prove that Fermat's Little Theorem also holds for $m=pq$,
that is

**Theorem** Let p,q be two primes and m=(p-1)(q-1) and let $x$ be an integer in the range [0,m-1]
which has no common factors with m, that is $gcd(x,m)=1$, then
* $x^m = 1$ mod $n$

**Proof**
First observe that 
* $x^m = (x^{p-1})^{q-1}$

Let 
* $x_p = x^{p-1}$ and $x_q = x^{q-1}$
 
By Fermat's little theorem we know that 
* $x_p^{q-1} = 1$ mod $q$ since $x_p$ is relatively prime to q, so
* $x_p^{q-1} = 1 + qm_1$ for some integer $m_1$

Likeise 
* $x_q^{p-1} = 1$ mod $p$ since $x_q$ is relatively prime to p, so
* $x_q^{p-1} = 1+ p m_2$ for some integer m_2

So $x^{(p-1)(q-1)} = x_p^{q-1} = x_q^{p-1} = 1 + q m_1 = 1 + p m_2$

This means
* $qm_1 = p m_2$ and since $p$ and $q$ are distinct primes, p divides $m_1$ so $m_1 = p m_3$ for some integer $m_3$
* so $q m_1 = q p m_3 = p m_2$ so $m_2 = q m_3$
* Thus $x^{(p-1)(q-1)} = x_p^{q-1} = x_q^{p-1} = 1 + q p m_3$, so
* $x^{(p-1)(q-1)} = 1$ mod $pq$ whenever x is not divisible by $p$ or $q$, so
* $x^m = 1$ mod $n$

**QED**

We can now complete the RSA algorithm.

Pick a random number $e$ in the range [0,m) for which $gcd(e,m) = 1$.
One may need to generate several random numbers to find one which is relatively prime to $m$

Now use the Bézout algorithm to find a numbers $f$ and $g$ such that
* $f * e + g * m = 1$

This means that $f * e = 1 + g * m = 1$ mod $m$.

**Corollary** [Correctness of RSA]
Let $x$ be any integer in the range $[0,n)$ which is not divisible by p or q, and let
* $y = x^e$ % $n$

then $y$ is in the range $[0,n)$ and $gcd(y,m)=1$
* $y^f$ % $n = x$

**Proof**
This is a simple calculation
* $y^f = (x^e)^f = x^{ef} = x^{1 + mg} = x^1 * x^{mg}$ mod $n$
* now we know that $x^m=1$ mod n, so
* $y^f = x * (x^m)^g = x * 1^g = x * 1 = x$ mod n
* so $y^f$ % $n = x$

**QED**

## Efficiency of arithmetic on large numbers
One thing we didn't talk about was how much time it takes to do arithmetic on very large numbers.
The simple way is to use the algorithms we use by hand for multiplication, addition, subtraction, and division
and you can convince your self that these operations on two $k$ digit numbers can be done in at most $c k^2$ steps
for some small constant $c$, but since $k$ is a relatively small number (say 100 or 500 or 1000). This doesn't
create a problem for efficient implementation (as you can see by running the Python code!) If we do arithmetic on
numbers with billions of digits, more sophisticated techniques would be needed...
