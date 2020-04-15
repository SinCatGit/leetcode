from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        """
        #### [545. Boundary of Binary Tree](https://leetcode.com/problems/boundary-of-binary-tree/)

        Given a binary tree, return the values of its boundary in **anti-clockwise** direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate **nodes**. (The values of the nodes may still be duplicates.)

        **Left boundary** is defined as the path from root to the **left-most** node. **Right boundary** is defined as the path from root to the **right-most** node. If the root doesn't have left subtree or right subtree, then the  root itself is left boundary or right boundary. Note this definition  only applies to the input binary tree, and not applies to any subtrees.

        The **left-most** node is defined as a **leaf** node you could  reach when you always firstly travel to the left subtree if exists. If  not, travel to the right subtree. Repeat until you reach a leaf node.

        The **right-most** node is also defined by the same way with left and right exchanged.

        **Example 1**

        ```
        Input:
          1
           \
            2
           / \
          3   4

        Ouput:
        [1, 3, 4, 2]

        Explanation:
        The root doesn't have left subtree, so the root itself is left boundary.
        The leaves are node 3 and 4.
        The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
        So order them in anti-clockwise without duplicates and we have [1,3,4,2].
        ```

        **Example 2**

        ```
        Input:
            ____1_____
           /          \
          2            3
         / |         |
        4   5        6
           / |      / |
          7   8    9  10

        Ouput:
        [1,2,4,7,8,9,10,6,3]

        Explanation:
        The left boundary are node 1,2,4. (4 is the left-most node according to definition)
        The leaves are node 4,7,8,9,10.
        The right boundary are node 1,3,6,10. (10 is the right-most node).
        So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].
        ```


        Parameters
        ----------
        root: TreeNode

        Returns
        -------
        List[int]

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/boundary-of-binary-tree/discuss/101307/Python-solution-recursive-dfs-~20-lines.

        """

        if not root: return []
        if not root.left and not root.right: return [root.val]

        left_edges, right_edges = [], []
        left, right = root.left, root.right

        while left:
            left_edges.append(left)
            left = left.left or left.right

        while right:
            right_edges.append(right)
            right = right.right or right.left

        stack, leafs = [], []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if not node.left and not node.right:
                    leafs.append(node)
                node = node.right
        if left_edges and left_edges[-1] is leafs[0]:
            left_edges = left_edges[:-1]
        if right_edges and right_edges[-1] is leafs[-1]:
            right_edges = right_edges[:-1]

        return [root.val] + [node.val for node in left_edges+leafs+right_edges[::-1]]

    def boundaryOfBinaryTreeV01(self, root):
        # The main idea is to carry the flag isleft and isight
        # in the dfs steps to help decide when to add node
        # values to the boundary array.
        if not root: return []
        boundary = [root.val]

        def dfs(root, isleft, isright):
            if root:
                # append when going down from the left or at leaf node
                if (not root.left and not root.right) or isleft:
                    boundary.append(root.val)

                if root.left and root.right:
                    dfs(root.left, isleft, False)
                    dfs(root.right, False, isright)
                else:
                    dfs(root.left, isleft, isright)
                    dfs(root.right, isleft, isright)

                # append to boundary when coming up from the right
                if (root.left or root.right) and isright:
                    boundary.append(root.val)

        dfs(root.left, True, False)
        dfs(root.right, False, True)
        return boundary
