from typing import List


class Solution:
    def getFactors(self, n: int) -> List[int]:
        """
        https://leetcode.com/problems/factor-combinations

        Numbers can be regarded as product of its factors. For example,

        8 = 2 x 2 x 2;
          = 2 x 4.
        Write a function that takes an integer n and return all possible combinations of its factors.

        Note:

        Each combination's factors must be sorted ascending, for example: The factors of 2 and 6 is [2, 6], not [6, 2].
        You may assume that n is always positive.
        Factors should be greater than 1 and less than n.


        Examples:
        input: 1
        output:

        []
        input: 37
        output:

        []
        input: 12
        output:

        [
          [2, 6],
          [2, 2, 3],
          [3, 4]
        ]
        input: 32
        output:

        [
          [2, 16],
          [2, 2, 8],
          [2, 2, 2, 4],
          [2, 2, 2, 2, 2],
          [2, 4, 4],
          [4, 8]
        ]



        Parameters
        ----------
        n: int

        Returns
        -------
        List[int]

        Examples
        --------
        >>> sol = Solution()
        >>> sol.getFactors(12)
        [[2, 6], [2, 2, 3], [3, 4]]

        Notes
        -----

        References
        ---------
        .. [1] https://www.cnblogs.com/grandyang/p/5332722.html
        .. [2]

        """
        todos = [(n, 2, [])]
        combes = []
        while todos:
            n, i, comb = todos.pop()
            while i * i <= n:
                if n % i == 0:
                    combes += comb + [i, n//i],
                    todos += (n//i, i, comb+[i]),
                i += 1
        return combes

    def getFactorsV01(self, n: int) -> List[int]:
        def dfs(i, n, comb, combes):
            while i * i <= n:
                if n % i == 0:
                    combes += comb + [i, n//i],
                    dfs(i, n//i, comb+[i], combes)

                i += 1
            return combes
        return dfs(2, n, [], [])

