from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        https://leetcode.com/problems/evaluate-reverse-polish-notation/

        Evaluate the value of an arithmetic expression in Reverse Polish Notation.
        Valid operators are +, -, *, /. Each operand may be an integer or another expression.

        Division between two integers should truncate toward zero.
        The given RPN expression is always valid. That means the expression would always evaluate to a result and
        there won't be any divide by zero operation.

        Parameters
        ----------
        tokens: List[str]

        Returns
        -------
        int

        Examples
        --------
        >>> solution = Solution()
        >>> solution.evalRPN(['2', '1', '+', '3', '*'])
        9
        >>> solution = Solution()
        >>> solution.evalRPN(['4', '13', '5', '/', '+'])
        6
        >>> solution = Solution()
        >>> solution.evalRPN(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+'])
        22
        """
        stack = list()
        for t in tokens:
            if t not in '+-*/':
                stack.append(int(t))
            else:
                right = stack.pop()
                left = stack.pop()
                if t == '+':
                    stack.append(left+right)
                elif t == '-':
                    stack.append(left-right)
                elif t == '*':
                    stack.append(left*right)
                elif t == '/':
                    stack.append(int(left/right))

        return stack[0]

