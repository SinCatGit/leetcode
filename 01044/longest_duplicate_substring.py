

class Solution:
    def longestDupSubstring(self, S: str) -> str:
        """
        #### [1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/)

        Given a string `S`, consider all *duplicated substrings*: (contiguous) substrings of S that occur 2 or more times. (The occurrences may overlap.)

        Return **any** duplicated substring that has the longest possible length. (If `S` does not have a duplicated substring, the answer is `""`.)

        **Example 1:**

        ```
        Input: "banana"
        Output: "ana"
        ```

        **Example 2:**

        ```
        Input: "abcd"
        Output: ""
        ```

        **Note:**

        1. `2 <= S.length <= 10^5`
        2. `S` consists of lowercase English letters.

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
        .. [1] https://leetcode.com/articles/longest-duplicate-substring/

        """
        n = len(S)
        nums = [ord(c)-ord('a') for c in S]
        a, mod = 26, 2**32

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
        start = search(left-1)
        return S[start:start+left-1]

