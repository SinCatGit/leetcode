from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        https://leetcode.com/problems/contains-duplicate-ii/

        Given an array of integers and an integer k, find out whether there are 
        two distinct indices i and j in the array such that nums[i] = nums[j] 
        and the absolute difference between i and j is at most k.

        Parameters
        ----------
        nums: List[int]
        k: int

        Returns
        -------
        bool

        Examples
        --------
        >>> sol = Solution()
        >>> sol.containsNearbyDuplicate([1, 2, 3, 1], 3)
        True
        >>> sol.containsNearbyDuplicate([1, 0, 1, 1], 1)
        True
        >>> sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
        False

        Notes
        -----

        References
        ---------

        """
        d = {}
        for i, n in enumerate(nums):
            if n in d and (i - d[n]) <= k:
                return True
            d[n] = i
        return False

    def containsNearbyDuplicateV01(self, nums: List[int], k: int) -> bool:
        nums_len = len(nums)
        for i in range(nums_len):
            j = i + 1
            while j < nums_len and j-i <= k:
                if nums[j] == nums[i]:
                    return True
                j += 1
        return False



