# 定义二叉树节点类
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# 创建二叉树
# 创建树的节点
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# 添加更多节点
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


# In-order traversal   中序
# Pre-order traversal   前序
# Post-order traversal   后序

# 前序遍历二叉树
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


# 中序遍历 
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)   # 遍历左子树
        print (node.value)
        in_order_traversal(node.right)

# 后序遍历
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def post_order_traversal(node):
            if node is None:
                return []
            return post_order_traversal(node.left) + post_order_traversal(node.right) + [node.val]
        return post_order_traversal(root)






# 列表 (list)：在 Python 中，遍历结果通常以列表的形式输出，因为列表是动态大小的数据结构，适合存储和操作序列数据。
# 数组 (array)：如果需要在 Python 中使用数组，可以使用 array 模块（适用于更基本的数据类型）或第三方库如 NumPy 提供的数组类型，但对于大多数树遍历应用，列表已经足够。