from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

        Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i;
        and a non-negative integer fee representing a transaction fee.

        You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
        You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

        Return the maximum profit you can make.

        Parameters
        ----------
        prices: List[int]
        fee: int


        Returns
        -------
        int

        Examples
        --------
        >>> solution = Solution()
        >>> solution.maxProfit([1, 3, 2, 8, 4, 9], 2)
        8

        Notes
        -----

        References
        ---------

        """
        if not prices:
            return 0
        prices_len = len(prices)
        hold = [0 for _ in range(prices_len)]
        un_hold = [0 for _ in range(prices_len)]
        hold[0] = -prices[0]-fee

        for i in range(1, prices_len):
            hold[i] = max(hold[i-1], un_hold[i-1]-prices[i]-fee)
            un_hold[i] = max(un_hold[i-1], hold[i-1]+prices[i])
        return un_hold[-1]

