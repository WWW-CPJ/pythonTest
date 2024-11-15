from queue import Full
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def post_order_traversal(node):
            if node is None:
                return []
            return post_order_traversal(node.left) + post_order_traversal(node.right) + [node.val]
        return post_order_traversal(root)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
objects = Solution()
print(objects.postorderTraversal(root))