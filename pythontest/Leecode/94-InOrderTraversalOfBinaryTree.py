# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        # 构造函数

class Solution:
    # 递归法
    def inorderTraversal_Recursion(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node):
            if node is None:
            # if not node:
                return []
            # 递归遍历左子树，访问根节点，递归遍历右子树
            return inorder(node.left) + [node.val] + inorder(node.right)
        return inorder(root)
# 函数中，如果 node为空，返回[]，如果不为空返回什么？
# return inorder(node.left) + [node.val] + inorder(node.right)  这句代码，分别返回的是什么，加起来是组成了一个列表嘛？
# node 和 root 的关系是什么？
# 递归遍历:
# inorder(node.left): 递归遍历当前节点的左子树，返回左子树中序遍历的结果列表。
# [node.val]: 当前节点的值作为一个单元素列表。
# inorder(node.right): 递归遍历当前节点的右子树，返回右子树中序遍历的结果列表。
# 合并结果:
# 将左子树的结果列表、当前节点的值和右子树的结果列表合并成一个新的列表。这是中序遍历的标准方式，即：左子树 -> 根节点 -> 右子树。
# 通过 + 运算符组合成一个完整的中序遍历列表

    # 迭代法
    def inorderTraversal_Iteration(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root

        while current or stack:
            # 将当前节点及其所有左子节点 入栈
            while current:
                stack.append(current)
                current = current.left

            # 弹出栈顶节点，访问节点
            current = stack.pop()
            result.append(current.val)

            # 处理当前节点的右子树
            current = current.right
        return result
        

root = TreeNode[1, null, 2, 3] # type: ignore
objectSoluction = Solution()
print(objectSoluction.inorderTraversal_Recursion(root))
print(objectSoluction.inorderTraversal_Iteration(root))


# 递归方法是实现中序遍历的最简单和直观的方法。基本思想是：
# 递归遍历左子树。
# 访问当前节点（根节点）。
# 递归遍历右子树。
# 代码解释:
# inorder 函数实现了中序遍历的递归逻辑。对于每个节点，先递归遍历左子树，再访问当前节点，最后递归遍历右子树。
# 递归函数返回一个由节点值组成的列表，通过列表的连接合并结果。

# 2. 迭代方法（使用栈）
# 迭代方法通过栈模拟递归过程，避免了递归调用的开销。基本思想是：
# 使用栈保存节点，先将根节点及其所有左子节点入栈。
# 弹出栈顶节点，访问节点。
# 将弹出节点的右子节点（如果存在）入栈，并继续处理。
# 代码解释: 
# 使用栈 stack 来模拟递归的过程。首先，将所有左子节点入栈，直到到达最左下的节点。
# 弹出栈顶节点，访问其值，并处理该节点的右子树。
# 重复上述步骤，直到栈为空且当前节点为 None。

# 要使用 `input` 函数生成一个二叉树，你需要首先设计一种方法来从输入字符串中构造二叉树。这通常涉及解析输入字符串并使用这些值来创建二叉树节点。
# 以下是一个实现示例，展示如何从 `input` 函数中读取的字符串生成二叉树：
# ### 步骤概述
# 1. **定义树节点类**：定义一个表示二叉树节点的类。
# 2. **解析输入**：从输入字符串中读取节点值，并构建二叉树。
# 3. **生成二叉树**：根据读取的值构建树结构。
# 4. **实现中序遍历**：遍历并输出生成的二叉树。

# ### Python 实现
# 首先，定义一个 `TreeNode` 类，然后编写代码从输入生成二叉树，并执行中序遍历：
# ```python
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def build_tree_from_list(values):
#     """从层序遍历的值列表构建二叉树"""
#     if not values:
#         return None
    
#     from collections import deque
    
#     root = TreeNode(values[0])
#     queue = deque([root])
#     index = 1
    
#     while queue and index < len(values):
#         node = queue.popleft()
        
#         if values[index] is not None:
#             node.left = TreeNode(values[index])
#             queue.append(node.left)
#         index += 1
        
#         if index < len(values) and values[index] is not None:
#             node.right = TreeNode(values[index])
#             queue.append(node.right)
#         index += 1
    
#     return root

# def inorder_traversal(root):
#     """中序遍历二叉树"""
#     result = []
    
#     def inorder(node):
#         if node:
#             inorder(node.left)
#             result.append(node.val)
#             inorder(node.right)
    
#     inorder(root)
#     return result

# def main():
#     # 从用户输入读取二叉树节点值
#     input_values = input("请输入二叉树节点值（用空格分隔，'None' 表示空节点）：").strip()
#     if not input_values:
#         print("输入为空")
#         return
    
#     # 将输入的字符串转换为列表
#     values = [int(x) if x != 'None' else None for x in input_values.split()]
    
#     # 构建二叉树
#     root = build_tree_from_list(values)
    
#     # 执行中序遍历
#     inorder_result = inorder_traversal(root)
    
#     print("中序遍历结果：")
#     print(inorder_result)

# if __name__ == "__main__":
#     main()
# ```

# ### 代码解释

# 1. **TreeNode 类**：
#    - 定义了一个树节点类，包含值 `val`、左子节点 `left` 和右子节点 `right`。

# 2. **build_tree_from_list 函数**：
#    - 从给定的值列表（层序遍历的结果）构建二叉树。使用队列 `deque` 来帮助构建树结构。

# 3. **inorder_traversal 函数**：
#    - 实现了二叉树的中序遍历，将遍历结果存储在 `result` 列表中。

# 4. **main 函数**：
#    - 从用户输入读取二叉树节点值，处理输入，将其转换为列表。
#    - 构建二叉树并执行中序遍历，打印遍历结果。

# ### 使用示例

# 1. **运行程序**。
# 2. **输入二叉树节点值**，例如 `1 2 3 None None 4 5`（表示如下二叉树）：

# ```
#     1
#    / \
#   2   3
#      / \
#     4   5
# ```

# 3. **程序将输出中序遍历结果**，即 `[2, 1, 4, 3, 5]`。

# 这样，你就可以通过 `input` 函数生成一个二叉树，并进行中序遍历。