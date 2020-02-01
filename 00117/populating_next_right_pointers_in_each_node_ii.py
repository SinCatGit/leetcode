
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

        Given a binary tree

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

        Parameters
        ----------
        root: Node

        Returns
        -------
        Node

        Examples
        --------

        References
        ---------
        .. [1] https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/37824/AC-Python-O(1)-space-solution-12-lines-and-easy-to-understand

        """
        parent = root
        child_head = Node(0)
        child = child_head

        while parent:
            for c in [parent.left, parent.right]:
                child.next = c
                if c:
                    child = child.next
            if parent.next:
                parent = parent.next
            else:
                parent = child_head.next
                child = child_head
        return root
