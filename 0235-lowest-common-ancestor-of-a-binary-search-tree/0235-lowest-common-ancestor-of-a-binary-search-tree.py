# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def findLCA(curr_node):
            if p.val == curr_node.val:
                return p
            elif q.val == curr_node.val:
                return q
            if (q.val < curr_node.val < p.val) or (p.val < curr_node.val < q.val):
                return curr_node

            if p.val < curr_node.val and q.val < curr_node.val:
                #search left
                return findLCA(curr_node.left)

            if p.val > curr_node.val and q.val > curr_node.val:
                # search right
                return findLCA(curr_node.right)
        
        return findLCA(root)