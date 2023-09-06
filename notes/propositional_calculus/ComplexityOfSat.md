# Estimating the time required to test for satisfiability

We know that we can test whether a Propositional Formula is satisifable using the Truth Table,
but how long will this take? Is it a practical method?

Suppose we have a formula with N variables, then the truth table will have $2^N$ rows.
Suppose we have a computer program which can process M rows per seconds
then it would take $2^N/M$ seconds. This is called exponential complexity.
Let's see what it looks like where we let M = 1 billion

| N | rows = $2^N$ |seconds = $2^N/M$ | days | years | millenia |
| --- | ---  | --- | --- | --- | --- | 
|10 |  1024 | 0.000001 | . | . | . | . |
| 50 | 1125899906842624 | 1125899.9| 13.03 |  0.035| 0.000035 |
| 100 | $1.26 * 10^{30}$ | $1.26 * 10^{21}$ | 14,671,881,947,085,990 | 40,169,423,537,538.65 | 40,169,423,537.5 |

As you can see already at N=100 it would take 40 trillion years and the table would have $10^{30}$ rows,
so this is just not practical for any but the smallest problems.
