from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        https://leetcode.com/problems/combination-sum-iii

        Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

        Note:

        All numbers will be positive integers.
        The solution set must not contain duplicate combinations.
        Example 1:

        Input: k = 3, n = 7
        Output: [[1,2,4]]
        Example 2:

        Input: k = 3, n = 9
        Output: [[1,2,6], [1,3,5], [2,3,4]]

        Parameters
        ----------
        k: int
        n: int

        Returns
        -------
        List[List[int]]

        Examples
        --------
        >>> sol = Solution()
        >>> sorted(sol.combinationSum3(3, 7)
        [[1, 2, 4]]
        >>> sorted(sol.combinationSum3(3, 9)
        [[1, 2, 6], [1, 3, 5], [2, 3, 4]]

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/combination-sum-iii/discuss/60624/Clean-167-liners-(AC)

        """
        self.ans = []

        def dfs(start, k, n, path):
            if k == 0 and n == 0:
                self.ans.append(path)
                return
            if k <= 0 or start > n:
                return
            dfs(start+1, k-1, n-start, path+[start])
            dfs(start+1, k, n, path)

        dfs(1, k, n, [])
        return self.ans

    def combinationSum3V01(self, k, n):
        from itertools import combinations
        return [list(c) for c in combinations(range(1, 10), k) if sum(c) == n]

