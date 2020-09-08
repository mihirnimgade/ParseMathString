# Helper functions

import re
from MathematicalOperations import *


def EvaluateParentheses(string):    # Evaluates all the expressions inside parentheses
    parenthetical_ops = []          # stores all the sums inside parentheses
    parenthetical_results = []      # stores the results of the sums inside the parentheses
    parentheses_start = False       # flag for the start of parentheses
    parentheses_string = ""         # stores the sum found inside parentheses

    for char in string:
        if char == "(":
            parentheses_start = True
        if parentheses_start:
            parentheses_string = parentheses_string + char      # add each character that comes after a "("
        if char == ")":
            parentheses_start = False                           # stop adding characters
            parenthetical_ops.append(parentheses_string)        # add the sum to the array of sums that are inside parentheses
            parentheses_string = ""                             # resets the character accumulator

    for ops in parenthetical_ops:       # for each sum in the array
        ops = ops.strip("()")           # removes the parentheses
        operator = re.findall("[0-9]+([\*\-\+/]*)[0-9]+", ops)[0]      # finds out the operator inside the parentheses
        numbers = re.findall("([0-9]+)", ops)                           # finds out the numbers that need to be operated on

        if operator == "+":                                     # line 59 to 68 actually performs the operations
            result = add(numbers[0], numbers[1])
        elif operator == "-":
            result = subtract(numbers[0], numbers[1])
        elif operator == "*":
            result = multiply(numbers[0], numbers[1])
        elif operator == "**":
            result = exponent(numbers[0], numbers[1])
        else:
            result = divide(numbers[0], numbers[1])

        parenthetical_results.append(result)        # adds the result to another array

    for i in range(0, len(parenthetical_ops)):      # basically replaces the sums with the results in the input array
        string = string.replace(str(parenthetical_ops[i]), str(parenthetical_results[i]))

    return(string)


def EvaluateOperation(string):
    if "**" in string:
        sum = re.findall("[0-9]*\*\*[0-9]*", string)[0]     # stores the sum itself and finds it using re
        numbers = re.findall("[0-9]+", sum)                 # stores the numbers to be operated on in array form
        result = str(exponent(numbers[0], numbers[1]))      # calculates result
        string = string.replace(sum, result)                # replaces the operation with the result in the input string
        return string                                       # the following code is exactly the same expect for a few changes in the regular expressions
    elif "/" in string:
        sum = re.findall("[0-9]*/[0-9]*", string)[0]
        numbers = re.findall("[0-9]+", sum)
        result = str(divide(numbers[0], numbers[1]))
        string = string.replace(sum, result)
        return string
    elif "*" in string:
        sum = re.findall("[0-9]*\*[0-9]*", string)[0]
        numbers = re.findall("[0-9]+", sum)
        result = str(multiply(numbers[0], numbers[1]))
        string = string.replace(sum, result)
        return string
    elif "+" in string:
        sum = re.findall("[0-9]*\+[0-9]*", string)[0]
        numbers = re.findall("[0-9]+", sum)
        result = str(add(numbers[0], numbers[1]))
        string = string.replace(sum, result)
        return string
    else:
        sum = re.findall("[0-9]*\-[0-9]*", string)[0]
        numbers = re.findall("[0-9]+", sum)
        result = str(subtract(numbers[0], numbers[1]))
        string = string.replace(sum, result)
        return string
