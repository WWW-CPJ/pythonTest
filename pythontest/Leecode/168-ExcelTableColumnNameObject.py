# ord('A')  获取 A 的ASCII码

# 给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。
# 例如：
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
# 关联题目, 171-Excel 表列序号

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber > 0:
            # 计算当前位的字符 (1-indexed)
            columnNumber -= 1
            result.append(chr(columnNumber % 26 + ord('A')))
            # 更新 columnNumber
            columnNumber //= 26

        # 反转字符串,因为我们是从后往前构造的列表
        return ''.join(result[::-1])
    
objects = Solution()
print (objects.convertToTitle(1))
print (objects.convertToTitle(28))
print (objects.convertToTitle(701))
print (objects.convertToTitle(2147483647))

# 转换的过程类似于将整数转换为26进制，但与通常的26进制不同的是，这里从1开始而不是0

# 算法思路
# 初始化一个空的字符串：用来存储最终的列名称。
# 循环直到 columnNumber 为0：
# 计算当前的列字母：columnNumber 减去 1，得到一个从0开始的值，然后对26取模，这样可以找到当前位的字符。
# 使用 chr 函数将计算得到的值转换为字符。
# 将这个字符加到结果字符串的开头。
# 更新 columnNumber：使用整数除法（//）更新 columnNumber。


# 解释
# columnNumber -= 1：因为 Excel 的列名称是从1开始的，而数字系统是从0开始的，所以我们先减去1，以便处理0到25范围的字符。
# chr(columnNumber % 26 + ord('A'))：计算当前列的字符。ord('A') 返回字母 'A' 的 ASCII 码，columnNumber % 26 返回列的字母索引（0 到 25），然后加上 ord('A') 得到对应的字符。
# columnNumber //= 26：更新 columnNumber，准备处理下一个字符。
# ''.join(result[::-1])：因为我们是从列名的最低位开始构造的，所以需要反转结果列表得到正确的列名。
#     result[::-1]：
#     result[::-1] 是一种 Python 切片操作，用于反转列表。这里的 [::-1] 表示从列表的末尾到开头，以步长为 -1 进行切片，从而得到一个反转后的列表。
#     ''.join(result[::-1])：
#     ''.join() 是一个字符串方法，用于将一个可迭代对象（如列表）中的元素连接成一个字符串。''.join() 以空字符串作为分隔符将列表中的字符连接起来。

