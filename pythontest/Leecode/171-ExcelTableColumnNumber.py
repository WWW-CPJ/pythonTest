# excel 表列序号
# 给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回 该列名称对应的列序号 。

# 例如：

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
# https://leetcode.cn/problems/excel-sheet-column-number/description/
# 不会
# 关联题目 168

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # 初始化结果变量
        result = 0
        # 遍历字符串中的每个字符
        for char in columnTitle:
            # 计算当前字符的值，计算字符 char 距离 A 的偏移量，+1 是因为 A 对应 1
            value = ord(char) - ord('A') + 1
            # 更新结果：之前的结果乘以26加上当前字符的值，乘以 26 是因为 Excel 列是基于 26 的。然后加上当前字符的值来更新结果。
            result = result * 26 + value
        return result
    

# 要将 Excel 列名称（如 A, B, Z, AA, AB 等）转换为列序号（即 A -> 1, B -> 2, AA -> 27），可以将 Excel 列名称视作一个 26 进制数来处理。每个字符表示一个基于 26 的数字，但与传统的 26 进制不同的是，Excel 列名称从 1 开始而不是 0。因此，A 表示 1，B 表示 2，...，Z 表示 26，AA 表示 27。

# 详细步骤
# 字符映射：

# 字符 A 对应 1，B 对应 2，...，Z 对应 26。
# 可以通过 ord(char) - ord('A') + 1 来得到字符 char 的对应值。
# 列名称处理：

# 从字符串的右端开始处理，每个字符的值乘以 26 的相应次幂，然后将结果累加到总数中。
# 示例
# 对于列名称 AB：
# A 在 26^1 的位置，B 在 26^0 的位置。
# 计算步骤：
# A 的值是 1，位置是 26^1，所以 A 的贡献是 1 * 26^1。
# B 的值是 2，位置是 26^0，所以 B 的贡献是 2 * 26^0。
# 总数是 26 + 2 = 28。