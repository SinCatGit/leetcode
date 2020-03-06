

class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        """
        [1067. Digit Count in Range](https://leetcode.com/problems/digit-count-in-range/)

        Given an integer d between 0 and 9, and two positive integers low and high as lower and upper
        bounds, respectively. Return the number of times that d occurs as a digit in all integers between low
        and high, including the bounds low and high.

        **Example 1:**

        ```
        Input: d = 1, low = 1, high = 13
        Output: 6
        Explanation:
        The digit d=1 occurs 6 times in 1,10,11,12,13. Note that the digit d=1 occurs twice in the number 11.
        ```

        **Example 2:**

        ```
        Input: d = 3, low = 100, high = 250
        Output: 35
        Explanation:
        The digit d=3 occurs 35 times in 103,113,123,130,131,...,238,239,243
        ```

        Parameters
        ----------
        d: int
        low: int
        high: int

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
        def count(n, d):
            cnt = 0
            m = 1
            while m <= n:
                if d == 0:
                    if n//m % 10 == 0:
                        cnt += (n//m-1)//10*m
                    else:
                        cnt += n//m//10*m
                else:
                    cnt += (n // m + 9 - d) // 10 * m
                cnt += (n // m % 10 == d) * (n % m + 1)
                m *= 10
            return cnt if d != 0 else cnt+1

        return count(high, d) - count(low-1, d)


