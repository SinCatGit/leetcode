

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        https://leetcode.com/problems/remove-duplicate-letters/

        Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

        Example 1:

        Input: "bcabc"
        Output: "abc"
        Example 2:

        Input: "cbacdcbc"
        Output: "acdb"


        Parameters
        ----------
        s: str

        Returns
        -------
        str

        Examples
        --------
        >>> solution = Solution()
        >>> solution.removeDuplicateLetters('bcabc')
        'abc'
        >>> solution.removeDuplicateLetters('cbacdcbc')
        'acdb'

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/remove-duplicate-letters/discuss/76787/Some-Python-solutions
        .. [2] https://leetcode.com/problems/remove-duplicate-letters/discuss/76766/Easy-to-understand-iterative-Java-solution

        """
        stack = ''
        last_index = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            if c not in stack:
                while c < stack[-1:] and i < last_index[stack[-1]]:
                    stack = stack[:-1]
                stack += c
        return stack
