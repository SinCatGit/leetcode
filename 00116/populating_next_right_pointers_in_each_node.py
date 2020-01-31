

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

        You are given a perfect binary tree where all leaves are on the same level,
        and every parent has two children. The binary tree has the following definition:

        struct Node {
          int val;
          Node *left;
          Node *right;
          Node *next;
        }

        Populate each next pointer to point to its next right node. If there is no next right node,
        the next pointer should be set to NULL.

        Initially, all next pointers are set to NULL.

        Follow up:
        You may only use constant extra space.
        Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
        """
        res = root
        while root and root.left:
            next_root = root.left
            while root:
                root.left.next = root.right
                if root.next and root.next.left:
                    root.right.next = root.next.left
                root = root.next
            root = next_root

        return res

    def connectV03(self, root):
        if not root or not root.left:
            return root
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root

    def connectV01(self, root):
        from collections import deque

        q = deque()
        q.append(root)
        q.append(None)
        while root and q:
            node = q.popleft()
            if node:
                node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                if len(q) > 0:
                    q.append(None)

        return root

    def connectV02(self, root):
        from collections import deque

        q = deque()
        q.append(root)
        level_len = 1
        while q:
            i = 0
            pre = None
            while i < level_len:
                node = q.popleft()
                if pre:
                    pre.next = node
                pre = node

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                i += 1
            level_len = len(q)
        return root

