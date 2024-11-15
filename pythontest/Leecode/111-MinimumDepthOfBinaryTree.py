# 给定一个二叉树，找出其最小深度。
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 说明：叶子节点是指没有子节点的节点。

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        # 定义一个递归函数计算深度
        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0 
            
            # 如果左子树为空，计算右子树的深度
            if not node.left:
                return depth(node.right) + 1
            
            # 如果右子树为空，计算左子树的深度
            if not node.right:
                return depth(node.left) + 1
            
            # 左右子树都在，计算最小深度
            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # 当前节点的深度，是左右子树深度的最小值
            return min(left_depth, right_depth) + 1
        return depth(root)

        
# root =TreeNode(3)
# left = TreeNode(9)
# right = TreeNode(20)

# right.left = TreeNode(15)
# right.right = TreeNode(7)
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

objectSolution = Solution()
print(objectSolution.minDepth(root))

root = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)

objectSolution = Solution()
print(objectSolution.minDepth(root))