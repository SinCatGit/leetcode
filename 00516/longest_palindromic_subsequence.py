class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        https://leetcode.com/problems/longest-palindromic-subsequence/

        Given a string s, find the longest palindromic subsequence's length in s.
        You may assume that the maximum length of s is 1000.

        Parameters
        ----------
        s: str

        Returns
        -------
        int

        Examples
        --------

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=v8irqkTcJ6s&list=PLTNkreZiUTIL-S_VJBLRxlmGktAQtla-m&index=8
        .. [2] https://www.youtube.com/watch?v=_nCsPn7_OgI
        .. [3] https://leetcode.com/problems/longest-palindromic-subsequence/discuss/99153/Fast-and-concise-Python-solution-that-actually-gets-AC

        """
        s_len = len(s)
        dp = [0 for _ in range(s_len)]
        for i in range(s_len-1, -1, -1):
            dp[i] = 1
            m_plus_minus_one = 0
            for j in range(i+1, s_len):
                if s[j] == s[i]:
                    mij = 2 + m_plus_minus_one
                else:
                    mij = max(dp[j-1], dp[j])
                m_plus_minus_one = dp[j]
                dp[j] = mij
        return dp[-1]

    def longestPalindromeSubseqV02(self, s):
        d = {}

        def f(fs):
            if fs in d:
                return d[fs]
            max_len = 0
            for c in set(fs):
                i, j = fs.find(c), fs.rfind(c)
                max_len = max(max_len, 1 if i == j else 2 + f(fs[i+1:j]))
            d[s] = max_len
            return d[s]
        f(s)
        return d[s]

    def longestPalindromeSubseqV01(self, s):
        s_len = len(s)
        dp = [[0 for _ in range(s_len)] for _ in range(s_len)]
        for i in range(s_len-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, s_len):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])

        return dp[0][-1]


