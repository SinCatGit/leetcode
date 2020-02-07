from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        https://leetcode.com/problems/subarray-sum-equals-k/

        Given an array of integers and an integer k, you need to find the total number of continuous subarrays
        whose sum equals to k.

        Parameters
        ----------
        nums: List[int]
        k: int

        Returns
        -------
        int

        Examples
        --------
        >>> solution = Solution()
        >>> solution.subarraySum([1, 1, 1], 2)
        2
        >>> solution.subarraySum([1, 2, 1, -3, 6, 1, 2], 4)
        3
        >>> solution.subarraySum([1, 1, -1, 1], 1)
        5

        Notes
        -----

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=aYfwus5T3Bs

        """
        prefix_sum = 0
        sub_hash = {0: 1}

        cnt = 0
        for n in nums:
            prefix_sum += n
            cnt += sub_hash.get(prefix_sum-k, 0)
            sub_hash[prefix_sum] = sub_hash.get(prefix_sum, 0) + 1

        return cnt

    def subarraySumV01(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total == k:
                    cnt += 1
        return cnt
