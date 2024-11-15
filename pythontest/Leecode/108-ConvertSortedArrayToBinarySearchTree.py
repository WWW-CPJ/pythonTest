# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right    # self.right = right: 将传入的 right 赋值给节点的 right 属性。

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        # Helper function to recursively build the tree.  辅助函数递归构建树
        def convert_to_bst(left:int, right:int) ->Optional[TreeNode]:
            # left: int: 子数组的起始索引。
            # right: int: 子数组的结束索引。

            # 检查子数组的其实索引是否超过结束索引，如果其实索引大于结束索引，返回 None，表示 该子树为空
            if left > right:
                return None
            
            # 计算当前子数组的中间索引
            mid = (left + right) //2
            root = TreeNode(nums[mid])
            # 使用中间索引的元素创建一个新的 TreeNode 实例，作为当前子树的跟节点

            # Recursively build the left and right subtree.  递归构建左右子树
            root.left = convert_to_bst(left, mid-1)
            root.right = convert_to_bst(mid+1, right)

            return root
        
        # Start the recursion with the entire array.  从整个数组开始递归
        return convert_to_bst(0, len(nums)-1)
    

nums = [-10, -3, 0, 5, 9]

objectSolution = Solution()
print(objectSolution.sortedArrayToBST(nums))





# 要将一个升序排列的整数数组 `nums` 转换为一棵平衡二叉搜索树（BST），你可以使用递归的方法。这个过程的关键思想是利用数组的中间元素作为树的根节点，这样可以确保左子树和右子树的节点数量尽可能平衡。
# ### 步骤
# 1. **选择根节点**: 选择数组的中间元素作为树的根节点，这样可以确保左右子树的节点数量尽可能平衡。
# 2. **递归构建子树**:
#    - 对于根节点的左子树，递归地处理数组中根节点左侧的部分。
#    - 对于根节点的右子树，递归地处理数组中根节点右侧的部分。
# 3. **终止条件**: 如果数组为空或子数组的起始索引大于终止索引，则返回 `None`（表示没有子树）。

# ### 实现
# 下面是实现上述算法的 Python 代码：
# ```python
# from typing import List, Optional
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#         # Helper function to recursively build the tree
#         def convert_to_bst(left: int, right: int) -> Optional[TreeNode]:
#             if left > right:
#                 return None
#             mid = (left + right) // 2
#             root = TreeNode(nums[mid])     
#             # Recursively build the left and right subtrees
#             root.left = convert_to_bst(left, mid - 1)
#             root.right = convert_to_bst(mid + 1, right)       
#             return root 
#         # Start the recursion with the entire array
#         return convert_to_bst(0, len(nums) - 1)
# ```

# ### 代码解析
# 1. **TreeNode 类**:
#    - 用于创建树节点，包含节点值 `val` 和左右子节点 `left`、`right`。
# 2. **`sortedArrayToBST` 方法**:
#    - 这是主函数，它接受一个升序排列的数组 `nums`。
#    - 调用辅助函数 `convert_to_bst` 来递归构建平衡的 BST。
# 3. **`convert_to_bst` 辅助函数**:
#    - **参数**: `left` 和 `right` 表示当前处理的子数组的范围。
#    - **终止条件**: 当 `left` 大于 `right` 时，返回 `None`。
#    - **中间节点**: 计算中间索引 `mid`，创建树节点。
#    - **递归调用**: 分别递归构建左子树和右子树。

# ### 示例
# 假设输入数组是 `[1, 2, 3, 4, 5, 6, 7]`，转换后的平衡二叉搜索树将如下所示：
# ```
#        4
#      /   \
#     2     6
#    / \   / \
#   1   3 5   7
# ```
# ### 总结
# 通过选择数组的中间元素作为树的根节点，可以保证生成的二叉搜索树是平衡的。递归地处理左右子数组来构建左子树和右子树，
# 这种方法确保了树的高度保持在对数级别，达到了平衡的要求。


