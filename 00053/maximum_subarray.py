from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/maximum-subarray/

        Given an integer array nums, find the contiguous subarray (containing at least one number)
        which has the largest sum and return its sum.

        Parameters
        ----------
        nums: List[int]

        Returns
        -------
        int

        Examples
        --------
        >>> solution = Solution()
        >>> solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6

        Notes
        -----

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=2MmGzdiKR9Y
        .. [2] https://www.youtube.com/watch?v=86CQq3pKSUw
        .. [3] https://leetcode.com/problems/maximum-subarray/discuss/20396/Easy-Python-Way

        """
        cur_max, final_max = nums[0], nums[0]
        for num in nums[1:]:
            cur_max = max(num, num + cur_max)
            final_max = max(cur_max, final_max)
        return final_max

    def maxSubArraryV01(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i-1]+nums[i])
        return max(nums)
