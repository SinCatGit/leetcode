from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        """
        https://leetcode.com/problems/find-duplicate-subtrees/

        Given a binary tree, return all duplicate subtrees. For each kind of
        duplicate subtrees, you only need to return the root node of any one of them.

        Two trees are duplicate if they have the same structure with same node values.

        Parameters
        ----------
        root: TreeNode

        Returns
        -------
        List[TreeNode]

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/find-duplicate-subtrees/discuss/106016/O(n)-time-and-space-lots-of-analysis
        .. [2] https://www.youtube.com/watch?v=LYU3y0-59_k

        """
        from collections import defaultdict
        id_hash = defaultdict()
        id_hash.default_factory = id_hash.__len__

        tree_hash = defaultdict(list)

        def get_id(r: TreeNode):
            if r:
                tree_id = id_hash[frozenset((r.val, get_id(r.left), get_id(r.right)))]
                tree_hash[tree_id].append(r)
                return tree_id

        get_id(root)
        return [ids[0] for ids in tree_hash.values() if len(ids) > 1]

    def findDuplicateSubtreesV01(self, root: TreeNode) -> List[TreeNode]:
        from collections import defaultdict
        nodes = defaultdict(list)

        def traverse(r: TreeNode):
            if not r:
                return ''
            tree_id = f'({r.val}, {traverse(r.left)}, {traverse(r.right)})'
            nodes[tree_id].append(r)
            return tree_id
        traverse(root)

        return [ids[0] for ids in nodes.values() if len(ids) > 1]





