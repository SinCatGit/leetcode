from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        https://leetcode.com/problems/insert-interval/

        Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

        You may assume that the intervals were initially sorted according to their start times.

        Example 1:

        Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
        Output: [[1,5],[6,9]]
        Example 2:

        Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
        Output: [[1,2],[3,10],[12,16]]
        Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
        NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

        Parameters
        ----------
        intervals: List[List[int]]
        newInterval: List[int]

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
        intervals = sorted(intervals+[newInterval])
        while intervals:
            pair = intervals.pop(0)
            if res and res[-1][0] <= pair[0] <= res[-1][1]:
                if res[-1][1] < pair[1]:
                    res[-1][1] = pair[1]
            else:
                res += pair,
        return res

    def insertV01(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = [], []
        start, end = newInterval
        for item in intervals:
            if item[1] < start:
                l += item,
            elif item[0] > end:
                r += item,
            else:
                start = min(start, item[0])
                end = max(end, item[1])

        return l + [[start, end]] + r



