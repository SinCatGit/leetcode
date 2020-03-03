from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        """
        [259. 3Sum Smaller](https://leetcode.com/problems/3sum-smaller)

        Given an array of n integers nums and a target, find the number of index
        triplets i, j, k with 0 <= i < j < k < n that satisfy the condition
        nums[i] + nums[j] + nums[k] < target.

        ```
        For example, given nums = [-2, 0, 1, 3], and target = 2.

        Return 2. Because there are two triplets which sums are less than 2:

        [-2, 0, 1]
        [-2, 0, 3]
        ```

        **Follow up:**

        Could you solve it in O(n2) runtime?

        """
        nums.sort()
        count = 0
        nums_len = len(nums)
        for i, v in enumerate(nums):
            l, r = i+1, nums_len-1
            while l < r:
                if v + nums[l] + nums[r] < target:
                    count += r - l
                    l += 1
                else:
                    r -= 1
        return count
