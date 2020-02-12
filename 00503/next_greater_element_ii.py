from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/next-greater-element-ii/

        Given a circular array (the next element of the last element is 
        the first element of the array), print the Next Greater Number 
        for every element. The Next Greater Number of a number x is the 
        first greater number to its traversing-order next in the array, 
        which means you could search circularly to find its next greater 
        number. If it doesn't exist, output -1 for this number.

        Parameters
        ----------
        nums: List[int]

        Returns
        -------
        List[int]

        Examples
        --------
        >>> sol = Solution()
        >>> sol.nextGreaterElements([1, 3, 4, 2])
        [3, 4, -1, 3]

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/next-greater-element-ii/discuss/98270/JavaC%2B%2BPython-Loop-Twice
        .. [2] https://www.youtube.com/watch?v=5IAq5jd8O7Y

        """
        res = [-1]*len(nums)
        stack = list()
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                res[stack.pop()] = n
            stack.append(i)

        for n in nums:
            while stack and nums[stack[-1]] < n:
                res[stack.pop()] = n

        return res

