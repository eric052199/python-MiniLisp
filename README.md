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

Casting: Not allowed, but type checking is a bonus feature.

