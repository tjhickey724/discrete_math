# Correctness of the RSA algorithm

In these notes we will show how to implement RSA and sketch a proof of each step.
You can see a complete treatment of RSA in Chapter 8.11 of 
[Mathematics for Computer Science by Lehman, Leighton, and Meyer](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/)

## Euclid's Algorithm
First we introduce Euclid's algorithm for finding the greatest common divisor of two positive integer m and n.

The greatest common divisor d of m and n is the largest integer which divides both m and n, that is
$m = m_1 d$ and $n=n_1 d$ and $m_1$ and $n_1$ have no common divisors larger than 1.

The following Python program calculates the gcd:

``` python
def gcd(a,b):
    ''' returns the greatest common divisor of a and b
    '''
    if b==0:
        return a
    else:
        c = a%b
        d = gcd(b,c)
        return d
```

Try it out by finding the gcd of 
* 21 and 15 or
* 105 and 49


## Bézout's identity
By modifying the algorithm slightly we can show that if d is the gcd of m and n, then there are positive integers a and b
such that

$a m + b n = d$

This is known as Bézout's identity.

Here is the code with the proof of its correctness embedded as comments.
``` python
def gcd(a,b):
    ''' returns tuple (d,m,n)
        where gcd(a,b)=d and
        d = m*a+n*b
    '''
    if b==0:
        return (a,1,0)
    else:
        c = a%b
        (d,m1,n1) = gcd(b,c)
        # by induction we know that
        # m1*b + n1*c = d
        # and by definition of // and %
        # a = (a//b)*b+ c
        # so c = a - (a//b)*b
        # so m1*b + n1*a -n1*(a//b)*b = d
        # so m = n1 n=m1-n1*(a//b)
        return (d,n1,m1-n1*(a//b))
```

Try it out by finding the coeficients a and b for the gcds of 
* 21 and 15 or
* 105 and 49

## The Division Algorithm
One very important feature of the integers is the division algorithm which states that
for any integers m and n with $n\gt 0$ there are unique integers $q$ and $r$ with $0\le r \lt n$ such that
* $m = qn+r$

In Python we calculate these with ```//``` for division and ```%``` for remainder
```
q = m//n
r = m%n
```

## The Finite Field $\mathbb{F}_p$ for primes p.
Let $p$ be a prime and let $\mathbb{F}_p$ be the set of integers $\\{0,1,2,\ldots,p-1\\}$.
We can define addition and multiplication on this set by
* $(x * y) % p$
* $(x + y) % p$

where $u % v$ is the result of dividing u by v and taking the remainder. 
It is not hard to prove that addition and multipication satisfy the standard properties:
* additive identity:  $x+0=x$
* multiplicative $x*1=x$
* additive commutativity: $x+y=y+x$
* multiplicative commutativity $x * y=y * x$
* additive associativity: $x+(y+z)=(x+y)+z$
* multiplicative associativity: $x * (y * z) = (x * y) * z$
* distributivity: $x * (y+z)=x * y+x * z$
* additive inverse: $\forall x \exists y \ x+y = 0$
* multiplicative inverse: $\forall x\  x\ne 0 \rightarrow \exists y\ x*y=1$

The last follows from Bézout's Theorem because if $x\ne 0$ then gcd(x,p)=1 so there exists a,b with
* $ax + bp = 1$

which means that $a*x= 1$ modulo p.

These properties make $\mathbb{F}_p$ into a mathematical object called a Field.
Other fields are the rational numbers and the real numbers and the complex numbers.

## Fermat's Little Theorem

**Theorem** Let $p$ be a prime and $x$ an integer not divisible by $p$, then
* $p$ divides $x^p - x$

**Proof**
First we prove that $(p-1)! = -1$ mod p

To do this observe that each non-zero element $x$ of $\mathbb{F}_p$ has a unique inverse $x^{-1}$
and that $x \ne x^{-1}$ unless x is 1 or -1. To see this, note that
* $x = x^{-1}$ implies $x * x = x * x^{-1} = 1$ so $x^2 = 1$ so $x^2-1 = (x-1)(x+1) = 0$
* so $x-1=0$ or $x+1=0$
* so $x = 1$ or $x=-1$

So $(p-1)! = 1 * 2 * \ldots * (p-2) * (p-1)$ 

and 
all of the numbers except the first and the last can be paired with their inverse. So multiplying them
gives $1$ and we conclude that
* $(p-1)! = 1 * 2 * \ldots * (p-2) * (p-1) = 1 * (p-1) = -1$ mod p

Now suppose we multiply each of those factors in $(p-1)!$ by some $x$ with 1\le x \lt p$, then we get
* $(1 * x) * (2 * x) * \dots * (p-1) * x = (p-1)! x^{p-1}$

but it is not hard to see that
* $((1 * x),(2 * x),  \dots , (p-1) * x)$ is a permutation of $(1,2,...,p-1)$

and hence has the same product! so
* $(1 * x) * (2 * x) * \dots * (p-1) * x = (p-1)! x^{p-1} = (p-1)! = -1$

and so we can conclude that 
* $x^{p-1} = 1$ mod p, so
* $x^p = x$ mod p, that is
* $p$ divides $x^p - x$

Let's try it out with $p=5$ or $p=7$ and various $x$.

# Fast probabalistic test for primality
We can use Fermat's little theorem to quickly test if a number is "probably" prime.
I won't prove it here, but if $p$ is not prime then 
* the probability that $x^p=x$ mod p is less than 1/2

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
    p = 1
    while n>0:
        # invariant on (p,x,n,m) is p* x^n mod m at top of the loop
        if n%2==0:
            #x^n= x^(2r)=(x^2)*r
            x = (x*x)%m
            n = n//2
        else:
            # p*x^n = 
            # p*x^(2r+1)=
            # (p*x)*(x^2)^r
            p = (p*x)%m
            x = (x*x)%m
            n = (n-1)//2
    
    return p
```

We can then use this to test primality and to generate large primes as follows
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
    n = randint(10**d,10**(d+1))
    while not prime_test(n,100):
        n=n+1
    return n
```
