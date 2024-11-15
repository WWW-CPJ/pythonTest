# 给定一个二叉树 root ，返回其最大深度。
# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
#  111找出最小深度
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) ->int:
        # 定义一个递归函数 来计算深度
        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            # 递归计算左右子树的深度
            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # 当前节点的深度 是左右子树深度的最大值 加1
            return max(left_depth, right_depth) +1
        return depth(root)

        
# root =TreeNode(3)
# left = TreeNode(9)
# right = TreeNode(20)

# right.left = TreeNode(15)
# right.right = TreeNode(7)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

objectSolution = Solution()
print(objectSolution.maxDepth(root))