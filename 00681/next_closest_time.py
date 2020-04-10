

class Solution:
    def nextClosestTime(self, time: str) -> str:
        """
        #### [681. Next Closest Time](https://leetcode.com/problems/next-closest-time)

        Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

        You may assume the given input string is always valid. For example,  "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

        **Example 1:**

        ```
        Input: "19:34"
        Output: "19:39"
        Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
        ```

        **Example 2:**

        ```
        Input: "23:59"
        Output: "22:22"
        Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
        ```

        Parameters
        ----------
        time: str

        Returns
        -------
        str

        Examples
        --------
        >>> sol = Solution()
        >>> sol.nextClosestTime('19:34')
        '19:39'
        >>> sol.nextClosestTime('23:59')
        '22:22'

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/next-closest-time/discuss/190816/Python-simple-20ms-solution
        .. [2] https://leetcode.com/problems/next-closest-time/discuss/107776/Python

        """
        hours, minutes = time.split(":")
        digits = sorted(set(hours+minutes))
        two_digits = [a+b for a in digits for b in digits]
        i = two_digits.index(minutes)
        two_len = len(two_digits)
        if i + 1 < two_len and two_digits[i+1] < '60':
            return f'{hours}:{two_digits[i+1]}'

        i = two_digits.index(hours)
        if i + 1 < two_len and two_digits[i+1] < '24':
            return f'{two_digits[i+1]}:{two_digits[0]}'

        return f'{two_digits[0]}:{two_digits[0]}'

