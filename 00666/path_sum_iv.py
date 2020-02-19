from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/path-sum-iv/

        If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.

        For each integer in this list:

        The hundreds digit represents the depth D of this node, 1 <= D <= 4.
        The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is
        the same as that in a full binary tree.

        The units digit represents the value V of this node, 0 <= V <= 9.


        Given a list of ascending three-digits integers representing a binary with the depth smaller than 5. You need
        to return the sum of all paths from the root towards the leaves.

        Example 1:

        Input: [113, 215, 221]
        Output: 12
        Explanation:
        The tree that the list represents is:
            3
           / \
          5   1

        The path sum is (3 + 5) + (3 + 1) = 12.


        Example 2:

        Input: [113, 221]
        Output: 4
        Explanation:
        The tree that the list represents is:
            3
             \
              1

        The path sum is (3 + 1) = 4.


        Parameters
        ----------
        nums: List[int]

        Returns
        -------
        int

        Examples
        --------

        References
        ---------
        .. [1] https://leetcode.com/articles/path-sum-iv/
        .. [2] https://www.cnblogs.com/grandyang/p/7570954.html
        .. [3] https://leetcode.com/problems/path-sum-iv/discuss/106934/Python-Straight-Forward-Solution

        """
        nums_len = len(nums)
        prefix_sum = [0 for _ in range(nums_len)]
        prefix_sum[0] = nums[0] % 10
        s = 0

        for i in range(0, nums_len):
            level = (nums[i] // 100 + 1) * 10
            cnt = (nums[i] // 10) % 10
            prefix = [level + 2 * cnt - 1, level + 2 * cnt]

            has_children = False
            for j in range(i + 1, nums_len):
                if nums[j] // 10 in prefix:
                    prefix_sum[j] += prefix_sum[i] + nums[j] % 10
                    has_children = True
            if not has_children:
                s += prefix_sum[i]

        return s














