# Remove duplicates from a sorted array
# 一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。
# https://leetcode.cn/problems/remove-duplicates-from-sorted-array/description/

def function():
    length = int (input("请输入数组长度： "))
    nums = []
    for i in range(length):
        element = int (input(f"请输入第{i}个元素: "))
        nums.append(element)
        
    i=1
    while i < len(nums):
        if nums[i] == nums[i-1]:
                nums.pop(i)           # remove 方法会改变列表的长度，使得循环逻辑可能访问无效的索引。
        else:
             i +=1      # 只有在没有移除元素时才移动到下一个元素
                        # 使用 while 循环代替 for 循环。这是因为 while 循环可以灵活处理删除操作后的位置调整。
                        # 当找到相邻重复元素时，使用 pop(i) 删除当前元素。如果删除了元素，i 不递增，因为删除后当前索引 i 的位置需要重新检查。
                        # 如果没有删除元素，则递增 i，以检查下一个元素。
    print (nums)
    print(len(nums))
    return nums

function()