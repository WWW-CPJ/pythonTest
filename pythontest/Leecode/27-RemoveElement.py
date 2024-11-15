def function():
    nums = []
    length = int(input("请输入数组的长度： "))
    for i in range(length):
        element = int (input(f"请输入第{i+1}个元素： "))
        nums.append(element)

    value = int(input("请输入value的值: "))

#  remove  和 pop 删除元素后都会改变 列表的结构，长度发生改变，索引会引发错误，所以不用 for 循环和这两个方法
    i =0
    while i < len(nums):
        if nums[i] == value:
            nums.pop(i)
        else:
            i+=1
    print (nums)
    print (len(nums))
    return nums

function()