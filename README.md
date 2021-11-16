## Overview

LISP is an ancient programming language based on S-expressions and lambda calculus.

All operations in Mini-LISP are written in parenthesized prefix notation. For example, a
simple mathematical formula “(1 + 2) * 3” written in Mini-LISP is:
```
(* (+ 1 2) 3)
```
As a simplified language, Mini-LISP has only three types (Boolean, number and function)
and a few operations. 

## Type Definition

- Boolean: Boolean type includes two values, #t for true and #f for false.
- Number: Signed integer from −(2^31) to 2^31 – 1, behavior out of this range is not defined.
- Function: See Function.

> Casting: Not allowed, but type checking is a bonus feature.

![minilisp](https://user-images.githubusercontent.com/94356490/141923854-3bc8377c-4013-4561-ad17-27f30c405ac5.PNG)
![image](https://user-images.githubusercontent.com/94356490/141924227-e5cf4138-61bb-4a93-9b6e-5814a6cef604.png)

### Other Operators: 
- define 
- fun 
- if

> Note that all operators are reserved words, you cannot use any of these words as ID.

### Lexical Details
- Preliminary Definitions:
```
separator ::= ‘\t’(tab) | ‘\n’ | ‘\r’ | ‘ ’(space)
letter ::= [a-z]
digit ::= [0-9]
```
- Token Definitions:
```
number ::= 0 | [1-9]digit* | -[1-9]digit*
Examples: 0, 1, -23, 123456
ID ::= letter (letter | digit | ‘-’)*
Examples: x, y, john, cat-food
bool-val ::= #t | #f
```
