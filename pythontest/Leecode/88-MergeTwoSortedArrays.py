def function():
    nums1 = []
    nums2 = []

    x = int (input("请输入列表1的元素数目: "))
    for i in range (x):
        element = int(input(f"请输入第{i+1}个元素: "))
        nums1.append(element)
    print(nums1)

    y = int(input("请输入列表2的元素数目: "))
    for i in range (y):
        element = int (input(f"请输入第{i+1}个元素： "))
        nums2.append(element)
    print(nums2)

    m = int (input("请输入列表1的有效元素数目: "))
    n = int (input("请输入列表2的有效元素数目: "))

    # 解决方案
    # class Solution:
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    # 初始化指针，指向 nums1 和 nums2 的末尾
    i = m-1    # 指向 nums1 中有效元素的末尾
    j = n-1    # 指向 nums2 的末尾
    k = m+n-1  # 指向 nums1 的末尾

    # 从后向前合并 nums1 和 nums2
    while i >=0 and j >=0:         # nums1 和 nums2 都不为空
        if nums1[i] > nums2[j]:    # 如果 nums1 的元素大于 nums2 的元素， 将 nums1 的元素放到合适的位置
            nums1[k] = nums1[i]    # 比较 列表最末尾的元素，谁大（就是两个列表 最大）就放到 合并后的列表 nums1 的最末尾
            i-=1                   # 移动 nums1 的指针，倒数第二个元素，继续比较
        else:
            nums1[k] = nums2[j]    # 如果 nums2 的元素大于 nums1 的元素， 将 nums2 的元素放到合适的位置
            j-=1                   # 移动 nums1 的指针，倒数第二个元素，继续比较
        k-=1                       # 移动合并列表的指针

    # 如果 nums2 中还有剩余元素，将他们拷贝到 nums1 的前面
    while j >= 0:
        nums1[k] = nums2[j]        # 将 nums2 的元素放到合适的位置
        j-=1
        k-=1

        # 注意， 不需要处理 nums1 中剩下的元素 ，他们已经在正确的位置上



# sorted(iterable, *, key=None, reverse=False)
# irerable  : 必需，需要排序的可迭代对象
# Key : 可选。一个函数，用于从每个元素中提取一个用于比较的值。默认为 None，即直接比较元素本身。
# Reverse : 可选，布尔值，如果为 true，则降序排序。默认值为 false，按照升序排序
# sorted  方法是python 内置的一个 函数，用于可迭代对象，（列表，元组，字符串等）进行排序。它会返回一个 新的列表，其中 包含排序后的元素，原始的可迭代对象不会被 修改。



# 初版
# def function():
#     nums1 = []
#     nums2 = []
#     m = int (input("请输入列表1的元素数目: "))
#     for i in range (m):
#         element = int(input(f"请输入第{i+1}个元素: "))
#         nums1.append(element)
#     print(nums1)
#     n = int(input("请输入列表2的元素数目: "))
#     for i in range (n):
#         element = int (input(f"请输入第{i+1}个元素： "))
#         nums2.append(element)
#     print(nums2)
#     # 如果存在空表，直接返回另外一个非空表
#     if m==0 and n==0:
#         return []
#     elif m == 0:
#         return nums2
#     elif n==0:
#         return nums1
#     # 如果存在 0 ，移除列中的0
#     nums1 = [x for x in nums1 if x != 0]
#     nums2 = [x for x in nums2 if x != 0]
#     # 合并两个列表并排序
#     nums3 = sorted(nums1 + nums2)
#     # 另一种方法
#     nums1 = nums1 + nums2
#     nums1.sort()    
#     print ("输出处理后的列表 nums1: ", nums1)
#     print ("输出处理后的列表 nums2: ", nums2)
#     print ("输出合并后的列表 nums3: ", nums3)
#     return nums3