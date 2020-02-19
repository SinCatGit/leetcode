from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def treeToDoublyList(self, root: TreeNode) -> TreeNode:
        """
        https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

        Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and
        right pointers as synonymous to the previous and next pointers in a doubly-linked list.

        Let's take the following BST as an example, it may help you understand the problem better:

        We want to transform this BST into a circular doubly linked list. Each node in a doubly linked
        list has a predecessor and successor. For a circular doubly linked list, the predecessor of the
        first element is the last element, and the successor of the last element is the first element.

        The figure below shows the circular doubly linked list for the BST above. The "head" symbol means
        the node it points to is the smallest element of the linked list.

        Specifically, we want to do the transformation in place. After the transformation, the left pointer
        of the tree node should point to its predecessor, and the right pointer should point to its successor.
        We should return the pointer to the first element of the linked list.

        The figure below shows the transformed BST. The solid line indicates the successor relationship, while
        the dashed line means the predecessor relationship.


        Parameters
        ----------
        root: TreeNode

        Returns
        -------
        TreeNode

        Examples
        --------

        References
        ---------
        .. [1] https://www.cnblogs.com/grandyang/p/9615871.html
        .. [2]
        .. [3]

        """
        stack = list()
        head = None
        tail = None
        is_first = False
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if not is_first:
                    is_first = True
                    head = root
                if tail:
                    tail.right = root
                    root.left = tail
                tail = root
                root = root.right
        head.left = tail
        tail.right = head
        return head
















