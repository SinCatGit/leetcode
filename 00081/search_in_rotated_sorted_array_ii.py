from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

        Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
        (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

        You are given a target value to search. If found in the array return true, otherwise return false.

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
        >>> sol.search([2, 5, 6, 0, 0, 1, 2], 0)
        True
        >>> sol.search([2, 5, 6, 0, 0, 1, 2], 3)
        False

        Notes
        -----

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=lWEIIFFflQY
        .. [2] https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/28202/Neat-JAVA-solution-using-binary-search
        .. [3] https://www.youtube.com/watch?v=eG27FBcmy1k

        """
        if not nums:
            return False
        left, right = 0, len(nums)-1
        while left <= right:
            while left < right and nums[left] == nums[right]:
                left += 1

            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True

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

        return False
