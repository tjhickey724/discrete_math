# Estimating the time required to test for satisfiability

We know that we can test whether a Propositional Formula is satisifable using the Truth Table,
but how long will this take? Is it a practical method?

Suppose we have a formula with N variables, then the truth table will have $2^N$ rows.
Suppose we have a computer program which can process M rows per seconds
then it would take $2^N/M$ seconds. This is called exponential complexity.
Let's see what it looks like where we let 

M = 1 billion rows per second

| N | rows = $2^N$ |seconds = $2^N/M$ | days | years | millenia |
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


As you can see already at N=50 it would take 13 days

at N=60 37 years

at N= 70 37 millenia

and at N=100 it would take 40 trillion years and the table would have $10^{30}$ rows,

so the Truth Table method is just not practical for any but the smallest problems.
