# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        def h(node):
            if not node:
                return 0

            l = 1
            if node.left:
                l += h(node.left)
            r = 1
            if node.right:
                r += h(node.right)
            return max(l, r)
        return h(root)
