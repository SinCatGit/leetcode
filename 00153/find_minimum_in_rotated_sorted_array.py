from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

        Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
        (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

        Find the minimum element.

        You may assume no duplicate exists in the array.

        Parameters
        ----------
        nums: List[int]

        Returns
        -------
        int

        Examples
        --------
        >>> sol = Solution()
        >>> sol.findMin([3, 4, 5, 1, 2])
        1
        >>> sol.findMin([4, 5, 6, 7, 0, 1, 2])
        0

        Notes
        -----

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=P4r7mF1Jd50
        .. [2] https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/28202/Neat-JAVA-solution-using-binary-search
        .. [3] https://www.youtube.com/watch?v=eG27FBcmy1k

        """
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]
            mid = left+(right-left)//2
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid


if __name__ == '__main__':
    sol = Solution()
    sol.findMin([3, 1, 2])
