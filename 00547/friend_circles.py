from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/friend-circles/

        There are N students in a class. Some of them are friends, while some are not.
        Their friendship is transitive in nature. For example, if A is a direct friend of B,
        and B is a direct friend of C, then A is an indirect friend of C. And we defined
        a friend circle is a group of students who are direct or indirect friends.

        Given a N*N matrix M representing the friend relationship between students in the class.
        If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.
        And you have to output the total number of friend circles among all the students.

        Parameters
        ----------
        M: List[List[int]]

        Returns
        -------
        int

        Examples
        --------

        Notes
        -----

        References
        ---------

        """
        if not M or not M[0]:
            return 0
        n = len(M)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j] == 1:
                    uf.union(i, j)
        return uf.count


class UnionFind:
    def __init__(self, n):
        self.count = n
        self.circles = [i for i in range(n)]

    def find(self, p):
        while p != self.circles[p]:
            self.circles[p] = self.find(self.circles[p])
            p = self.circles[p]
        return p

    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        if pi == pj:
            return
        self.circles[pj] = pi
        self.count -= 1
