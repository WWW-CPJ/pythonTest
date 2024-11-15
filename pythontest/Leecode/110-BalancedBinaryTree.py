# 给定一个二叉树，判断它是否是 平衡二叉树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check_balance_and_height(node: TreeNode) -> (bool, int): # type: ignore
            if node is None:
                return True, 0
            
            # Check left subtree
            left_balanced, left_height = check_balance_and_height(node.left)
            if not left_balanced:
                return False, 0
            
            # Check right subtree
            right_balanced, right_height = check_balance_and_height(node.right)
            if not right_balanced:
                return False, 0
            
            # Check current node balance
            balanced = abs(left_height - right_height) <= 1
            height = max(left_height, right_height) + 1
            
            return balanced, height
        
        balanced, _ = check_balance_and_height(root)
        return balanced


# 判断一个二叉树是否为平衡二叉树（或平衡树）的标准是二叉树的高度差不能超过1。
# 具体来说，一棵平衡二叉树的每个节点的左子树和右子树的高度差不能超过1。要实现这一点，可以使用递归方法来检查树的高度并同时判断是否平衡。

# ### 定义
# - **平衡二叉树**：对于每个节点，其左子树和右子树的高度差（即 `left_height - right_height`）不超过1。

# ### 递归方法
# 一种常见的递归方法是，在递归计算每个子树的高度时，同时检查每个子树是否平衡。具体步骤如下：

# 1. **计算树的高度**：
#    - 递归地计算左子树和右子树的高度。
#    - 树的高度是从节点到其最深叶子节点的最长路径长度。

# 2. **检查子树的平衡性**：
#    - 如果某个子树的高度差超过1，则树不平衡。
#    - 如果左右子树都平衡且高度差不超过1，则当前节点也是平衡的。

# ### 实现
# 下面是一个 Python 示例代码，演示如何判断二叉树是否为平衡二叉树：

# ```python
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         def check_balance_and_height(node: TreeNode) -> (bool, int):
#             if node is None:
#                 return True, 0
            
#             # Check left subtree
#             left_balanced, left_height = check_balance_and_height(node.left)
#             if not left_balanced:
#                 return False, 0
            
#             # Check right subtree
#             right_balanced, right_height = check_balance_and_height(node.right)
#             if not right_balanced:
#                 return False, 0
            
#             # Check current node balance
#             balanced = abs(left_height - right_height) <= 1
#             height = max(left_height, right_height) + 1
            
#             return balanced, height
        
#         balanced, _ = check_balance_and_height(root)
#         return balanced
# ```

# ### 代码解析
# 1. **TreeNode 类**:
#    - 定义了二叉树节点的数据结构，包含节点值 `val` 和左右子节点 `left`、`right`。

# 2. **`isBalanced` 方法**:
#    - 这是主方法，检查树是否平衡。调用了辅助函数 `check_balance_and_height` 来计算树的平衡性和高度。

# 3. **`check_balance_and_height` 辅助函数**:
#    - **返回值**: 返回一个二元组 `(bool, int)`，第一个元素是布尔值，表示子树是否平衡；第二个元素是树的高度。
#    - **递归终止条件**:
#      - 如果节点为空 (`node is None`)，则返回 `True` 和高度 `0`。
#    - **检查左子树**:
#      - 递归地计算左子树的平衡性和高度。如果左子树不平衡，则返回 `False` 和高度 `0`。
#    - **检查右子树**:
#      - 递归地计算右子树的平衡性和高度。如果右子树不平衡，则返回 `False` 和高度 `0`。
#    - **检查当前节点平衡性**:
#      - 判断当前节点的左右子树高度差是否超过1。如果超过，则当前节点不平衡。
#    - **计算当前节点高度**:
#      - 当前节点的高度是其左右子树高度的最大值加1。

# 4. **返回结果**:
#    - 通过调用 `check_balance_and_height` 得到根节点的平衡性，并返回结果。

# ### 总结
# 通过递归计算每个节点的左右子树的高度，并检查高度差是否超过1，可以有效判断一个二叉树是否为平衡二叉树。
# 该方法的时间复杂度为 \(O(n)\)，其中 \(n\) 是树中节点的数量，因为每个节点都被访问一次。