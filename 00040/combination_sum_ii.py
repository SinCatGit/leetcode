from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        https://leetcode.com/problems/combination-sum-ii

        Given a collection of candidate numbers (candidates) and a target number (target),
        find all unique combinations in candidates where the candidate numbers sums to target.

        Each number in candidates may only be used once in the combination.

        Note:

        All numbers (including target) will be positive integers.
        The solution set must not contain duplicate combinations.
        Example 1:

        Input: candidates = [10,1,2,7,6,1,5], target = 8,
        A solution set is:
        [
          [1, 7],
          [1, 2, 5],
          [2, 6],
          [1, 1, 6]
        ]
        Example 2:

        Input: candidates = [2,5,2,1,2], target = 5,
        A solution set is:
        [
          [1,2,2],
          [5]
        ]

        Parameters
        ----------
        candidates: List[int]
        target: int

        Returns
        -------
        List[List[int]]

        Examples
        --------
        >>> sol = Solution()
        >>> sorted(sol.combinationSum2([2, 5, 2, 1, 2], 5)
        [[1, 2, 2], [5]]

        Notes
        -----

        References
        ---------

        """
        self.ans = []
        candidates = sorted(candidates)

        def dfs(remain, t, path):
            if t == 0:
                self.ans.append(path)
                return

            if not remain or remain[0] > t:
                return
            head = remain[0]
            dfs(remain[1:], t-head, path+[head])
            i = 1
            while i < len(remain) and remain[i] == remain[i-1]:
                i += 1
            dfs(remain[i:], t, path)

        dfs(candidates, target, [])
        return self.ans

