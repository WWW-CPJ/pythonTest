def function ():
    array = []
    target = int(input("请输入数组长度："))
    lengthList = []
    letterList = []

    for i in range(target):
        element = str(input(f"请输入第{i}个元素:"))
        array.append(element)
        length = len(element)
        lengthList.append(length)
    print(f"输出array为: {array}")
    print(f"输出lengthList为: {lengthList}")
    print(f"输出字符最短长度为: {min(lengthList)}")

    num = min(lengthList)

    # for j in range(num):    从小到大遍历
    for j in range(num-1,-1,-1):     # 从大到小遍历
        letterList = []
        for i in range(target):
            if len(array[i]) > j:
                x = array[i][0:j+1:1]
                letterList.append(x)

        letter_set = set(letterList)
        print (letter_set)
        if len(letter_set) == 1:
            print(f"最长公共前缀为：{letter_set}")
            return letter_set.pop()
        # pop  删除 集合唯一的元素
        else:
            continue
    return ""
function()





def get_first_letter(s):
    if not s:
        return ""  # 空字符串的情况
    return s[0]

# 示例
print(get_first_letter("Hello"))  # 输出: H
print(get_first_letter("world"))  # 输出: w
print(get_first_letter(""))       # 输出: ""

def find_minimum(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    return min(numbers)

# 示例
numbers = [5, 3, 9, 1, 6]
print(find_minimum(numbers))  # 输出: 1

'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        listlength = len(strs)
        lengthList = [len(x) for x in strs]
        num = min(lengthList)

        for j in range(num-1,-1,-1):
            letterList = []
            for i in range(listlength):
                if len(strs[i]) > j:
                    x= strs[i][0:j+1:1]
                    letterList.append(x)
            letter_set = set(letterList)
            if len(letter_set) == 1:
                return letter_set.pop()
        return ""
'''


'''
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    
    # 取第一个字符串作为参考
    prefix = strs[0]
    
    for s in strs[1:]:
        # 更新前缀
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

# 示例
strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))  # 输出: "fl"

'''