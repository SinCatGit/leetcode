from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        https://leetcode.com/problems/sort-colors/

        Given an array with n objects colored red, white or blue,
        sort them in-place so that objects of the same color are adjacent,
        with the colors in the order red, white and blue.

        Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

        Note: You are not suppose to use the library's sort function for this problem.

        Parameters
        ----------
        nums: List[int]

        Returns
        -------
        None

        Examples
        --------
        >>> solution = Solution()
        >>> solution.sortColors([2,0,2,1,1,0])

        Notes
        -----

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=yTwW8WiGrKw&list=PLTNkreZiUTIL-S_VJBLRxlmGktAQtla-m&index=3
        .. [2] https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation
        .. [2] https://www.youtube.com/watch?v=7zuGmKfUt7s
        """
        i, j, k = 0, 0, len(nums)-1
        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1


