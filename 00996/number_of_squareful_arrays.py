from typing import List


class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        """
        https://leetcode.com/problems/number-of-squareful-arrays/

        Given an array A of non-negative integers, the array is squareful
        if for every pair of adjacent elements, their sum is a perfect square.

        Return the number of permutations of A that are squareful.  Two permutations
        A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].

        Example 1:

        Input: [1,17,8]
        Output: 2
        Explanation:
        [1,8,17] and [17,8,1] are the valid permutations.

        Example 2:

        Input: [2,2,2]
        Output: 1

        Note:

        1 <= A.length <= 12
        0 <= A[i] <= 1e9

        Parameters
        ----------
        A: List[int]

        Returns
        -------
        int

        Examples
        --------
        >>> sol = Solution()
        >>> sol.numSquarefulPerms([1, 17, 8])
        2
        >>> sol.numSquarefulPerms([2, 2, 2])
        1

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/number-of-squareful-arrays/discuss/238562/C%2B%2BPython-Backtracking
        .. [2] https://www.hackerearth.com/practice/algorithms/graphs/hamiltonian-path/tutorial/

        """
        from collections import Counter
        self.c = Counter(A)
        self.cond = {i: {j for j in self.c if int((i+j)**0.5)**2 == i+j} for i in self.c}
        self.cnt = 0

        def dfs(x, left=len(A)-1):
            self.c[x] -= 1
            if left == 0:
                self.cnt += 1
            for y in self.cond[x]:
                if self.c[y]:
                    dfs(y, left-1)
            self.c[x] += 1

        for x in self.c:
            dfs(x)
        return self.cnt

