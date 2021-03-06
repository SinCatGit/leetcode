from typing import List


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        https://leetcode.com/problems/remove-k-digits/

        Given a non-negative integer num represented as a string, remove k 
        digits from the number so that the new number is the smallest possible.

        Note:
        The length of num is less than 10002 and will be ≥ k.
        The given num does not contain any leading zero.

        Example 1:
        
        Input: num = "1432219", k = 3
        Output: "1219"
        Explanation: Remove the three digits 4, 3, and 2 to form the new 
        number 1219 which is the smallest.

        Example 2:
        
        Input: num = "10200", k = 1
        Output: "200"
        Explanation: Remove the leading 1 and the number is 200. Note that the 
        output must not contain leading zeroes.
        Example 3:
        
        Input: num = "10", k = 2
        Output: "0"
        Explanation: Remove all the digits from the number and it is left with 
        nothing which is 0.

        Parameters
        ----------
        num: str
        k: int

        Returns
        -------
        str

        Examples
        --------
        >>> solution = Solution()
        >>> solution.removeKdigits('1432219', 3)
        '1219'
        >>> solution.removeKdigits('10200', 1)
        '200'
        >>> solution.removeKdigits('10', 2)
        '0'

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/remove-k-digits/discuss/88668/Short-Python-one-O(n)-and-one-RegEx
        .. [2] https://leetcode.com/problems/remove-k-digits/discuss/111931/Python-using-stack-O(n)-with-explain

        """
        stack = list()
        for n in num:
            while k and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)

        return ''.join(stack[:(-k or None)]).lstrip('0') or '0'

