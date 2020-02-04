from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

        Say you have an array for which the ith element is the price of a given stock on day i.

        Design an algorithm to find the maximum profit. You may complete as many transactions
        as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

        You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
        After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

        Parameters
        ----------
        prices: List[int]

        Returns
        -------
        int

        Examples
        --------
        >>> solution = Solution()
        >>> solution.maxProfit([1, 2, 3, 0, 2])
        3

        Notes
        -----

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=oL6mRyTn56M
        .. [1] https://www.youtube.com/watch?v=Ggzbo9eVrLU&list=PLTNkreZiUTIL-S_VJBLRxlmGktAQtla-m&index=9&pbjreload=10

        """
        hold, sold, rest = float('-inf'), 0, 0

        for p in prices:
            hold, rest, sold = max(hold, rest-p), max(sold, rest), hold+p

        return max(rest, sold)


