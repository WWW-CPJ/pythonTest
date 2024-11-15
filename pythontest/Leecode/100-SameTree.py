# 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

from typing import Optional

# TreeNode 类:这是一个基本的二叉树节点类，包含值 val，左子树 left 和右子树 right。
class Treenode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[Treenode], q: Optional[Treenode]) -> bool:
        # 首先检查两个节点 p 和 q 是否都是 None。如果是，说明两个树都为空，因此它们是相同的。
        # 如果两个节点都为空，树相同
        if not p and not q:
            return True
        # 如果有一个节点为空，树不相同
        if not p or not q:
            return False
        # 如果当前节点的值不同，树是不相同的
        if p.value != q.value:
            return False
        
        # 递归检查左子树和右子树
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 

# 树的输入 是前序遍历
p = Treenode(1)
p.left = Treenode(2)
p.right = Treenode(3)

q = Treenode(1)
q.left = Treenode(2)
q.right = Treenode(3)

objectSolution = Solution()
print(objectSolution.isSameTree(p, q))