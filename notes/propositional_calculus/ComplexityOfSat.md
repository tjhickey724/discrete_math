# Estimating the time required to test for satisfiability

We know that we can test whether a Propositional Formula is satisifable using the Truth Table,
but how long will this take? Is it a practical method?

Suppose we have a formula with N variables, then the truth table will have $2^N$ rows.
Suppose we have a computer program which can process M rows per seconds
then it would take $2^N/M$ seconds. This is called exponential complexity.
Let's see what it looks like where we let 

M = 1 billion rows per second

| N | rows = $2^N$ |seconds = $2^N/M$ | days=seconds/(24*3600) | years=days/365.25 | millenia=years/1000 |
| --- | ---  | --- | --- | --- | --- | 
|10|1024.0|0.000001024|-|-|-|
|20|1048576.0|0.001048576|-|-|-|
|30|1073741824.0|1.073741824|-|-|-|
|40|1099511627776.0|1099.511627776|0.01272|-|-|
|50|1125899906842624.0|1125899.906842624|13.0312|0.0357|-|
|60|1.15e+18|1152921504.606847|13343.99|36.55|0.03655|
|70|1.18e+21|1180591620717.4114|13664254.86|37436.3|37.4|
|80|1.2089e+24|1208925819614629.2|13992196986.2|38334786.2|38334.7|
|90|1.2379e+27|1.237e+18|14328009713951.1|39254821134.11277|39254821.1|
|100|1.2676e+30|1.267e+21|1.467e+16|40196936841331.4|40196936841.3|


As you can see already 

at N=50 it would take 13 days

at N=60 it would take 37 years

at N= 70 it would take 37 millenia

at N=100 it would take 40 trillion millenia and the table would have $10^{30}$ rows,

This is a perfect example of what we call exponential growth, and any algorithm which has exponential growth
quickly becomes unusable!

So the Truth Table method is just not practical for testing satisfiability for any but the smallest Propositional Logic formulas.

One way around this is to look for other ways to check if a formula is satisiable or is a tautology. We will look at two approaches:
* logical inference rules
* the truth tree method

In many cases these new methods can be used to find solutions to larger problems much faster than the Truth Table method, but in the worst case
they are still exponential.  It is an open problem (and a very important one) to see if there is an algorithm to test for satisfiability
that is substantialy faster than the exponential Truth Table method.  This is known as the P vs NP problem and you can learn more about it
if you take a course in the "Theory of Computation"




