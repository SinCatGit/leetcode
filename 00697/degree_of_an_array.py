from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/degree-of-an-array/

        Given a non-empty array of non-negative integers nums, the degree of this array is
        defined as the maximum frequency of any one of its elements.

        Your task is to find the smallest possible length of a (contiguous) subarray of nums,
        that has the same degree as nums.

        Parameters
        ----------
        nums: List[int]

        Returns
        -------
        int

        Examples
        --------
        >>> solution = Solution()
        >>> solution.findShortestSubArray([1, 2, 2, 3, 1, 4, 2])
        6

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/degree-of-an-array/discuss/124317/JavaC%2B%2BPython-One-Pass-Solution
        .. [2] https://leetcode.com/problems/degree-of-an-array/discuss/108666/Python-easy-and-concise-solution

        """
        from collections import defaultdict
        counts = defaultdict(list)
        for i in range(len(nums)):
            counts[nums[i]].append(i)
        return min((-len(l), l[-1]-l[0]+1) for l in counts.values())[1]

    def findShortestSubArrayV01(self, nums: List[int]) -> int:
        first, frequency, degree = {}, {}, 0
        res = len(nums)
        for i, v in enumerate(nums):
            first.setdefault(v, i)
            frequency[v] = frequency.get(v, 0) + 1
            if frequency[v] > degree:
                degree = frequency[v]
                res = i-first[v]+1
            elif frequency[v] == degree:
                res = min(res, i-first[v]+1)
        return res

