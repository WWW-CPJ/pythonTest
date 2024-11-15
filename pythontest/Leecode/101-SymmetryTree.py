# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val =val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric (self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # 用一个 辅助函数来比较两个树是否镜像对称
        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            # 递归地比较两个子树是否镜像对称,所有条件都满足，return 语句的结果是 True，表示树是对称的。
            return (left.val == right.val) and isMirror(left.left, right.right) and isMirror (left.right, right.left) 
        
        # 从根节点开始检查左右子树的对称性
        return isMirror(root.left, root.right)


        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

objectSolution = Solution()
print (objectSolution.isSymmetric(root))