from typing import List


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        """

        Given a list of words and two words word1 and word2, return the shortest distance
        between these two words in the list.

        Parameters
        ----------
        words: List[str]
        word1: str
        word2: str

        Returns
        -------
        int

        Examples
        --------
        >>> sol = Solution()
        >>> sol.shortestDistance(['practice', 'makes', 'perfect', 'coding', 'makes'], 'coding', 'practice')
        3
        >>> sol.shortestDistance(['practice', 'makes', 'perfect', 'coding', 'makes'], 'makes', 'coding')
        1

        Notes
        -----

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=n_t0a_8H8VY
        """
        idx = -1
        res = float('inf')
        for i, word in enumerate(words):
            if word in [word1, word2]:
                if idx != -1 and word != words[idx]:
                    res = min(res, abs(i-idx))
                idx = i
        return res

    def shortestDistanceV01(self, words, word1, word2):
        dis1, dis2 = -1, -1
        res = float('inf')
        for i, word in enumerate(words):
            if word == word1:
                dis1 = i

            if word == word2:
                dis2 = i

            if dis1 != -1 and dis2 != -1:
                res = min(res, abs(dis2-dis1))

        return res
