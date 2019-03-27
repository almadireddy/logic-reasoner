# Logic Reasoner

### A Knowledge Base Reasoner written in Python

Created for CS 4365 Artificial Intelligence

---

This is a logic resolver that figures out validity of sentences using a proof by contradiction. 

## Homework Usage
`python main2.py <.in file>` will use the .in file as the input, the first N-1 lines being initial knowledge base and the last Nth line being the clause to test. See example below.

## General Usage
**Constructor:** `kb = KB(lines)`, with `lines` being a list of strings representing clauses according to the syntax below. This forms the initial knowledge base

**ask():** `kb.ask(sentence)`, where sentence is a string with the sentence to test the validity of such as `"~p q x"`. Returns True if the sentence holds according to the proof by contradiction. It also prints all the sentences in the knowledge base as they are resolved to stdout.

**addClause():** `kb.addClause(clause)` where clause if an instance of `Clause`. If you have a `Clause()` for whatever reason, you can add it to the knowledge base using addClause().  

## Input Syntax

`~p q` represents `NOT p OR q`

If a sentence is generated and requires `AND`s in it, it gets split and added into KB with each literal on either side of the `AND` in that sentence as its own sentence. For example, `p AND q` becomes two separate clauses, `p` and `q` each on its own line.

## Example

First `n-1` lines are the initial Knowledge Base.
The last line `n` is the sentence that we are testing. There should be no `AND` operators in your file. 

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
