# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return root

        isLeaf = root.left == None and root.right == None

        if isLeaf:
            return root
        
        old_left = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(old_left)

        return root
        