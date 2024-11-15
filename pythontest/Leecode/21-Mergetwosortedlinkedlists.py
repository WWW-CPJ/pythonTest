# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# ListNode 类表示链表的节点，包含节点值 val 和指向下一个节点的指针 next。
# 单链表 (Singly Linked List):A → B → C → D → None
# 每个节点有一个 next 指针，指向链表中的下一个节点。
# 头节点是链表的起始节点，尾节点的 next 指针为 None，表示链表的结束。

# Optional 通常用于函数参数或返回值类型，表示这些值是可选的，即可能不存在。
#  参数的类型是 Optional[ListNode]，意味着它可以是 ListNode 类型，也可以是 None。默认值 None 表示函数参数是可选的。
class Solution:
    def mergeList(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个虚拟节点作为新链表的起始点
        dummy = ListNode()    # dump 假的，仿真的，虚设的
        current = dummy
        # dummy 是一个虚拟头节点，用于简化合并过程。current 用于指向新链表的当前节点。
        # 当前节点也就是第一个节点，是我们虚构的的这个节点，
        #  dummy -> next

        # 遍历两个链表，直到其中一个链表为空
        while list1 and list2:              #  list1 and list2: 循环继续的条件是 list1 和 list2 都不为空。即，只有当两个链表都还有节点时，才会进入循环体。
            if list1.val <= list2.val:      #  比较两个链表当前节点的值，判断哪个值较小或相等。
                current.next = list1        #  将 current 节点的 next 指针指向 list1 的当前节点。这将把 list1 的当前节点添加到合并链表的末尾。
                list1 = list1.next          #  移动 list1 指针到下一个节点。这样在下一次循环中，list1 的当前节点将是下一个节点。
            else:
                current.next = list2
                list2 = list2.next

            # 使用 while list1 and list2 循环遍历两个链表。
            # 比较两个链表的当前节点值，较小的节点链接到 current.next。
            # 移动到下一个节点并更新 current。
            # 移动当前节点到下一节点
            current = current.next

            # 连接剩余的节点,当其中一个链表遍历完成后，直接将剩余的非空链表连接到新链表的末尾。
            if list1:
                current.next = list1
            if list2:
                current.next = list2

            # 返回合并后的链表的头节点
            return dummy.next


list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
list2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
objectSolution = Solution()
print(objectSolution.mergeList(list1, list2))

# 总结
# 合并后的链表从 dummy.next 开始：
# 1 → 1 → 2 → 3 → 4 → 4
# 初始化: 使用一个虚拟节点 dummy 和一个指针 current。
# 合并过程: 逐步比较两个链表的节点值，将较小的节点添加到合并链表，并移动 current 和输入链表的指针。
# 剩余节点: 当一个链表空时，将另一个链表的剩余部分直接连接到合并链表的末尾。
# 这种逐步合并的方式确保了合并链表的有序性。


# 递归
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if not l1: return l2  # 终止条件，直到两个链表都空
#         if not l2: return l1
#         if l1.val <= l2.val:  # 递归调用
#             l1.next = self.mergeTwoLists(l1.next,l2)
#             return l1
#         else:
#             l2.next = self.mergeTwoLists(l1,l2.next)
#             return l2




# def mergelist():
#     list1ength = int(input("请输入列表的长度: "))
#     list1 = []
#     list2 = []
#     list3 = []

#     for i in range(list1ength):
#         list1element = int (input(f"请输入列表1 的第 {i}个元素： "))
#         list1.append(list1element)

#     for i in range(list1ength):
#         list2element = int (input(f"请输入列表2 的第{i}元素： "))
#         list2.append(list2element)

#     for i in range(list1ength):
#         if list1[i] <= list2[i]:
#             list3.append(list1[i])
#             list3.append(list2[i])
#         else:
#             list3.append(list2[i])
#             list3.append(list1[i])
    
#     print (list3)




# 示例
# 假设我们有以下单链表：
# 节点 A (val = 1, next 指向节点 B)
# 节点 B (val = 2, next 指向节点 C)
# 节点 C (val = 3, next 指向 None)
# 链表的代码实现：
# python

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# # 创建链表 A → B → C
# node3 = ListNode(3)
# node2 = ListNode(2, node3)
# node1 = ListNode(1, node2)

# # 遍历链表
# current = node1
# while current:
#     print(current.val)
#     current = current.next
# 输出:
# 复制代码
# 1
# 2
# 3





# 假设我们有两个链表：
# 链表 1: 1 -> 2 -> 4
# 链表 2: 1 -> 3 -> 4
# 我们的目标是将它们合并成一个有序链表。
# 过程图示
# 步骤 1: 创建一个虚拟节点 dummy 并设置 current 指针指向它。dummy 节点是为了简化合并操作，最终的合并链表将从 dummy.next 开始。

# sql
# 复制代码
# dummy → None
# current → dummy
# 步骤 2: 比较两个链表的当前节点值，1 和 1。我们选择 list1 的 1，将其链接到 current.next。然后移动 current 到下一个节点，并移动 list1 到下一个节点。

# rust
# 复制代码
# dummy → 1 → None
# current → 1
# list1: 2 -> 4
# list2: 1 -> 3 -> 4
# 步骤 3: 继续比较 list1 的 2 和 list2 的 1。选择 list2 的 1，链接到 current.next。然后移动 current 到下一个节点，并移动 list2 到下一个节点。

# rust
# 复制代码
# dummy → 1 → 1 → None
# current → 1
# list1: 2 -> 4
# list2: 3 -> 4
# 步骤 4: 比较 list1 的 2 和 list2 的 3。选择 list1 的 2，链接到 current.next。然后移动 current 到下一个节点，并移动 list1 到下一个节点。

# makefile
# 复制代码
# dummy → 1 → 1 → 2 → None
# current → 2
# list1: 4
# list2: 3 -> 4
# 步骤 5: 比较 list1 的 4 和 list2 的 3。选择 list2 的 3，链接到 current.next。然后移动 current 到下一个节点，并移动 list2 到下一个节点。

# makefile
# 复制代码
# dummy → 1 → 1 → 2 → 3 → None
# current → 3
# list1: 4
# list2: 4
# 步骤 6: 比较 list1 的 4 和 list2 的 4。选择 list1 的 4，链接到 current.next。然后移动 current 到下一个节点，并移动 list1 到下一个节点。

# sql
# 复制代码
# dummy → 1 → 1 → 2 → 3 → 4 → None
# current → 4
# list1: None
# list2: 4
# 步骤 7: list1 已经空了，只剩下 list2 的 4。将 list2 的剩余部分连接到 current.next。

# sql
# 复制代码
# dummy → 1 → 1 → 2 → 3 → 4 → 4 → None
# current → 4
# list1: None
# list2: None
# 最终结果
# 合并后的链表从 dummy.next 开始：

# 复制代码
# 1 → 1 → 2 → 3 → 4 → 4