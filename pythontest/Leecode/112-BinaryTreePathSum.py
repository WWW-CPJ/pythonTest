# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。
# 判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。
# 如果存在，返回 true ；否则，返回 false 。
# 叶子节点 是指没有子节点的节点。

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], tragetSum: int) -> bool:
        if not root:
            return False
        def pathSum(node: Optional[TreeNode], currentSum: int) -> bool:
            if not node:
                return False
            # 更新当前路径的和
            currentSum = currentSum + node.val
        
            # 如果是叶子节点，检查路径和是否等于目标值
            if not node.left and not node.right:
                return currentSum == tragetSum
            
            # 递归检查左子树歌右子树
            return (pathSum(node.left, currentSum) or pathSum(node.right, currentSum))
        return pathSum(root, 0)

    

root = TreeNode(1)
root.left = TreeNode(2)
root.right= TreeNode(3)

objectSolution = Solution()
print(objectSolution.hasPathSum(root, 5))
                
