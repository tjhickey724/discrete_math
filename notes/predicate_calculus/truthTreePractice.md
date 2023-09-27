# Truth Tree Practice

We can try some of the examples from [The Logic Notes](https://users.cecs.anu.edu.au/~jks/LogicNotes/exercises3.html)

Here's another to try.
🔗A: Alice

🔗C(x): True if x has a Coach class ticket.

🔗O(x, y) True if Person x may Occupy seat y.

🔗F(x) True if x gets a First class ticket.

🔗Prove: ∀x ((C(x) ∧ ¬∃y (O(x, y))) → F(x)) If anyone has a coach class ticket but there is no coach seat then that passenger gets a first class ticket.

🔗C(A) Alice has a coach class ticket.

🔗∀y (¬O(A, y)) Every coach seat is one that cannot be occupied by Alice.

🔗∴ F(A) Alice gets a first class ticket.

