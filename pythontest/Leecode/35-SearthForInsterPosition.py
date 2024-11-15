# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
from typing import List
class Solution:
    # def searchFunction(self, nums:list(int), target: int) -> int:
    def searchFunction(self, nums:List[int], target: int) -> int: # type: ignore
        
        length = len(nums)
        for i in range(length):
            if nums[i] == target:
                print(f"目标值存在于数组中为 {nums[i]}，返回索引值为： {i}")
                return i 
        
        if target > nums[-1]:
            nums.append(target)
            i = len(nums) -1
        else:
            # if target not in nums:
            #     print("目标值不存在与数组中")
            for i in range(length):
                if target < nums[i]:
                    nums.insert(i, target)
                    break
            else:
                # 处理 target 比 nums 中所有元素都大的情况
                i = len(nums)

        print(f"新数组为：{nums}")
        return i


# 定义一个对象
searchObject = Solution()
# nums = [1, 3, 4, 5, 6, 8, 9]
# input 函数返回的是一个字符串类型，而不是列表类型
input_string = input("输入数组，以空格分割： ")
# 将字符串 input_string 按空格分隔，然后将每个部分转换为整数，最后将这些整数存储到列表中
nums = list(map(int, input_string.split()))

target = int(input("输入目标值： "))
index = searchObject.searchFunction(nums, target)
print(f"目标值插入位置为：{index}")


# 在 Python 中，arr[-1] 用于访问列表 arr 的最后一个元素。负索引在 Python 中提供了一种方便的方法来从列表的尾部进行索引。
# 负索引的工作原理
# arr[-1]：访问列表的最后一个元素。
# arr[-2]：访问倒数第二个元素，以此类推。
# 这种负索引的机制使得访问列表末尾的元素非常直观且简洁。


# # 定义一个字符串列表
# string_numbers = ['1', '2', '3', '4']
# # 使用 map 函数将每个字符串转换为整数
# int_numbers = list(map(int, string_numbers))
# print(int_numbers)  # 输出: [1, 2, 3, 4]
# map(int, string_numbers)：map 函数将 int 函数应用到 string_numbers 列表中的每个元素上，结果是一个迭代器，该迭代器生成转换为整数后的值。
# list(map(int, string_numbers))：将 map 函数返回的迭代器转换为列表，以便我们可以查看结果。
