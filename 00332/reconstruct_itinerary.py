from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        https://leetcode.com/problems/reconstruct-itinerary/

        Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
        reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK.
        Thus, the itinerary must begin with JFK.

        If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical
        order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order
        than ["JFK", "LGB"].

        All airports are represented by three capital letters (IATA code).
        You may assume all tickets form at least one valid itinerary.

        Parameters
        ----------
        tickets: List[List[str]]

        Returns
        -------
        List[str]

        Examples
        --------
        >>> solution = Solution()
        >>> solution.findItinerary([['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']])
        ['JFK', 'MUC', 'LHR', 'SFO', 'SJC']
        >>> solution.findItinerary([['JFK','SFO'],['JFK','ATL'],['SFO','ATL'],['ATL','JFK'],['ATL','SFO']])
        ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']
        >>> solution.findItinerary([['JFK','KUL'],['JFK','NRT'],['NRT','JFK']])
        ['JFK', 'NRT', 'JFK', 'KUL']

        References
        ---------
        .. [1] https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C%2B%2B
        .. [2] https://www.youtube.com/watch?v=LKSdX31pXjY&list=PLTNkreZiUTIL-S_VJBLRxlmGktAQtla-m&index=7
        .. [3] https://www.youtube.com/watch?v=4udFSOWQpdg
        .. [4] https://www.youtube.com/watch?v=9mRDfF4eyO0

        """
        from collections import defaultdict
        res = list()
        dest = defaultdict(list)
        for k, v in sorted(tickets)[::-1]:
            dest[k] += v,

        def dfs(airport):
            while dest[airport]:
                dfs(dest[airport].pop())
            res.append(airport)

        dfs('JFK')

        return res[::-1]

    def findItineraryV01(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        res = list()
        dest = defaultdict(list)
        for k, v in sorted(tickets)[::-1]:
            dest[k] += v,
        stack = ['JFK']

        while stack:
            while dest[stack[-1]]:
                stack.append(dest[stack[-1]].pop())
            res.append(stack.pop())

        return res[::-1]


