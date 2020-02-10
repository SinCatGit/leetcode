from typing import List


class Solution(object):
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

        Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
        write a function to find the number of connected components in an undirected graph.

        Parameters
        ----------
        n: int
        edges: List[List[int]]

        Returns
        -------
        int

        Examples
        --------
        >>> solution = Solution()
        >>> solution.countComponents(5, [[0, 1], [1, 2], [3, 4]])
        2

        Notes
        -----

        References
        ---------

        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        uf = UnionFind(n)
        for i, j in edges:
            uf.union(i, j)
        return uf.count


class UnionFind:
    def __init__(self, n):
        self.count = n
        self.graph = [i for i in range(n)]

    def find(self, p):
        while p != self.graph[p]:
            self.graph[p] = self.find(self.graph[p])
            p = self.graph[p]
        return p

    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        if pi == pj:
            return
        self.graph[pj] = pi
        self.count -= 1

