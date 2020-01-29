from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        https://leetcode.com/problems/top-k-frequent-words/

        Given a non-empty list of words, return the k most frequent elements.

        Your answer should be sorted by frequency from highest to lowest.
        If two words have the same frequency, then the word with the lower alphabetical order comes first.

        Parameters
        ----------
        words: List[str]
        k: int

        Returns
        -------
        List[str]

        Examples
        --------
        >>> solution = Solution()
        >>> solution.topKFrequent(['i', 'love', 'leetcode', 'i', 'love', 'coding'], 2)
        ['i', 'love']
        >>> solution.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)
        ["the", "is", "sunny", "day"]

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=0MTNMM7KSRM&list=PLTNkreZiUTIL-S_VJBLRxlmGktAQtla-m&index=6

        """
        from collections import Counter
        count = Counter(words)
        items = list(count.items())
        items.sort(key=lambda item: (-item[1], item[0]))
        return [item[0] for item in items[:k]]
