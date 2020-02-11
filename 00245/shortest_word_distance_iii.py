from typing import List


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        """
        https://leetcode.com/problems/shortest-word-distance-iii

        This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.
        Given a list of words and two words word1 and word2, return the shortest distance between these
        two words in the list.

        word1 and word2 may be the same and they represent two individual words in the list.

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
        >>> sol.shortestDistance(['practice', 'makes', 'perfect', 'coding', 'makes'], 'makes', 'makes')
        3

        Notes
        -----

        References
        ---------

        """
        idx = -1
        res = float('inf')
        for i, word in enumerate(words):
            if word in [word1, word2]:
                if idx != -1:
                    if word != words[idx]:
                        res = min(res, abs(i-idx))
                    elif word1 == word2:
                        res = min(res, abs(i-idx))
                idx = i
        return res
