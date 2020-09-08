import re
import sys
from MathematicalOperations import *
from HelperFunctions import *

string = sys.argv[1]


def StringCalculate(string):
    string = EvaluateParentheses(string)            # Calculates all the values inside the parentheses
    operators = re.findall("[0-9]+([\*\-\+/]*)[0-9]+", string)      # Finds all the remaining operators
    while operators != [""]:    # while there are still operators in the input string...
        string = EvaluateOperation(string)      # evaluate an operation in the input string.
        operators = re.findall("[0-9]+([\*\-\+/]*)[0-9]+", string)      # check the input string for operators again
    return string


print(StringCalculate(string))
