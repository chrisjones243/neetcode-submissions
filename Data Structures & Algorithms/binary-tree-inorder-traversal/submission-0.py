# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        out: List[int] = []

        # Leaf node, return val
        if not (root.left or root.right):
            return [root.val]

        # Add left subtree to output
        if root.left:
            out.extend(self.inorderTraversal(root.left))

        # add current value to output
        out.append(root.val)

        # Add right subtree to output
        if root.right:
            out.extend(self.inorderTraversal(root.right))

        return out