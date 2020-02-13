from typing import List
from collections import defaultdict


class Solution:
    def __init__(self, graph):
        self.graph = graph

    def knows(self, a: int, b: int) -> bool:
        return self.graph[a][b] == 1

    def findCelebrity(self, n: int) -> int:
        """
        https://leetcode.com/problems/find-the-celebrity/

        Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one
        celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she
        does not know any of them.

        Now you want to find out who the celebrity is or verify that there is not one. The only thing you are
        allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B.
        You need to find out the celebrity (or verify there is not one) by asking as few questions as possible
        (in the asymptotic sense).

        You are given a helper function bool knows(a, b)which tells you whether A knows B. Implement a function
        int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's
        label if there is a celebrity in the party. If there is no celebrity, return -1.

        Parameters
        ----------
        n: int

        Returns
        -------
        int

        Examples
        --------
        >>> sol = Solution([[1, 1, 0], [0, 1, 0], [1, 1, 1]])
        >>> sol.findCelebrity()
        1

        Notes
        -----

        References
        ---------
        .. [1] https://www.cnblogs.com/grandyang/p/5310649.html
        .. [2] https://www.youtube.com/watch?v=QDehNYXlCAg

        """
        res = 0
        for i in range(n):
            if self.knows(res, i):
                res = i
        for i in range(0, res):
            if not self.knows(i, res) or self.knows(res, i):
                return -1
        for i in range(res+1, n):
            if not self.knows(i, res):
                return -1
        return res

    def findCelebrityV01(self, n: int) -> int:
        for i in range(n):
            j = 0
            while j < n:
                if i == j:
                    j += 1
                    continue
                if self.knows(i, j) or not self.knows(j, i):
                    break
                j += 1
            if j == n:
                return i
        return -1


if __name__ == '__main__':
    sol = Solution([[1, 1, 0], [0, 1, 0], [1, 1, 1]])
    print(sol.findCelebrity(3))

