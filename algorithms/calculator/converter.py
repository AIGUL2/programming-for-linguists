"""
Programming for linguists

Implementation of the Reverse Polish Notation Converter
"""
from algorithms.calculator.reverse_polish_notation import (Digit, Op, ReversePolishNotation)
from data_structures.queue_ import Queue_
from data_structures.stack import Stack


class ReversePolishNotationConverterState:
    """
    Class to store the state of RPN convert process
    """

    def __init__(self, expression_in_infix_notation: str):
        """
        :param expression_in_infix_notation: string with expression in infix notation
        """
        self.expression_in_infix_notation = Queue_(expression_in_infix_notation)
        self.expression_in_postfix_notation = ReversePolishNotation()
        self.stack = Stack()

    def pop_from_stack_until_opening_bracket(self):
        """
        Help function
        :return:
        """


class ReversePolishNotationConverter:
    """
    Class for converting infix expressions to reverse polish notation
    """

    def __init__(self, expression_in_infix_notation: str):
        self.point = '.'
        self.priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.operators = set(['+', '-', '*', '/', '(', ')', '^'])
        self.output = ""
        self.rpn_cs = ReversePolishNotationConverterState(expression_in_infix_notation)

    def convert(self) -> str:
        """
        Main method of the class.
        Convert an infix expression to reverse polish notation

        :return: ReversePolishNotation object
        """
        for i in range(self.rpn_cs.expression_in_infix_notation.size()):
            if self.rpn_cs.expression_in_infix_notation.top() not in self.operators:
                self.output += self.rpn_cs.expression_in_infix_notation.get()
            elif self.is_open_bracket(self.rpn_cs.expression_in_infix_notation.top()):
                self.rpn_cs.stack.push(self.rpn_cs.expression_in_infix_notation.get())
            elif self.is_close_bracket(self.rpn_cs.expression_in_infix_notation.top()):
                while not self.is_open_bracket(self.rpn_cs.stack.top()) and not self.rpn_cs.stack.empty():
                    self.output += " " + self.rpn_cs.stack.top()
                    self.rpn_cs.stack.pop()
                self.rpn_cs.stack.pop()
            else:
                while not self.rpn_cs.stack.empty() and not self.is_open_bracket(self.rpn_cs.stack.top()) and self.priority[
                    self.rpn_cs.expression_in_infix_notation.top()] <= self.priority[self.rpn_cs.stack.top()]:
                    self.output += " " + self.rpn_cs.stack.top()
                    self.rpn_cs.stack.pop()
                self.output += " "
                self.rpn_cs.stack.push(self.rpn_cs.expression_in_infix_notation.get())
        while not self.rpn_cs.stack.empty():
            self.output += " " + self.rpn_cs.stack.top()
            self.rpn_cs.stack.pop()
        print(self.output)
        return self.output

    @staticmethod
    def pop_from_stack_until_prioritizing(operator: Op, state: ReversePolishNotationConverterState):
        """
        Help function to move elements from stack to state elements (operators)
        until element on the top of the stack  has less priority then current operator
        :param operator: Instance of Op class - current operator
        :param state: State of the RPN convert process
        """

    def read_digit(self, state) -> Digit:
        """
        Method to read a digit from self._infix_notation

        :param state: expression in Reverse Polish Notation Format
        :return: Instance of Digit class
        """


    @staticmethod
    def is_part_of_digit(character: str) -> bool:
        """
        Help function to check if symbol is a part of floating point number
        :param character: current symbol
        :return: True if character can be part of a digit, else False
        """

    def is_open_bracket(self, operator: Op) -> bool:
        """
        Method to check if the next character in the infix expression is open bracket

        :param operator: Operator redden from the infix expression
        :return: True id this operator is the open bracket operator else False
        """
        if operator == '(':
            return True
        return False

    def is_close_bracket(self, operator: Op) -> bool:
        """
        Method to check if the next character in the infix expression is close bracket

        :param operator: Operator redden from the infix expression
        :return: True id this operator is the close bracket operator else False
        """
        if operator == ')':
            return True
        return False

    @staticmethod
    def is_binary_operation(operator: Op) -> bool:
        """
        Method to check if the next character in the infix expression is binary operator

        :param operator: Operator redden from the infix expression
        :return: True id this operator is the binary operator else False
        """


a = ReversePolishNotationConverter("13+7*(5*6)")
a.convert()
####check