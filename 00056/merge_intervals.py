from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        https://leetcode.com/problems/merge-intervals/

        Given a collection of intervals, merge all overlapping intervals.

        Example 1:

        Input: [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
        Example 2:

        Input: [[1,4],[4,5]]
        Output: [[1,5]]
        Explanation: Intervals [1,4] and [4,5] are considered overlapping.
        NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

        Parameters
        ----------
        intervals: List[List[int]]

        Returns
        -------
        List[List[int]]

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1]
        .. [2]
        .. [3]

        """
        res = []
        intervals = sorted(intervals)
        while intervals:
            pair = intervals.pop(0)
            if res and res[-1][0] <= pair[0] <= res[-1][1]:
                if res[-1][1] < pair[1]:
                    res[-1][1] = pair[1]
            else:
                res += pair,
        return res

    def mergeV01(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        for item in sorted(intervals):
            start, end = item
            if not res or start > res[-1][1]:
                res += item,
            else:
                res[-1][1] = max(res[-1][1], end)
        return res
