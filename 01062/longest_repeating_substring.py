from typing import List


class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        """
        #### [1062. Longest Repeating Substring](https://leetcode.com/problems/longest-repeating-substring/)

        Given a string `S`, find out the length of the longest repeating substring(s). Return `0` if no repeating substring exists.

        **Example 1:**

        ```
        Input: "abcd"
        Output: 0
        Explanation: There is no repeating substring.
        ```

        **Example 2:**

        ```
        Input: "abbaba"
        Output: 2
        Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
        ```

        **Example 3:**

        ```
        Input: "aabcaabdaab"
        Output: 3
        Explanation: The longest repeating substring is "aab", which occurs 3 times.
        ```

        **Example 4:**

        ```
        Input: "aaaaa"
        Output: 4
        Explanation: The longest repeating substring is "aaaa", which occurs twice.
        ```

        **Note:**

        1. The string `S` consists of only lowercase English letters from `'a'` - `'z'`.
        2. `1 <= S.length <= 1500`

        Parameters
        ----------
        S: str

        Returns
        -------
        int

        Examples
        --------

        References
        ---------
        .. [1] https://leetcode.com/articles/longest-repeating-substring/

        """
        n = len(S)
        left, right = 1, n

        def search(L):
            seen = set()
            for i in range(n-L+1):
                if S[i:i+L] in seen:
                    return i
                seen.add(S[i:i+L])
            return -1

        while left <= right:
            L = left + (right-left)//2
            if search(L) != -1:
                left = L + 1
            else:
                right = L - 1

        return left - 1

    def longestRepeatingSubstringV01(self, S: str) -> int:
        n = len(S)
        nums = [ord(c)-ord('a') for c in S]
        a, mod = 26, 2**26

        def search(L):
            h = 0
            aL = pow(a, L, mod)
            for i in range(L):
                h = (h*a + nums[i]) % mod
            seen = {h}
            for i in range(1, n-L+1):
                h = (h*a - nums[i-1]*aL + nums[i+L-1]) % mod
                if h in seen:
                    return i
                seen.add(h)
            return -1

        left, right = 1, n
        while left <= right:
            L = left + (right-left)//2
            if search(L) != -1:
                left = L + 1
            else:
                right = L - 1

        return left - 1

