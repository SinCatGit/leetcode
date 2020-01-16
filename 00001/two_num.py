from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        https://leetcode.com/problems/two-sum/

        Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        >>> solution = Solution()
        >>> solution.twoSum([2, 7, 11, 15], 9)
        [0, 1]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None
        

