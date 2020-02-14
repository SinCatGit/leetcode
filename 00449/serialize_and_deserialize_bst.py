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
            else:
                res.append('#')

        dfs(root)
        return ' '.join(res)

    def deserialize(self, data: str) -> TreeNode:
        """
        Decodes your encoded data to tree.
        """
        def dfs():
            val = next(val_iter)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        val_iter = iter(data.split())
        return dfs()


if __name__ == '__main__':
    r = TreeNode(1)
    node2 = TreeNode(2)
    r.right = node2
    cr = codec.deserialize('1 # 2 # #')
    print(cr.val)
    print(cr.right.val)
    print(cr.left)
