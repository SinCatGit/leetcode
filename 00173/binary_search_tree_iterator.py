from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    """
    https://leetcode.com/problems/binary-search-tree-iterator/

    Implement an iterator over a binary search tree (BST). Your iterator will be
    initialized with the root node of a BST.

    Calling next() will return the next smallest number in the BST.

    Example:

    Input: [7,3,15,null, null, 9, 20]
        7
       / \
      3  15
        /  \
       9   20

    BSTIterator iterator = new BSTIterator(root);
    iterator.next();    // return 3
    iterator.next();    // return 7
    iterator.hasNext(); // return true
    iterator.next();    // return 9
    iterator.hasNext(); // return true
    iterator.next();    // return 15
    iterator.hasNext(); // return true
    iterator.next();    // return 20
    iterator.hasNext(); // return false

    References
    ---------
    .. [1] https://leetcode.com/problems/binary-search-tree-iterator/discuss/52642/Two-Python-solutions-stack-and-generator

    """
    def __init__(self, root: TreeNode):
        self.stack = list()
        self.root = root
        from collections import deque
        self.queue = deque()
        self.in_order()

    def in_order(self):
        while self.root or self.stack:
            if self.root:
                self.stack.append(self.root)
                self.root = self.root.left
            else:
                self.root = self.stack.pop()
                self.queue.append(self.root.val)
                self.root = self.root.right

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.queue.popleft()

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.queue) > 0



