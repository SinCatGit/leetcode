from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        https://leetcode.com/problems/subarray-product-less-than-k/

        Your are given an array of positive integers nums.

        Count and print the number of (contiguous) subarrays where the product of all the elements
        in the subarray is less than k.

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
        >>> solution.numSubarrayProductLessThanK([10, 5, 2, 6], 100)
        8
        >>> solution.numSubarrayProductLessThanK([10, 100, 2, 6], 100)
        4

        Notes
        -----

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=SxtxCSfSGlo

        """
        if k <= 1:
            return 0
        left, right, cnt = 0, 0, 0
        prod = 1
        while right < len(nums):
            prod *= nums[right]
            while prod >= k:
                prod /= nums[left]
                left += 1
            cnt += right - left + 1
            right += 1
        return cnt


