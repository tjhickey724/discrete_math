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

Try it out!

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


