
from typing import List, Optional


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def pre_orde_traversal(node):
            if node is None:
                return result
            return [node.val] + pre_orde_traversal(node.left) + pre_orde_traversal(node.right)
        return pre_orde_traversal(root)

# preorderTraversal 是主方法名，而 pre_order_travelsal 是内部函数名。
# preorderTraversal 函数本身不能被递归调用，需要一个辅助函数来进行递归调用
