from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/next-greater-element-i/

        You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
        Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

        The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
        If it does not exist, output -1 for this number.

        Parameters
        ----------
        nums1: List[int]
        nums2: List[int]

        Returns
        -------
        List[int]

        Examples
        --------
        >>> sol = Solution()
        >>> sol.nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
        [-1, 3, -1]
        >>> sol.nextGreaterElement([2, 4], [1, 2, 3, 4])
        [3, -1]

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/next-greater-element-i/discuss/97604/Python-Solution-with-O(n)

        """
        res = list()
        stack = list()
        d = dict()
        for n in nums2:
            while stack and stack[-1] < n:
                d[stack.pop()] = n
            stack.append(n)

        for m in nums1:
            res.append(d.get(m, -1))
        return res

    def nextGreaterElementV01(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1]*len(nums1)
        for k, num in enumerate(nums1):
            pos = -1
            for i, n in enumerate(nums2):
                print(i, n)
                if n == num:
                    pos = i
                if pos != -1 and n > num:
                    res[k] = n
                    break
        return res
