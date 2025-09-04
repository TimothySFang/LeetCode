# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # max of left + max of right
        self.diameter = 0
        
        def height(root):
            if not root:
                return 0

            # get heights of left and right    
            left = height(root.left)
            right = height(root.right)

            # check for maximum diameter using LEFT + RIGHT
            self.diameter = max(left + right, self.diameter)

            # return only height
            return max(left, right) + 1

        height(root)
        return self.diameter