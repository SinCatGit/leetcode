from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        https://leetcode.com/problems/next-permutation

        Implement next permutation, which rearranges numbers into the 
        lexicographically next greater permutation of numbers.

        If such arrangement is not possible, it must rearrange it as the 
        lowest possible order (ie, sorted in ascending order).
        
        The replacement must be in-place and use only constant extra memory.
        
        Here are some examples. Inputs are in the left-hand column and 
        its corresponding outputs are in the right-hand column.
        
        1,2,3 → 1,3,2
        3,2,1 → 1,2,3
        1,1,5 → 1,5,1
        
        Parameters
        ----------
        nums: List[int]

        Returns
        -------
        None

        Examples
        --------
        >>> sol = Solution()
        >>> nums = [5, 4, 3, 6, 4, 3, 2]
        >>> sol.nextPermutation(nums)
        >>> nums
        [5, 4, 4, 2, 3, 3, 6]

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/next-permutation/discuss/14054/Python-solution-with-comments.
        .. [2] https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

        """
        i, j = len(nums)-1, len(nums)-1
        while j > 0 and nums[j-1] >= nums[j]:
            j -= 1
        if j == 0:
            nums.reverse()
            return

        k = j-1
        while nums[i] <= nums[k]:
            i -= 1
        nums[i], nums[k] = nums[k], nums[i]

        l, r = j, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


