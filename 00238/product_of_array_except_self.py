from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

        Given an array nums of n integers where n > 1,  return an array output such that output[i]
        is equal to the product of all the elements of nums except nums[i].

        **Example:**
        ```
        Input:  [1,2,3,4]
        Output: [24,12,8,6]
        ```

        **Note:** Please solve it without division and in O(n).

        **Follow up:**

        Could you solve it with constant space complexity? (The output array does not count as
        extra space for the purpose of space complexity analysis.)

        """
        nums_len = len(nums)
        res = [1]*nums_len
        p = 1
        for i in range(nums_len):
            res[i] = p
            p *= nums[i]
        p = 1
        for i in range(nums_len)[::-1]:
            res[i] *= p
            p *= nums[i]

        return res

