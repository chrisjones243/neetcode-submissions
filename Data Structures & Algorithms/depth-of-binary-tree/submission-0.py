# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth: int = 0) -> int:

        if root != None:
            depth += max(self.maxDepth(root.left, depth), 
                self.maxDepth(root.right, depth)) + 1

        return depth
        