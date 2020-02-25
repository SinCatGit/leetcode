from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        https://leetcode.com/problems/permutation-sequence

        The set [1,2,3,...,n] contains a total of n! unique permutations.

        By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

        "123"
        "132"
        "213"
        "231"
        "312"
        "321"
        Given n and k, return the kth permutation sequence.

        Note:

        Given n will be between 1 and 9 inclusive.
        Given k will be between 1 and n! inclusive.
        Example 1:

        Input: n = 3, k = 3
        Output: "213"
        Example 2:

        Input: n = 4, k = 9
        Output: "2314"

        Parameters
        ----------
        n: int
        k: int

        Returns
        -------
        str

        Examples
        --------
        >>> sol = Solution()
        >>> sol.getPermutation(3, 3)
        '213'
        >>> sol.getPermutation(4, 9)
        '2314'

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/permutation-sequence/discuss/22507/%22Explain-like-I'm-five%22-Java-Solution-in-O(n)
        .. [2] https://leetcode.com/problems/permutation-sequence/discuss/22659/Python-concise-solution

        """
        import math
        tokens = [str(i) for i in range(1, n+1)]
        res = ''
        k = k-1
        while n > 0:
            n -= 1
            a, k = divmod(k, math.factorial(n))
            res += tokens.pop(a)
        return res


