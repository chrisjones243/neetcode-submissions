# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def level(nodes: List[TreeNode]) -> List[List[int]]:
            if not nodes:
                return []

            current_level = []
            next_level_nodes = []

            for node in nodes:
                current_level.append(node.val)

                if node.left is not None:
                    next_level_nodes.append(node.left)

                if node.right is not None:
                    next_level_nodes.append(node.right)

            out = [current_level]
            out.extend(level(next_level_nodes))

            return out

        return level([root] if root else [])

            
        