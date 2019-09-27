# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # recursion
        def f(nodes):
            if not nodes:
                return True

            s = [node.val for node in nodes]
            if s != s[::-1]:
                return False
            tem = []
            for node in nodes:
                tem.append(node.left)
                tem.append(node.right)
            return f(tem)

        return f(root)

        # iteration
        
