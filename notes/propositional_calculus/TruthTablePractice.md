# Truth table examples

Here are some problems to get practice constructing truth tables
---

Write the truth table for 
```
    A and B or C
```
You should have a column for each of the two operators.
So it will have 5 columns total. 
This is a more compact form for the table as we write the
truth values for subexpressions underneath the operator

```
A B C  (A and B) or C
T T T      T      T
T T F      T      T
T F T      F      T
T F F      F      F
F T T      F      T
F T F      F      F
F F T      F      T
F F F      F      F
```
Here is a more verbose way to write the table

```
A B C  (A and B) (A and B) or C
T T T      T               T
T T F      T               T
T F T      F               T
T F F      F               F
F T T      F               T
F T F      F               F
F F T      F               T
F F F      F               F
```

---

Write the Truth Table for
```
(A implies not (B and A))
```
You should have a column of four truth values under each  operator. So it will have the structure with four rows and five columns
```
A B (A implies not (B and A)
T T       ?     ?      ?     
T F
F T
F F
```
=
