# Constant folding for logical expression
Python script to simplify logical expression with constant values, while preserving original order of operations and their syntax as much as possible.`

Works for fortran-style expression so far, but shoud be easily modifiable for other languages as well.

# Workflow
1. Substitute function calls and subscripted arrays, so that following logic can be simpler.
2. Convert original expression to Reverse Polish Notation (or also postfix notation) using a modified "shunting yard" algorithm to preserve parenthesization.
3. Parse the RPN list back to infix notation, while getting rid of redundant expressions.
4. Substitute back the function calls and subsripted arrays to obtain the final simplified expression.

## Examples:
  .not. .not.a >  2.and..true. .and. ( arr(l2(1),2) .or. .false.)
  
  gets converted to
  
  a >  2 .and. arr(l2(1),2)
