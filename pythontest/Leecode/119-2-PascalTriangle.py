# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        
        for i in range(rowIndex+1):
            row = [1] * (i+1)

            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]

            triangle.append(row)
        return triangle[rowIndex]
    
objectSolution = Solution()
print (objectSolution.getRow(4))