# 下面是对代码逐句的详细分析：
# ```python
# from typing import List, Optional
# ```
# - **`from typing import List, Optional`**: 从 `typing` 模块导入 `List` 和 `Optional` 类型注解。
#   - **`List[int]`**: 表示一个包含整数的列表。
#   - **`Optional[TreeNode]`**: 表示一个可以是 `TreeNode` 对象或 `None` 的类型，通常用于表示函数返回值可能为空的情况。

# ```python
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# ```
# - **`class TreeNode:`**: 定义一个二叉树节点的类。
#   - **`def __init__(self, val=0, left=None, right=None):`**: 构造函数，用于初始化一个 `TreeNode` 实例。
#     - **`val=0`**: 节点的值，默认值为 `0`。
#     - **`left=None`**: 节点的左子树，默认为 `None`。
#     - **`right=None`**: 节点的右子树，默认为 `None`。
#   - **`self.val = val`**: 将传入的 `val` 赋值给节点的 `val` 属性。
#   - **`self.left = left`**: 将传入的 `left` 赋值给节点的 `left` 属性。
#   - **`self.right = right`**: 将传入的 `right` 赋值给节点的 `right` 属性。

# ```python
# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
# ```
# - **`class Solution:`**: 定义一个 `Solution` 类，其中包含处理问题的函数。
# - **`def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:`**: 定义一个方法 `sortedArrayToBST`，用于将升序排列的数组 `nums` 转换为平衡的二叉搜索树。
#   - **`nums: List[int]`**: 参数 `nums` 是一个包含整数的升序数组。
#   - **`-> Optional[TreeNode]`**: 方法的返回类型是一个 `TreeNode` 对象或 `None`，表示生成的平衡二叉搜索树的根节点。

# ```python
#         # Helper function to recursively build the tree
#         def convert_to_bst(left: int, right: int) -> Optional[TreeNode]:
# ```
# - **`def convert_to_bst(left: int, right: int) -> Optional[TreeNode]:`**: 定义一个辅助递归函数 `convert_to_bst`，用于从 `nums` 的子数组中递归构建二叉搜索树。
#   - **`left: int`**: 子数组的起始索引。
#   - **`right: int`**: 子数组的结束索引。
#   - **`-> Optional[TreeNode]`**: 返回值是一个 `TreeNode` 对象或 `None`，表示构建的子树的根节点。

# ```python
#             if left > right:
#                 return None
# ```
# - **`if left > right:`**: 检查子数组的起始索引是否超过结束索引。
#   - **`return None`**: 如果起始索引大于结束索引，则返回 `None`，表示该子树为空。

# ```python
#             mid = (left + right) // 2
#             root = TreeNode(nums[mid])
# ```
# - **`mid = (left + right) // 2`**: 计算当前子数组的中间索引。
# - **`root = TreeNode(nums[mid])`**: 使用中间索引的元素创建一个新的 `TreeNode` 实例，作为当前子树的根节点。

# ```python
#             # Recursively build the left and right subtrees
#             root.left = convert_to_bst(left, mid - 1)
#             root.right = convert_to_bst(mid + 1, right)
# ```
# - **`root.left = convert_to_bst(left, mid - 1)`**: 递归地构建当前节点的左子树，子数组的范围是 `left` 到 `mid - 1`。
# - **`root.right = convert_to_bst(mid + 1, right)`**: 递归地构建当前节点的右子树，子数组的范围是 `mid + 1` 到 `right`。

# ```python
#             return root
# ```
# - **`return root`**: 返回构建好的当前子树的根节点。

# ```python
#         # Start the recursion with the entire array
#         return convert_to_bst(0, len(nums) - 1)
# ```
# - **`return convert_to_bst(0, len(nums) - 1)`**: 从整个数组范围开始递归地构建二叉搜索树。
#   - **`0`**: 数组的起始索引。
#   - **`len(nums) - 1`**: 数组的结束索引。

