class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """
    https://leetcode.com/problems/serialize-and-deserialize-bst/

    Serialization is the process of converting a data structure or object into
    a sequence of bits so that it can be stored in a file or memory buffer, or
    transmitted across a network connection link to be reconstructed later in
    the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary search tree.
    There is no restriction on how your serialization/deserialization algorithm should work.
    You just need to ensure that a binary search tree can be serialized to a string and this
    string can be deserialized to the original tree structure.

    The encoded string should be as compact as possible.

    Note: Do not use class member/global/static variables to store states.
    Your serialize and deserialize algorithms should be stateless.

    References
    ---------
    .. [1] https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/74259/Recursive-preorder-Python-and-C%2B%2B-O(n)

    """

    def serialize(self, root: TreeNode) -> str:
        """
        Encodes a tree to a single string.
        """
        res = []

        def dfs(r: TreeNode):
            if r:
                res.append(str(r.val))
                dfs(r.left)
                dfs(r.right)

        dfs(root)
        return ' '.join(res)

    def deserialize(self, data: str) -> TreeNode:
        """
        Decodes your encoded data to tree.
        """
        preorder = [int(v) for v in data.split()]
        inorder = sorted(preorder)

        def dfs(mid_order):
            if mid_order:
                ind = mid_order.index(preorder.pop(0))
                node = TreeNode(int(mid_order[ind]))
                node.left = dfs(mid_order[:ind])
                node.right = dfs(mid_order[ind+1:])
                return node

        return dfs(inorder)


