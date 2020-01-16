class Solution:
    def calculate(self, s: str) -> int:
        """
        https://leetcode.com/problems/basic-calculator-ii/

        Implement a basic calculator to evaluate a simple expression string.

        The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
        The integer division should truncate toward zero.

        Parameters
        ----------
        s: str

        Returns
        -------
        int

        Examples
        --------
        >>> solution = Solution()
        >>> solution.calculate('3+2*2')
        7
        >>> solution.calculate(' 3/2 ')
        1
        >>> solution.calculate(' 3+5 / 2 ')
        5

        Notes
        -----

        References
        ---------
        .. [1] https://github.com/grandyang/leetcode/issues/227

        """
        stack = list()
        num = 0
        op = '+'
        for i, c in enumerate(s):
            if c.isalnum():
                num = num*10+int(c)

            if c in '+-*/' or i == len(s)-1:
                if op == '+':
                    stack.append(num)
                if op == '-':
                    stack.append(-num)
                if op == '*':
                    stack.append(stack.pop()*num)
                if op == '/':
                    stack.append(int(stack.pop()/num))
                op = c
                num = 0

        return sum(stack)


