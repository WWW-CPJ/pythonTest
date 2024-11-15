# 定义一个链表节点类：'ListNode'
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 定义一个链表加法函数 来计算两个链表的和：
def add_two_numbers(l1, l2):
    # 创建一个虚拟头节点来简化处理
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0
    
    # 遍历两个链表
    while l1 or l2 or carry:
        # 获取当前位的值
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # 计算当前位的和
        total = val1 + val2 + carry
        
        # 更新进位
        carry = total // 10
        
        # 更新当前位的值
        current.next = ListNode(total % 10)
        
        # 移动到下一个节点
        current = current.next
        
        # 移动到下一个链表节点
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next

# 测试代码是否正常工作：
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# 构造两个链表：2 -> 4 -> 3 (表示数字 342)
l1 = ListNode(2, ListNode(4, ListNode(3)))

# 构造第二个链表：5 -> 6 -> 4 (表示数字 465)
l2 = ListNode(5, ListNode(6, ListNode(4)))

# 计算两个链表的和
result = add_two_numbers(l1, l2)

# 打印结果链表：7 -> 0 -> 8 (表示数字 807)
print_list(result)

# 代码解释
# 定义一个链表节点类，并编写一个函数来处理链表的加法运算。
# 我们假设链表节点包含一个 val 属性表示节点的值和一个 next 属性表示下一个节点
# ListNode 类：表示链表节点，包含 val 和 next 属性。
# add_two_numbers 函数：
# dummy_head：虚拟头节点，用于简化链表操作。
# current：指向当前节点，用于构建结果链表。
# carry：保存进位。
# 遍历两个链表：逐位计算和，并处理进位。
# dummy_head.next：返回结果链表的头节点。
# print_list 函数：打印链表内容，帮助验证结果。
# 这个实现通过逐位加法处理两个链表，并且处理了进位的情况。它返回的是表示和的链表，节点的值按照逆序存储。