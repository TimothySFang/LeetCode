# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        order_dict = defaultdict(list)
        queue = deque()
        height = 0
        if not root:
            return []
        def dfs(curr_node, order) :
            if not curr_node:
                return

            nonlocal height
            height = max(height, order)
            order_dict[order].append(curr_node.val)

            dfs(curr_node.left, order + 1)
            dfs(curr_node.right, order + 1)
        
        dfs(root, 0)
        print(order_dict)
        result = []
        for i in range(height + 1):
            result.append(order_dict[i])
        return result