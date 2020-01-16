class Solution:
    def calculate(self, s: str) -> int:
        """
        https://leetcode.com/problems/basic-calculator/

        Implement a basic calculator to evaluate a simple expression string.
        The expression string may contain open ( and closing parentheses ), the plus + or minus sign -,
        non-negative integers and empty spaces .

        Parameters
        ----------
        s: str

        Returns
        -------
        int

        Examples
        --------
        >>> solution = Solution()
        >>> solution.calculate('1 + 1')
        2
        >>> solution.calculate(' 2-1 + 2 ')
        3
        >>> solution.calculate('(1+(4+5+2)-3)+(6+8)')
        23

        Notes
        -----
        简单迭代实现计算器。

        输入的算式总是有效的，意味着括号总是匹配。初始的sign=1，累计循环数字num=0，计算结果result=0。

        针对5种输入分别处理:
        1. 数字: 累计入当前的num
        2. '+': 数字结束，sign和num相乘加入result，重新设置sign=1，num=0
        3. '-': 数字结束，sign和num相乘加入result，重新设置sign=-1，num=0
        4. '(': 把目前计算的result和sign放入栈，设置result=0，开始计算括号内式子。
        5. ')': 括号内式子计算结束，弹出栈顶的sign与当前result相乘；弹出栈顶先前计算结果与当前result相加。重新赋值sign=1，num=0

        在只有一个数字的情况下，判断num是否为0，不为0，累加入result。
        """
        result, num, sign = 0, 0, 1
        stack = list()
        for c in s:
            if c.isalnum():
                num = num*10+int(c)
            elif c == '+':
                result += sign*num
                num = 0
                sign = 1
            elif c == '-':
                result += sign*num
                num = 0
                sign = -1
            elif c == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif c == ')':
                result += sign*num
                result *= stack.pop()
                result += stack.pop()
                sign = 1
                num = 0

        return result + sign*num


