from collections import defaultdict
from typing import List


class WordDistance:
    def __init__(self, words: List[str]):
        self.locations = defaultdict(list)
        for i, word in enumerate(words):
            self.locations[word].append(i)

    def shortest(self, word1: str, word2: str):
        """
        https://leetcode.com/problems/shortest-word-distance-ii/
        https://leetcode.com/articles/shortest-word-distance-ii/


        Design a class which receives a list of words in the constructor, and implements a method that takes two words
        word1 and word2 and return the shortest distance between these two words in the list. Your method will be called
        repeatedly many times with different parameters.

        """
        idx1, idx2 = 0, 0
        dis1, dis2 = self.locations[word1], self.locations[word2]
        res = float('inf')
        while idx1 < len(dis1) and idx2 < len(dis2):
            res = min(res, abs(dis1[idx1]-dis2[idx2]))
            if dis1[idx1] < dis2[idx2]:
                idx1 += 1
            else:
                idx2 += 1
        return res

