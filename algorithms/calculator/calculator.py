"""
Programming for linguists

Implementation of the Reverse Polish Notation Converter
"""
from algorithms.calculator.reverse_polish_notation import ReversePolishNotation
from data_structures.stack.stack import Stack
from converter import ReversePolishNotationConverter


class ReversePolishNotationCalculator:
    """
    Calculator of expression in Reverse Polish Notation
    """
    def __init__(self):
        self.stack = Stack()
        self.ops = {
            "+": (lambda a, b: a + b),
            "-": (lambda a, b: a - b),
            "*": (lambda a, b: a * b),
            "/": (lambda a, b: a / b)
        }

    def calculate(self, expr) -> int:
        """
        Main method of the ReversePolishNotationCalculator class.
        Calculating result of expression in Reverse Polish Notation.

        :param rpn_expression: expression in Reverse Polish Notation Format
        :return: result of the expression
        """
        a = ReversePolishNotationConverter(expr)
        result = a.convert().split()

        for res in result:
            if res in self.ops:
                operand2 = self.stack.top()
                self.stack.pop()
                operand1 = self.stack.top()
                self.stack.pop()
                rst = self.ops[res](operand1, operand2)
                self.stack.push(rst)
            else:
                self.stack.push(int(res))

        return int(self.stack.top())


calc = ReversePolishNotationCalculator()
print(calc.calculate("15+7*(15/5*6)"))