# ### 总结
# 这个代码片段实现了将一个升序排列的整数数组转换为一棵平衡的二叉搜索树。具体步骤是通过递归方法选择中间元素作为当前子树的根节点，
# 然后递归地处理左右子数组来构建左右子树，最终返回整个树的根节点。这样的方法保证了生成的二叉搜索树是平衡的，
# 因为每次选择的中间元素能尽量均匀地分配节点到左右子树。




# 这段代码的逻辑是将一个升序排列的整数数组转换为一棵平衡的二叉搜索树（BST）。为了理解代码的逻辑以及如何确定子树的结构，下面详细解释每个步骤和其背后的思想。
# ### 代码逻辑
# 1. **选择根节点**:
#    - 代码中的关键思想是利用数组的中间元素作为当前子树的根节点。这是因为对于一个升序排列的数组，选择中间元素作为根节点可以确保左右子树的节点数量尽可能平衡。
#    - 通过这种方式构建的树是平衡的，即左右子树的高度差不会超过1，从而保证了树的整体平衡性。

# 2. **递归构建子树**:
#    - 对于每个节点（由中间元素确定），我们递归地构建其左子树和右子树。
#    - 对于当前子树的左子树，我们只需要考虑当前子数组中中间元素左侧的部分。
#    - 对于当前子树的右子树，我们只需要考虑当前子数组中中间元素右侧的部分。

# 3. **终止条件**:
#    - 如果子数组的起始索引大于结束索引，表示该子数组为空，这时候返回 `None`，表示没有子树。

# ### 如何知道子树的结构

# 1. **确定根节点**:
#    - 对于当前处理的子数组 `nums[left:right+1]`，选择中间元素 `nums[mid]` 作为根节点。
#    - 中间索引 `mid` 计算公式为 `(left + right) // 2`。

# 2. **构建左子树**:
#    - 对于当前节点的左子树，我们处理的是当前子数组中 `left` 到 `mid - 1` 的部分。
#    - 递归调用 `convert_to_bst(left, mid - 1)` 来构建左子树。

# 3. **构建右子树**:
#    - 对于当前节点的右子树，我们处理的是当前子数组中 `mid + 1` 到 `right` 的部分。
#    - 递归调用 `convert_to_bst(mid + 1, right)` 来构建右子树。

# 4. **递归终止条件**:
#    - 如果递归的子数组范围不合法（即 `left > right`），则返回 `None`，表示该子树为空。

# ### 示例说明

# 假设我们有一个升序排列的数组 `[1, 2, 3, 4, 5, 6, 7]`，我们要将其转换为平衡的二叉搜索树。

# - **初始调用**:
#   - `convert_to_bst(0, 6)` 处理整个数组。
#   - 中间索引为 `(0 + 6) // 2 = 3`，所以根节点为 `4`。

# - **构建左子树**:
#   - 调用 `convert_to_bst(0, 2)` 处理 `[1, 2, 3]`。
#   - 中间索引为 `(0 + 2) // 2 = 1`，所以左子树的根节点为 `2`。
#   - 再次递归构建左子树，处理 `[1]` 和右子树，处理 `[3]`。

# - **构建右子树**:
#   - 调用 `convert_to_bst(4, 6)` 处理 `[5, 6, 7]`。
#   - 中间索引为 `(4 + 6) // 2 = 5`，所以右子树的根节点为 `6`。
#   - 再次递归构建左子树，处理 `[5]` 和右子树，处理 `[7]`。

# 最终，构建的平衡二叉搜索树如下所示：

# ```
#        4
#      /   \
#     2     6
#    / \   / \
#   1   3 5   7
# ```

# ### 总结
# 通过递归地选择数组的中间元素作为每个子树的根节点，代码能够构建出一棵平衡的二叉搜索树。这种方法确保了树的平衡性，
# 因为每次选择的中间元素能够将子数组均匀地分为左右两部分，从而使得树的高度保持在对数级别。