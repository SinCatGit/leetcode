class Solution:
    def calculate(self, s: str) -> int:
        """
        https://leetcode.com/problems/basic-calculator-iii/

        Implement a basic calculator to evaluate a simple expression string.

        The expression string contains only non-negative integers, +, -, *, / operators,
        open ( and closing parentheses ) and empty spaces.

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
        >>> solution.calculate('6 - 4/2 ')
        4
        >>> solution.calculate('2*(5+5*2)/3+(6/2+8)')
        21
        >>> solution.calculate('(2+6* 3+5- (3*14/7+2)*5)+3')
        -12

        Notes
        -----

        References
        ---------
        .. [1] https://github.com/grandyang/leetcode/issues/227

        """
        stack = list()
        num = 0
        op = '+'
        s_len = len(s)
        i = 0
        while i < s_len:
            if s[i].isalnum():
                num = num*10+int(s[i])
            elif s[i] == '(':
                cnt = 1
                j = i
                while cnt != 0:
                    i += 1
                    if s[i] == '(':
                        cnt += 1
                    if s[i] == ')':
                        cnt -= 1
                num = self.calculate(s[j+1:i])

            if s[i] in '+-*/' or i == s_len-1:
                if op == '+':
                    stack.append(num)
                if op == '-':
                    stack.append(-num)
                if op == '*':
                    stack.append(stack.pop()*num)
                if op == '/':
                    stack.append(int(stack.pop()/num))
                op = s[i]
                num = 0
            i += 1

        return sum(stack)

    def calculateV01(self, s):
        stack = list()
        num = 0
        op = '+'
        for i, c in enumerate(s):
            if c.isalnum():
                num = num*10+int(c)

            if c in '+-*/)' or i == len(s)-1:
                if op == '+':
                    stack.append(num)
                if op == '-':
                    stack.append(-num)
                if op == '*':
                    stack.append(stack.pop()*num)
                if op == '/':
                    stack.append(int(stack.pop()/num))
                if op != ')':
                    op = c
                num = 0
            if c == '(':
                stack.append(op)
                stack.append(c)
                op = '+'

            if c == ')':
                t_sum = 0
                while stack[-1] != '(':
                    t_sum += stack.pop()
                stack.pop()
                op = stack.pop()
                num = t_sum
                if i == len(s)-1:
                    if op == '+':
                        stack.append(num)
                    if op == '-':
                        stack.append(-num)
                    if op == '*':
                        stack.append(stack.pop() * num)
                    if op == '/':
                        stack.append(int(stack.pop() / num))

        return sum(stack)


