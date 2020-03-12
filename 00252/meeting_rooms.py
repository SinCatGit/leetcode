from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms)

        Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...]`
        (si < ei), determine if a person could attend all meetings.

        Example 1:

        ```
        Input: [[0,30],[5,10],[15,20]]
        Output: false
        ```

        Example 2:

        ```
        Input: [[7,10],[2,4]]
        Output: true
        ```

        **NOTE:** input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.


        Parameters
        ----------
        intervals: List[List[int]]

        Returns
        -------
        bool

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1]

        """
        intervals = sorted(intervals, key=lambda i: i[0])
        return all(intervals[i][0] >= intervals[i-1][1] for i in range(1, len(intervals)))

    def canAttendMeetingsV01(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key=lambda i: i[0])
        end = float('-inf')
        for s, e in intervals:
            if s >= end:
                end = e
            else:
                return False
        return True
