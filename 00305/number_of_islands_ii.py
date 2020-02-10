class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    def numIslands2(self, n, m, operators):
        """
        https://leetcode.com/problems/number-of-islands-ii/

        Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k).
        Originally, the 2D matrix is all 0 which means there is only sea in the matrix.
        The list pair has k operator and each operator has two integer A[i].x, A[i].y means
        that you can change the grid matrix[A[i].x][A[i].y] from sea to island. Return how many island are there
        in the matrix after each operator.

        Parameters
        ----------
        n: int
        m: int
        operators: List[List[int]]

        Returns
        -------
        List

        Examples
        --------

        Notes
        -----

        References
        ---------

        """
        res = list()
        islands = list()
        operators = [(p.x, p.y) for p in operators if 0 <= p.x < n and 0 <= p.y < m]
        delta_xy = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for x, y in operators:
            union_land = [(x, y)]
            solo_lands = list()
            for island in islands:
                if (x, y) in island:
                    union_land = list()
                elif any([(x+dx, y+dy) in island for dx, dy in delta_xy]):
                    union_land += island
                else:
                    solo_lands.append(island)
            islands = solo_lands
            islands += union_land,
            res.append(len(islands))
        return res

    def numIslands2V01(self, n, m, operators):
        res = list()
        operators = [(p.x, p.y) for p in operators if 0 <= p.x < n and 0 <= p.y < m]
        delta_xy = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        uf = UnionFind(n, m)
        for x, y in operators:
            p = x*m+y
            if uf.find(p) != -1:
                res.append(uf.count)
                continue
            uf.set_value(p)
            for dx, dy in delta_xy:
                _x, _y = dx + x, dy + y
                if 0 <= _x < n and 0 <= _y < m and uf.find(_x*m+_y) != -1:
                    uf.union(p, _x*m+_y)
            res.append(uf.count)
        return res


class UnionFind:
    def __init__(self, n, m):
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)

    def find(self, p):
        if self.parent[p] == -1:
            return -1
        while p != self.parent[p]:
            p = self.find(self.parent[p])
            self.parent[p] = p
        return p

    def set_value(self, p):
        self.parent[p] = p
        self.count += 1

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return

        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[px] = py
            self.rank[py] += 1
        self.count -= 1
