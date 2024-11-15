# Majority element  多数元素
# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# frequency  出现次数,频率

# 使用哈希函数 会很简单 
import collections
from typing import List


class Solution:
    def max_majorityElement(self, nums: List[int]) -> int:
        # 哈希表
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

# collections.Counter 是 Python 标准库 collections 模块中的一个类，用于计算可哈希对象的出现次数。
# Counter(nums) 创建一个 Counter 对象，nums 列表中每个元素的出现次数会被统计并存储在 counts 对象中。
# 例如，给定 nums = [3, 2, 3]，Counter(nums) 会返回 Counter({3: 2, 2: 1})，这表示数字 3 出现了 2 次，数字 2 出现了 1 次。

# counts.keys() 返回 Counter 对象中的所有键，即 nums 列表中的所有唯一元素。
# max(counts.keys(), key=counts.get) 计算所有键中，哪个键对应的计数值最大。
# key=counts.get 是一个用于 max 函数的关键字参数，它表示 max 函数应该根据 counts.get 的返回值来比较这些键。
# 例如，继续用上面的例子，counts.keys() 是 [3, 2]，counts.get 分别返回 3 和 1，因此 max(counts.keys(), key=counts.get) 会返回 3，因为 3 的计数是最大的。

# 假设 nums 是 [4, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]：
# Counter(nums) 的结果是 Counter({4: 4, 3: 3, 2: 2, 1: 1})。
# counts.keys() 是 [4, 1, 2, 3]。
# max(counts.keys(), key=counts.get) 遍历这些键，查找计数值：
# counts.get(4) 是 4
# counts.get(1) 是 1
# counts.get(2) 是 2
# counts.get(3) 是 3
# 所以 max 找到计数值最大的键是 4。
# 总结来说，return max(counts.keys(), key=counts.get) 的目的是在所有唯一元素中找出出现次数最多的那个元素。counts.get 是用于获取这些元素的计数值，从而使 max() 能够正确地比较并返回出现次数最多的元素。






        # 暴力解法
        # unique_nums = list(set(nums))
        # frequencies = []
        # for x in unique_nums:
        #     frequency = nums.count(x)
        #     frequencies.append(frequency)

        # maxfrequency = max(frequencies)
        
        # index_maxfrequency = frequencies.index(maxfrequency)
        # return unique_nums[index_maxfrequency]
    


nums = [2,2,1,1,1,2,2]
nums = [1,1,1,1,2,2,2,2]

objects = Solution()
print(objects.max_majorityElement(nums))