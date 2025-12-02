# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS with a counter??

        count = 0
        def dfs(curr, path_max):
            if not curr:
                return 
            if curr.val >= path_max:
                nonlocal count
                count += 1
                dfs(curr.left, curr.val)
                dfs(curr.right, curr.val)
            else:
                dfs(curr.left, path_max)
                dfs(curr.right, path_max)
            
        dfs(root, -math.inf)
        return count