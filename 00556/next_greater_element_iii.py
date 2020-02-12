class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
        https://leetcode.com/problems/next-greater-element-iii/

        Given a positive 32-bit integer n, you need to find the smallest 32-bit 
        integer which has exactly the same digits existing in the integer n and 
        is greater in value than n. If no such positive 32-bit integer exists, 
        you need to return -1.

        Parameters
        ----------
        n: int

        Returns
        -------
        int

        Examples
        --------
        >>> sol = Solution()
        >>> sol.nextGreaterElement(12)
        21
        >>> sol.nextGreaterElement(21)
        -1

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/next-greater-element-iii/discuss/197421/Python-100-solution.-Same-logic-behind-next-permutation.

        """
        digits = list(str(n))
        i = len(digits)-2
        while i >= 0 and digits[i] >= digits[i+1]:
            i -= 1
        if i == -1:
            return -1

        j = i + 1
        while j < len(digits) and digits[i] < digits[j]:
            j += 1
        digits[i], digits[j-1] = digits[j-1], digits[i]
        return int(''.join(digits[0:i+1]+digits[-1:i-len(digits):-1]))


if __name__ == '__main__':
    sol = Solution()
    print(sol.nextGreaterElement(12))
