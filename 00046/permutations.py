from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        https://leetcode.com/problems/permutations

        Given a collection of distinct integers, return all possible permutations.

        Example:
        
        Input: [1,2,3]
        Output:
        [
          [1,2,3],
          [1,3,2],
          [2,1,3],
          [2,3,1],
          [3,1,2],
          [3,2,1]
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
        >>> sorted(sol.permute([1, 2, 3]))
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/permutations/discuss/18296/Simple-Python-solution-(DFS).
        .. [2] https://leetcode.com/problems/permutations/discuss/18241/One-Liners-in-Python

        """
        if not nums:
            return [[]]
        res = []
        for i, n in enumerate(nums):
            res += [[n]+item for item in self.permute(nums[:i]+nums[i+1:])]
        return res

    def permuteV01(self, nums: List[int]):
        from itertools import permutations
        return [list(item) for item in permutations(nums)]

