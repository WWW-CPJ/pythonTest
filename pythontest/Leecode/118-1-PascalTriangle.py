# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:   # generate  产生，生成
        # 初始化杨辉三角,初始化一个空列表，用于存储杨辉三角的每一行。
        triangle = []   # triangle 三角形

        # 生成每一行
        for i in range(numRows):
            # 创建当前行的初始状态，每行都有i+1 个元素
            row = [1] *(i +1)

            # 每一行除了第一个和最后一个元素，其他的元素需要根据上一行进行计算
            for j in range (1, i):
                row [j] = triangle[i-1][j-1] + triangle[i-1][j]

            # 将生成的行添加到杨辉三角中
            triangle.append(row)
        return triangle
    
objectSolution = Solution()
print (objectSolution.generate(5))