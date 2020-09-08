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

## Usage

To use the function to evaluate the mathematical string, open your terminal and enter:

```
python StringEvaluate.py <your-string-here>
```

### Example

A usage example is shown below:

```
python StringEvaluate.py (6**2)-4/2-6
```
The above command returns `28` as you would expect.

## Supported mathematical operations

Currently the code supports the following mathematical operations:

- Addition (+)
- Subtraction (-)
- Multiplication (\*)
- Division (/)
- Exponents (\*\*)

NOTE: the function only supports integer operations currently.
