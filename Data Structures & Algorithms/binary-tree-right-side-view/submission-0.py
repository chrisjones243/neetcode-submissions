# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def level(nodes: List[TreeNode]) -> List[int]:
            if not nodes:
                return []

            current_level: List[int] = []
            next_level_nodes: List[TreeNode] = []

            for node in nodes:
                current_level.append(node.val)

                if node.left:
                    next_level_nodes.append(node.left)

                if node.right:
                    next_level_nodes.append(node.right)

            out = [current_level[-1]]
            out.extend(level(next_level_nodes))

            return out
        
        return level([root] if root else [])