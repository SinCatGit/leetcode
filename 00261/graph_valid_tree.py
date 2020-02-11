from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        https://leetcode.com/problems/graph-valid-tree/

        Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
        write a function to check whether these edges make up a valid tree.

        Parameters
        ----------
        n: int
        edges: List[List[int]]

        Returns
        -------
        bool

        Examples
        --------
        >>> sol = Solution()
        >>> sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
        True
        >>> sol.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
        False

        Notes
        -----

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=n_t0a_8H8VY

        """
        uf = UnionFind(n)

        for a, b in edges:
            pa, pb = uf.find(a), uf.find(b)
            if pa == pb:
                return False
            uf.union(pa, pb)

        return len(edges) == n-1


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
            p = self.parent[p]
        return p

    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        if pi == pj:
            return
        self.parent[pj] = pi
