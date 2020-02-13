

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        https://leetcode.com/problems/decode-ways/

        A message containing letters from A-Z is being encoded to numbers using the following mapping:

        'A' -> 1
        'B' -> 2
        ...
        'Z' -> 26
        Given a non-empty string containing only digits, determine the total number of ways to decode it.

        Parameters
        ----------
        s: str

        Returns
        -------
        int

        Examples
        --------
        >>> sol = Solution()
        >>> sol.numDecodings('012')
        0
        >>> sol.numDecodings('102')
        1

        Notes
        -----

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=ZLwwc3-vVP4

        """
        if not s or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1

        dp0, dp1 = 1, 1
        for i in range(2, len(s)+1):
            dpi = 0
            if s[i-1] != '0':
                dpi += dp1
            if (s[i-2] == '2' and s[i-1] <= '6') or s[i-2] == '1':
                dpi += dp0
            dp0, dp1 = dp1, dpi
        return dp1


if __name__ == '__main__':
    sol = Solution()
    print(sol.numDecodings('12'))

