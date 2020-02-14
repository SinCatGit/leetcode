class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def token(self, s):
        i = 0
        sign = 1
        num = 0
        is_acc_num = False
        while i < len(s):
            if s[i] == '(':
                yield s[i], 'left'
                i += 1

            if i < len(s) and s[i] in ')':
                yield s[i], 'right'
                i += 1

            if i < len(s) and s[i] == '-':
                sign = -1
                i += 1

            while i < len(s) and s[i].isalnum():
                is_acc_num = True
                num = num*10 + int(s[i])
                i += 1

            if is_acc_num:
                yield num*sign, 'integer'
                sign = 1
                num = 0
                is_acc_num = False

    def str2tree(self, s: str) -> TreeNode:
        """
        https://leetcode.com/problems/construct-binary-tree-from-string/

        You need to construct a binary tree from a string consisting of parenthesis and integers.

        The whole input represents a binary tree. It contains an integer followed by zero,
        one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis
        contains a child binary tree with the same structure.

        You always start to construct the left child node of the parent first if it exists.

        Parameters
        ----------
        s: str

        Returns
        -------
        TreeNode

        Examples
        --------

        Notes
        -----

        References
        ---------

        """
        stack = list()

        for t, kind in self.token(s):
            if kind == 'left':
                continue
            elif kind == 'right':
                stack.pop()
            elif kind == 'integer':
                node = TreeNode(t)
                if stack:
                    top = stack[-1]
                    if not top.left:
                        top.left = node
                    else:
                        top.right = node
                stack.append(node)

        return stack[0]


if __name__ == '__main__':
    sol = Solution()
    for item in sol.token('-41(21(33)(1))(6(5))'):
        print(item)
