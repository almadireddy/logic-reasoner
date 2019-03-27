# Logic Reasoner

### A Knowledge Base Reasoner written in Python

Created for CS 4365 Artificial Intelligence

---

This is a logic resolver that figures out validity of sentences using a proof by contradiction. 

## Syntax

`~p q` represents `NOT p OR q`

If a sentence has `AND`s in it, it gets split and added into KB with each individual atom in that sentence as its own sentence.  

## Example

First `n-1` lines are the initial Knowledge Base.
The last line `n` is the sentence that we are testing

#### Input: 
```text
~p q
~z y
~q p
q ~p z
q ~p ~z
~z y ~p   
```

#### Output:
```text
1. ~p q {}
2. ~z y {}
3. ~q p {}
4. q ~p z {}
5. q ~p ~z {}
6. z {}
7. ~y {}
8. p {}
9. q ~p y {4, 2}
10. y {6, 2}
11. ~z {7, 2}
12. q {8, 1}
13. q z {8, 4}
14. q ~z {8, 5}
15. q y {9, 8}
16. Contradiction {10, 7}
Valid
```

This shows that the sentence `~z y ~p` holds for this knowledge base.
