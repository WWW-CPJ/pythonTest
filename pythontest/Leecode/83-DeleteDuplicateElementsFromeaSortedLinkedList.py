# 给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
# ListNode 类表示链表的节点，包含节点值 val 和指向下一个节点的指针 next。
# 单链表 (Singly Linked List):A → B → C → D → None
# 每个节点有一个 next 指针，指向链表中的下一个节点。
# 头节点是链表的起始节点，尾节点的 next 指针为 None，表示链表的结束。

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        current = head
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


# 创建链表
def create_linked_list(values):
    # 从列表创建链表
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head



input_values = input("输入链表的值（用空格分隔):  ").strip()
if not input_values:
    print("链表为空")

# 将输入的字符串转换为整数列表
values = list(map(int, input_values.split()))

# 创建链表
head = create_linked_list(values)

objectSolution = Solution()
print(objectSolution.deleteDuplicates(head))



# 在链表操作中，将 `current` 指针设置为 `head` 是一种常见的做法，它让你从链表的头部开始处理整个链表。这个做法非常直观并且有效，因为你可以通过 `current` 指针遍历链表的所有节点。以下是为什么 `current` 可以等于 `head`，并且它如何用于处理整个链表的详细解释。
# ### 理解 `current = head`
# 1. **链表结构**：
#    - 链表由一系列节点组成，每个节点包含数据和一个指向下一个节点的指针。
#    - 链表的头节点（`head`）是链表的起始点，它是第一个节点的引用。
# 2. **初始化 `current`**：
#    - 将 `current` 设置为 `head`，意味着 `current` 指针现在指向链表的第一个节点。
#    - 这使得你可以从链表的起点开始，逐个访问链表中的所有节点。
# ### 遍历链表的过程
# 1. **起始位置**：
#    - 通过 `current = head`，你将 `current` 指针设置为链表的起始位置。此时，`current` 指向链表的第一个节点。
# 2. **处理节点**：
#    - 使用 `current` 指针，你可以访问当前节点的值和下一个节点。
#    - 在链表遍历过程中，你可以修改 `current` 指向下一个节点，通过 `current = current.next` 来继续处理链表的其余部分。
# 3. **结束条件**：
#    - 遍历通常会在 `current` 为 `None` 时结束，即链表的末尾。循环条件如 `while current` 确保你在到达链表的末尾之前继续处理。
# ### 示例代码解释
# 以下是一个简单的示例，展示了如何从链表的头节点开始遍历链表，并处理每个节点：

# ```python
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# def print_linked_list(head: ListNode):
#     """打印链表的所有节点"""
#     current = head
#     while current:
#         print(current.val, end=" -> ")
#         current = current.next
#     print("None")
# # 创建链表: 1 -> 2 -> 3 -> 4
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
# print("链表内容:")
# print_linked_list(head)
# ```
# ###解释
# 1. **创建链表**：
#    - `head` 指向链表的第一个节点，该节点的值为 1，后面跟随值为 2、3 和 4 的节点。
# 2. **遍历链表**：
#    - 在 `print_linked_list` 函数中，将 `current` 设置为 `head`，从头节点开始遍历。
#    - 使用 `while current` 循环来访问链表的每个节点，直到 `current` 为 `None`（链表的末尾）。
# ### 总结
# 将 `current` 设置为 `head` 是一种标准的做法，能够让你从链表的起始点开始遍历。通过这种方式，你可以访问和处理链表的每个节点。这种方法在许多链表操作中都是必需的，例如删除重复节点、反转链表或搜索特定值等。