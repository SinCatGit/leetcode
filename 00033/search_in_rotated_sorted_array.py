from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        https://leetcode.com/problems/search-in-rotated-sorted-array/

        Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
        (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

        You are given a target value to search. If found in the array return its index, otherwise return -1.

        You may assume no duplicate exists in the array.

        Your algorithm's runtime complexity must be in the order of O(log n).

        Parameters
        ----------
        nums: List[str]
        target: int

        Returns
        -------
        int

        Examples
        --------
        >>> sol = Solution()
        >>> sol.search([4, 5, 6, 7, 0, 1, 2], 0)
        4
        >>> sol.search([4, 5, 6, 7, 0, 1, 2], 3)
        -1

        Notes
        -----

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=7SC0hWGeyBo
        .. [1] https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14436/Revised-Binary-Search

        """
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

