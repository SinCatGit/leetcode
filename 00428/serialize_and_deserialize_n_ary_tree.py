

class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Codec:
    """
    https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

    Serialization is the process of converting a data structure or object into a sequence of
    bits so that it can be stored in a file or memory buffer, or transmitted across a network
    connection link to be reconstructed later in the same or another computer environment.

    Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted
    tree in which each node has no more than N children. There is no restriction on how your
    serialization/deserialization algorithm should work. You just need to ensure that an N-ary
    tree can be serialized to a string and this string can be deserialized to the original tree structure.

    For example, you may serialize the following 3-ary tree

        1
      / | \
     3  2  4
    / \
    5 6
    as [1 [3[5 6] 2 4]]. You do not necessarily need to follow this format, so please be creative
    and come up with different approaches yourself.

    Note:
        N is in the range of [1, 1000]
        Do not use class member/global/static variables to store states. Your serialize and
        deserialize algorithms should be stateless.

    References
    ---------
    .. [1] https://aaronice.gitbooks.io/lintcode/trees/serialize-and-deserialize-n-ary-tree.html
    .. [2] https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/discuss/151421/Java-preorder-recursive-solution-using-queue

    """

    def serialize(self, root: DirectedGraphNode) -> str:
        """
        Encodes a tree to a single string.
        """
        res = list()
        if not root:
            return ''

        def pre_order(r: DirectedGraphNode):
            res.append(str(r.label))
            for i in r.neighbors:
                pre_order(i)
            res.append('#')

        pre_order(root)
        return ' '.join(res)

    def deserialize(self, data: str) -> DirectedGraphNode:
        """
        Decodes your encoded data to tree.
        """
        tokens = iter(data.split())

        def pre_order():
            val = next(tokens)
            if val == '#':
                return None

            node = DirectedGraphNode(val)
            child = pre_order()
            while child:
                node.neighbors.append(child)
                child = pre_order()

            return node

        return pre_order()

    def deserializeV01(self, data: str) -> DirectedGraphNode:
        """
        Decodes your encoded data to tree.
        """
        if not data:
            return None
        from collections import deque
        tokens = deque(data.split())
        root = DirectedGraphNode(tokens.popleft())

        def pre_order(r):
            if not tokens:
                return
            while tokens[0] != '#':
                node = DirectedGraphNode(tokens.popleft())
                r.neighbors.append(pre_order(node))

            tokens.popleft()
            return r

        pre_order(root)
        return root

    def serializeV02(self, root: DirectedGraphNode) -> str:
        """
        Encodes a tree to a single string.
        """
        res = list()
        if not root:
            return ''

        def pre_order(r: DirectedGraphNode):
            res.append(str(r.label))
            res.append(str(len(r.neighbors)))
            for i in r.neighbors:
                pre_order(i)

        pre_order(root)
        return ' '.join(res)

    def deserializeV02(self, data: str) -> DirectedGraphNode:
        """
        Decodes your encoded data to tree.
        """
        tokens = iter(data.split())

        def pre_order():
            val = next(tokens)

            node = DirectedGraphNode(val)
            for i in range(int(next(tokens))):
                node.neighbors.append(pre_order())

            return node

        return pre_order()


if __name__ == '__main__':
    sol = Codec()
    #     1
    #   / | \
    #  3  2  4
    # / \
    # 5  6
    node1 = DirectedGraphNode(1)
    node3 = DirectedGraphNode(3)
    node2 = DirectedGraphNode(2)
    node4 = DirectedGraphNode(4)
    node5 = DirectedGraphNode(5)
    node6 = DirectedGraphNode(6)
    node1.neighbors.append(node3)
    node1.neighbors.append(node2)
    node1.neighbors.append(node4)
    node3.neighbors.append(node5)
    node3.neighbors.append(node6)
    print(sol.serialize(node1))
    print(sol.serialize(sol.deserialize(sol.serialize(node1))))
    print(sol.serialize(sol.deserializeV01(sol.serialize(node1))))
    print(sol.serializeV02(sol.deserializeV02(sol.serializeV02(node1))))

