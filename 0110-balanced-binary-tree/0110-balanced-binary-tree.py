# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag = True
        def height(root):
            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)

            if left - right > 1 or right - left > 1:
                self.flag = False
                return 0

            return max(left, right) + 1
        height(root)
        return self.flag