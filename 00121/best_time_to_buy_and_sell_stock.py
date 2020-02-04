from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

        Say you have an array for which the ith element is the price of a given stock on day i.

        If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
        design an algorithm to find the maximum profit.

        Note that you cannot sell a stock before you buy one.

        Parameters
        ----------
        prices: List[int]

        Returns
        -------
        int

        Examples
        --------
        >>> solution = Solution()
        >>> solution.maxProfit([7, 1, 5, 3, 6, 4])
        5
        >>> solution.maxProfit([7, 6, 4, 3, 1])
        0

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
        .. [2] https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-%3A)-(In-case-if-interviewer-twists-the-input)

        """
        cur_max, final_max = 0, 0
        for i in range(1, len(prices)):
            cur_max = max(0, cur_max +prices[i ] -prices[ i -1])
            final_max = max(cur_max, final_max)
        return final_max


