
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """
        https://leetcode.com/problems/delete-node-in-a-bst/

        Given a root node reference of a BST and a key, delete the node with 
        the given key in the BST. Return the root node reference (possibly 
        updated) of the BST.

        Basically, the deletion can be divided into two stages:

        Search for a node to remove.
        If the node is found, delete the node.
        Note: Time complexity should be O(height of tree).

        References
        ---------
        .. [1] https://leetcode.com/problems/delete-node-in-a-bst/discuss/93374/Simple-Python-Solution-With-Explanation
        .. [2] https://leetcode.com/problems/delete-node-in-a-bst/discuss/93296/Recursive-Easy-to-Understand-Java-Solution

        """
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            t = root.right
            mini_val = t.val
            while t.left:
                t = t.left
                mini_val = t.val
            root.val = mini_val
            root.right = self.deleteNode(root.right, mini_val)
        return root


if __name__ == '__main__':
    sol = Solution()
    #    5
    #   / \
    #   3  6
    #  /  \ \
    #  2  4  7

    node1 = TreeNode(5)
    node3 = TreeNode(3)
    node2 = TreeNode(6)
    node4 = TreeNode(2)
    node5 = TreeNode(4)
    node6 = TreeNode(7)

    node1.left = node3
    node1.right = node2
    node3.left = node4
    node3.right = node5
    node2.right = node6

    from collections import deque
    q = deque([sol.deleteNode(node1, 0)])
    while q:
        node = q.popleft()
        print(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

