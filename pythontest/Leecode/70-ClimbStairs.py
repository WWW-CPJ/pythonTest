# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

class Solution:
    def climbStairs(self, n: int) -> int:
        # 边界条件
        if n == 0:
            return 0 
        if n == 1:
            return 1
        
        # 初始化dp 数组
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
         
        #  填充 DP 数组
        for i in range(2,n+1):
            dp[i] = dp [i-1] + dp [i-2]
        print (dp[n])
        return dp[n]
    
n = int(input("输入整数 n : "))
objectSolution = Solution()
objectSolution.climbStairs(n)
        
# 这个问题是经典的动态规划问题，也可以使用递归解决，但动态规划方法通常效率更高。在这个问题中，我们需要计算到达第 n 阶楼梯的方法数量，其中每次可以爬 1 或 2 个台阶。
# 解决方法
# 动态规划
# 我们可以使用动态规划来解决这个问题。设 dp[i] 为到达第 i 阶的方法数。显然，到达第 i 阶的方式有两种：
# 从第 i-1 阶跳 1 阶。
# 从第 i-2 阶跳 2 阶。
# 因此，状态转移方程为： dp[i]=dp[i−1]+dp[i−2]
# 其中，dp[0] 表示 0 阶楼梯的方式数，为 1（假设不需要爬任何台阶就是一种方法），dp[1] 表示 1 阶楼梯的方式数，为 1（只能一步到达）。