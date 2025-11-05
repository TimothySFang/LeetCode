# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_view = []
        queue = deque()
        queue.append(root)

        while queue:
            level_nodes = len(queue)
            right_flag = True
            for _ in range(level_nodes):
                curr_node = queue.popleft()
                if not curr_node:
                    continue
                if right_flag:
                    right_view.append(curr_node.val)
                    right_flag = False
                queue.append(curr_node.right)
                queue.append(curr_node.left)
        
        return right_view