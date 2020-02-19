from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        """
        https://leetcode.com/problems/lexicographically_smallest_equivalent_string/

        Given strings A and B of the same length, we say A[i] and B[i] are equivalent characters. For example, if A = “abc” and B = “cde”, then we have ‘a’ = 'c', 'b' = ‘d’, ‘c’ == ‘e’.

        Equivalent characters follow the usual rules of any equivalence relation:

        Reflexivity: ‘a’ = 'a'
        Symmetry: 'a' = ‘b’ implies ‘b’ = 'a'
        Transitivity: 'a' = ‘b’ and ‘b’ = 'c' implies 'a' = ‘c’
        For example, given the equivalency information from A and B above, S = “eed”, “acd”, and “aab” are equivalent strings, and “aab” is the lexicographically smallest equivalent string of S.

        Return the lexicographically smallest equivalent string of S by using the equivalency information from A and B.

        Example 1:

        Input: A = "parker", B = "morris", S = "parser"
        Output: "makkek"
        Explanation: Based on the equivalency information in A and B, we can group their characters as [m,p], [a,o], [k,r,s], [e,i]. The characters in each group are equivalent and sorted in lexicographical order. So the answer is "makkek".
        Example 2:

        Input: A = "hello", B = "world", S = "hold"
        Output: "hdld"
        Explanation:  Based on the equivalency information in A and B, we can group their characters as [h,w], [d,e,o], [l,r]. So only the second letter 'o' in S is changed to 'd', the answer is "hdld".
        Example 3:

        Input: A = "leetcode", B = "programs", S = "sourcecode"
        Output: "aauaaaaada"
        Explanation:  We group the equivalent characters in A and B as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in S except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".
        Note:

        String A, B and S consist of only lowercase English letters from ‘a’ – ‘z’.
        The lengths of string A, B and S are between 1 and 1000.
        String A and B are of the same length.

        Parameters
        ----------
        A: str
        B: str
        S: str

        Returns
        -------
        str

        Examples
        --------

        References
        ---------
        .. [1] https://code.dennyzhang.com/lexicographically-smallest-equivalent-string
        .. [2] https://www.cnblogs.com/Dylan-Java-NYC/p/11297136.html
        .. [3] https://leetcode.com/problems/lexicographically-smallest-equivalent-string/discuss/412777/python-bfsdfsunion-find-complexity-analysis
        .. [4] https://leetcode.com/problems/lexicographically-smallest-equivalent-string/discuss/316905/python-union-find

        """
        uf = UnionFind()
        # for i in range(len(A)):
        #     uf.union(ord(A[i])-ord('a'), ord(B[i])-ord('a'))
        for a, b in zip(A, B):
            uf.union(ord(a)-ord('a'), ord(b)-ord('a'))
        res = ''
        for c in S:
            res += chr(uf.find(ord(c)-ord('a'))+ord('a'))
        return res


class UnionFind:
    def __init__(self):
        self.data = [i for i in range(26)]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return
        if pa < pb:
            self.data[pb] = pa
        else:
            self.data[pa] = pb

    def find(self, i):
        if i != self.data[i]:
            self.data[i] = self.find(self.data[i])
        return self.data[i]












