from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        https://leetcode.com/problems/permutations-ii

        Given a collection of numbers that might contain duplicates, return all possible unique permutations.

        Example:

        Input: [1,1,2]
        Output:
        [
          [1,1,2],
          [1,2,1],
          [2,1,1]
        ]

        Parameters
        ----------
        nums: List[int]

        Returns
        -------
        List[List[int]]

        Examples
        --------
        >>> sol = Solution()
        >>> sorted(sol.permuteUnique([1, 1, 2]))
        [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/permutations-ii/discuss/18602/9-line-python-solution-with-1-line-to-handle-duplication-beat-99-of-others-%3A-)
        .. [2] https://leetcode.com/problems/permutations-ii/discuss/18616/6-lines-Python-Ruby

        """
        ans = [[]]
        for n in nums:
            ans = [l[:i]+[n]+l[i:] for l in ans for i in range((l+[n]).index(n)+1)]
        return ans

    def permuteUniqueV01(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.nums_len = len(nums)

        def dfs(path, counter):
            if self.nums_len == len(path):
                self.ans.append(path)
            for k in counter:
                if counter[k] > 0:
                    counter[k] -= 1
                    dfs(path+[k], counter)
                    counter[k] += 1

        from collections import Counter
        dfs([], Counter(nums))
        return self.ans

