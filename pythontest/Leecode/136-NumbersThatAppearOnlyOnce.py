# 给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # # 暴力解法
        # for x in nums:
        #     if nums.count(x) <=1:
        #         return x        

        # 异或运算符： ^
        result = 0
        for num in nums:
            result = result ^ num
        return result

# a ^ 0 = a
# a ^ a = 0

# 初始化:
# result = 0
# 遍历和计算: 十进制数字转换为二进制，再转为十进制
# result = 0 ^ 4 = 4 （当前结果是 4）
# result = 4 ^ 1 = 5 （当前结果是 5）
# result = 5 ^ 2 = 7 （当前结果是 7）
# result = 7 ^ 1 = 6 （当前结果是 6）
# result = 6 ^ 2 = 4 （当前结果是 4）
# 结果:
# 最终 result 的值是 4，即唯一出现一次的数字。

nums = [2,2,1]
nums = [4,1,2,1,2]
nums = [1]
objectSolution = Solution()
print(objectSolution.singleNumber(nums))    



# 异或运算（XOR，"exclusive OR"）是一种位运算，用于对二进制位进行逻辑运算。异或运算符的主要特点是：
# 相同的位：如果两个位相同，结果为 0。
# 不同的位：如果两个位不同，结果为 1。
# 在Python中，异或运算使用 ^ 符号表示。例如：

# a = 5  # 二进制: 0101
# b = 3  # 二进制: 0011
# result = a ^ b  # 结果是 6，二进制: 0110

# 异或运算的性质
# 自反性:
# a ^ a = 0
# 对同一个数进行异或运算，结果为 0。
# 交换律:
# a ^ b = b ^ a
# 异或运算的顺序可以交换。
# 结合律:
# (a ^ b) ^ c = a ^ (b ^ c)
# 异或运算的顺序可以组合。
# 与0的运算:
# a ^ 0 = a
# 任意数与 0 进行异或运算，结果是该数本身。



# 常见应用

# 交换两个变量的值:
# 使用异或运算可以在不使用额外变量的情况下交换两个变量的值。

# a = 5
# b = 3

# a = a ^ b
# b = a ^ b
# a = a ^ b

# print(a)  # 输出: 3
# print(b)  # 输出: 5


# 查找只出现一次的数字:
# 在一个数组中，所有数字出现两次，只有一个数字出现一次。使用异或运算可以找到这个唯一的数字。

# def singleNumber(nums):
#     result = 0
#     for num in nums:
#         result ^= num
#     return result

# nums = [4, 1, 2, 1, 2]
# print(singleNumber(nums))  # 输出: 4
# 解释:
# 通过对所有数字进行异或操作，相同的数字会被消除，只留下那个唯一出现一次的数字。

# 检查数字是否是2的幂:
# 如果一个数字 n 是2的幂，它与 n-1 进行异或运算的结果会是 0。

# def isPowerOfTwo(n):
#     return n > 0 and (n & (n - 1)) == 0

# print(isPowerOfTwo(16))  # 输出: True
# print(isPowerOfTwo(18))  # 输出: False
# 解释:
# 通过 n & (n - 1) 可以检查 n 是否是2的幂。因为2的幂的二进制表示只有一个 1，n-1 的二进制表示所有比 n 中 1 右边的位都是 1，所以 n & (n - 1) 结果是 0。