

class Solution:
    def numWays(self, n: int, k: int) -> int:
        """
        [276. Paint Fence](https://leetcode.com/problems/paint-fence)

        There is a fence with n posts, each post can be painted with one of the k colors.

        You have to paint all the posts such that no more than two adjacent fence posts have the same color.

        Return the total number of ways you can paint the fence.

        **Note:**
        n and k are non-negative integers.

        Parameters
        ----------
        n: int
        k: int

        Returns
        -------
        int

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/paint-fence/discuss/71151/Lucas-formula-maybe-%22O(1)%22-and-34-liners
        .. [2] https://www.cnblogs.com/grandyang/p/5231220.html
        .. [3] https://baihuqian.github.io/2018-07-29-paint-fence/

        """
        if n == 0:
            return 0
        if n == 1:
            return k
        same, diff = 0, k
        for i in range(2, n+1):
            same, diff = diff, (same+diff)*(k-1)
        return same+diff

