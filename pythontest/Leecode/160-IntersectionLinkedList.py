# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional [ListNode]:
        if not headA or not headB:
            return None
        
        # 初始化两个指针
        ptr1, ptr2 = headA, headB

        # 遍历两个列表
        while ptr1 != ptr2:
            # 如果到达链表末尾，转到另一个链表的头节点
            ptr1 = ptr1.next if ptr1 else headB
            ptr2 = ptr2.next if ptr2 else headA

        # ptr1 和 ptr2 会在交点相遇。或者都为 None(无交点)
        return ptr1
    
#     双指针法的思路
# 初始化两个指针：分别指向两个链表的头节点。
# 遍历两个链表：
# 当两个指针不相等时，它们会分别遍历各自的链表。如果一个指针到达链表末尾，则将其指向另一个链表的头节点。
# 这样，当两个指针遍历了两个链表后，它们就会在相交的节点相遇，或者都达到链表末尾（即都为 None）。

# 初始化：
# ptr1 和 ptr2 分别指向链表 headA 和 headB 的头节点。
# 循环：
# 如果 ptr1 和 ptr2 不相等，它们会继续向下遍历。如果某个指针到达链表末尾，就转到另一个链表的头节点。
# 这种方法确保两个指针会遍历两个链表的总长度，因此它们会在交点处相遇（如果有交点），或者在链表末尾处同时变为 None。
# 返回结果：
# 当 ptr1 和 ptr2 相等时，返回该节点作为交点；如果都为 None，则表示两个链表没有交点，返回 None。