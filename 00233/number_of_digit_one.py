

class Solution:
    def countDigitOne(self, n: int) -> int:
        """
        [233. Number of Digit One](https://leetcode.com/problems/number-of-digit-one/)

        Given an integer n, count the total number of digit 1 appearing in all non-negative integers
        less than or equal to n.

        **Example:**

        ```
        Input: 13
        Output: 6
        Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
        ```

        Parameters
        ----------
        n: int

        Returns
        -------
        int

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/number-of-digit-one/discuss/64381/4%2B-lines-O(log-n)-C%2B%2BJavaPython

        """
        ones = 0
        d = 1
        m = 1
        while m <= n:
            ones += (n//m + 9-d)//10*m+(n//m % 10 == d)*(n % m+1)
            m *= 10
        return ones


