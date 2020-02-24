from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        https://leetcode.com/problems/combinations

        Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

        Example:

        Input: n = 4, k = 2
        Output:
        [
          [2,4],
          [3,4],
          [2,3],
          [1,2],
          [1,3],
          [1,4],
        ]


        Parameters
        ----------
        n: int
        k: int

        Returns
        -------
        List[List[int]]

        Examples
        --------
        >>> sol = Solution()
        >>> sorted(sol.combine(4, 2))
        [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3,4]]

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/combinations/discuss/27024/1-liner-3-liner-4-liner
        .. [2] https://leetcode.com/problems/combinations/discuss/27202/Fast-and-simple-python-code-.-recursive

        """
        if k == 1:
            return [[i] for i in range(1, n+1)]
        if k == n:
            return [list(range(1, n+1))]
        if k < 1 or k > n:
            return []

        used = self.combine(n-1, k)
        part = self.combine(n-1, k-1)

        return used + [item+[n] for item in part]

    def combineV01(self, n, k):
        from itertools import combinations
        return [ list(item) for item in combinations(range(1, n+1), k)]

