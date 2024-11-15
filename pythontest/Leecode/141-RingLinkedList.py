# Ring Linked List
# 给你一个链表的头节点 head ，判断链表中是否有环。
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
# 如果链表中存在环 ，则返回 true 。 否则，返回 false 。

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 初始化快指针和慢指针,将 slow 和 fast 指针都初始化为链表的头结点 head。
        slow = head
        fast = head

        # 遍历列表
        while fast and fast.next:
            slow = slow.next             # 慢指针每次移动一个节点
            fast = fast.next.next        # 快指针每次移动两个节点

            # 如果快慢指针相遇，说明 链表中有环
            # 相遇检测：如果链表有环，slow 和 fast 最终会在环中的某个节点相遇；如果链表没有环，fast 会到达 末尾，即null。
            if slow == fast:
                return True
            
        # 如果快指针到达链表的末尾，说明链表中没有环
        return False
    

# 时间复杂度：O(n)，其中 n 是链表的长度。每个节点最多被访问两次。
# 空间复杂度：O(1)，只使用了常量级别的额外空间。

head = [3, 2, 0, -4]
objectSolution = Solution()
print(objectSolution.hasCycle(head))