
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        https://leetcode.com/problems/kth-smallest-element-in-a-bst/

        Given a binary search tree, write a function kthSmallest to find the 
        kth smallest element in it.

        Note:
        You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
        
        Example 1:
        
        Input: root = [3,1,4,null,2], k = 1
           3
          / \
         1   4
          \
           2
        Output: 1
        Example 2:
        
        Input: root = [5,3,6,2,4,null,null,1], k = 3
               5
              / \
             3   6
            / \
           2   4
          /
         1
        Output: 3
        Follow up:
        What if the BST is modified (insert/delete operations) often and you 
        need to find the kth smallest frequently? How would you optimize the 
        kthSmallest routine?


        References
        ---------
        .. [1] https://leetcode.com/problems/kth-smallest-element-in-a-bst/discuss/63703/Pythonic-approach-with-generator

        """
        kth_list = list()

        def in_order(r):
            if not r:
                return
            in_order(r.left)
            kth_list.append(r.val)
            if len(kth_list) == k:
                return
            in_order(r.right)
        in_order(root)
        return kth_list[k-1]


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

    print(sol.kthSmallest(node1, 1))
    print(sol.kthSmallest(node1, 2))
    print(sol.kthSmallest(node1, 3))
    print(sol.kthSmallest(node1, 6))

