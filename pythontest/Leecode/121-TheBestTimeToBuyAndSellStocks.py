# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
# 题目解析：数组列表，选择两个元素，后面的减去前面的，差最大

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = float('inf')  # 初始化为无穷大,设定最小价格为正无穷大，以便在第一次遇到价格时更新。
        max_profit = 0
        
        # 对于每个价格，检查是否小于当前的 min_price，如果是，则更新 min_price。
        # 否则，计算当前价格与 min_price 的差值，检查这个差值是否大于 max_profit，如果是，则更新 max_profit。
        for price in prices:
            if price < min_price:
                min_price = price  # 更新最小价格
            elif price - min_price > max_profit:
                max_profit = price - min_price  # 更新最大利润
        
        return max_profit

# 这个优化后的代码避免了不必要的计算，时间复杂度为 𝑂(𝑛)O(n)，空间复杂度为 𝑂(1)O(1)，非常适合处理大数据集。

prices = []
length = int (input ("输入数组长度："))
for i in range(length):
    element = int (input(f"输入第 {i} 个元素： "))
    prices.append(element)
print (prices)

# prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]

objectSolution = Solution()
print (objectSolution.maxProfit(prices))




# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
        
#         length = len(prices)
#         if length <= 1:
#             return 0
#         else:
#             profit= []
#             for i in range(length):
#                 for j in range(i+1, length):
#                     poor = prices[j] - prices[i]
#                     profit.append(poor)

#             print (profit)   
#             if max(profit) <= 0:
#                 return 0
#             else:         
#                 return max(profit)