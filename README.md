# ParseMathString

Welcome to ParseMathString!

## Overview

This repository contains a Python function that takes in a string and evaluates all the mathematical operations within it. This parsing of the string is
done entirely with regular expressions.

For example, if it is given:

```python
inputString = "(6**2)-4/2-6"
```
It will evaluate that string to `28`.

## Supported mathematical operations

Currently the code supports the following mathematical operations:

- Addition (+)
- Subtraction (-)
- Multiplication (\*)
- Division (/)
- Exponents (\*\*)

NOTE: the function only supports integer operations currently.
