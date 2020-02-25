from typing import List


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """
        https://leetcode.com/problems/palindrome-permutation

        Given a string, determine if a permutation of the string could form a palindrome.

        Example 1:

        Input: "code"
        Output: false
        Example 2:

        Input: "aab"
        Output: true
        Example 3:

        Input: "carerac"
        Output: true
        Hint:

        Consider the palindromes of odd vs even length. What difference do you notice?
        Count the frequency of each character.
        If each character occurs even number of times, then it must be a palindrome. How about
        character which occurs odd number of times?

        Parameters
        ----------
        s: str

        Returns
        -------
        bool

        Examples
        --------
        >>> sol = Solution()
        >>> sol.canPermutePalindrome('code')
        False
        >>> sol.canPermutePalindrome('aab')
        True

        Notes
        -----

        References
        ---------
        .. [1] https://www.cnblogs.com/grandyang/p/5223238.html
        .. [2] https://leetcode.com/problems/palindrome-permutation/discuss/69574/1-4-lines-Python-Ruby-C%2B%2B-C-Java

        """
        from collections import Counter

        return sum([v % 2 for v in Counter(s).values()]) < 2

    def canPermutePalindromeV01(self, s):
        from collections import Counter
        count = Counter(s)
        cnt = 0
        for v in count.values():
            if v % 2 == 1:
                cnt += 1
        return cnt == 0 or (len(s) % 2 == 1 and cnt == 1)

