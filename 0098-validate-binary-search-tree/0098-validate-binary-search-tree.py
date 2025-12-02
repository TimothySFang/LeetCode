# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BFS implementation

        heap = deque([(root, -math.inf, math.inf)])

        while heap:
            curr, minval, maxval = heap.popleft()
            print(curr.val, minval, maxval)
            if curr.left and (not curr.val > curr.left.val or curr.left.val <= minval):
                return False

            if curr.right and (not curr.val < curr.right.val or curr.right.val >= maxval):
                return False
            
            if curr.left:
                heap.append((curr.left, minval, curr.val))
            if curr.right:
                heap.append((curr.right, curr.val, maxval))
        return True