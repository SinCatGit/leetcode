from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        https://leetcode.com/problems/contains-duplicate/

        Given an array of integers, find if the array contains any duplicates.

        Your function should return true if any value appears at least twice 
        in the array, and it should return false if every element is distinct.


        Parameters
        ----------
        nums: List[int]

        Returns
        -------
        bool

        Examples
        --------
        >>> sol = Solution()
        >>> sol.containsDuplicate([1, 2, 3, 1])
        True
        >>> sol.containsDuplicate([1, 2, 3])
        False

        Notes
        -----

        References
        ---------

        """
        return len(nums) > len(set(nums))



