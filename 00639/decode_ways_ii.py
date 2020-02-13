

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        https://leetcode.com/problems/decode-ways-ii/

        A message containing letters from A-Z is being encoded to numbers using the following mapping way:

        'A' -> 1
        'B' -> 2
        ...
        'Z' -> 26
        Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

        Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

        Also, since the answer may be very large, you should return the output mod 109 + 7.

        Parameters
        ----------
        s: str

        Returns
        -------
        int

        Examples
        --------
        >>> sol = Solution()
        >>> sol.numDecodings('*')
        9
        >>> sol.numDecodings('1*')
        18

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/decode-ways-ii/discuss/105262/Python-6-lines-DP-solution

        """
        ones = {str(k): 1 for k in range(1, 10)}
        ones.update({'0': 0, '*': 9})
        twos = {str(k): 1 for k in range(10, 27)}
        twos.update({'*'+str(k): 2 if k <= 6 else 1 for k in range(10)})
        twos.update({'1*': 9, '2*': 6, '**': 15})
        pre, cur = 1, ones.get(s[:1], 0)
        for i in range(1, len(s)):
            pre, cur = cur, (ones.get(s[i], 0)*cur + twos.get(s[i-1:i+1], 0)*pre) % 1000000007
        return cur



