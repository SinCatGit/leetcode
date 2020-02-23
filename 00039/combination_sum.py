from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        https://leetcode.com/problems/combination-sum

        Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

        The same repeated number may be chosen from candidates unlimited number of times.

        Note:

            All numbers (including target) will be positive integers.
            The solution set must not contain duplicate combinations.
        Example 1:

            Input: candidates = [2,3,6,7], target = 7,
            A solution set is:
            [
              [7],
              [2,2,3]
            ]
        Example 2:

            Input: candidates = [2,3,5], target = 8,
            A solution set is:
            [
              [2,2,2,2],
              [2,3,3],
              [3,5]
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
        >>> sorted(sol.combinationSum([2, 3, 6, 7], 7))
        [[2, 2, 3], [7]]

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/combination-sum/discuss/237525/Python-simple-Bactracking-solution-beats-99

        """
        if target == 0:
            return [[]]
        if len(candidates) <= 0:
            return []
        candidates.sort()
        res = list()
        head = candidates[0]
        if head > target:
            return []
        max_count = target // head

        for i in range(max_count + 1):
            res += [[head] * i + item for item in self.combinationSum(candidates[1:], target - i * head)]

        return res

    def combinationSumV01(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        candidates = sorted(candidates)

        def dfs(remain, t, path):
            if t == 0:
                self.ans.append(path)

            for i, num in enumerate(remain):
                if num > t:
                    break
                dfs(remain[i:], t-num, path+[num])

        dfs(candidates, target, [])
        return self.ans





if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum([7], 7))
    print(sol.combinationSum([2, 3, 6, 7], 7))
