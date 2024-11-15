def main():
    array=[]
    target = int(input("输入目标数字： "))
    size = int(input("输入数组长度： "))

    for i in range(size):
        element = int(input(f"输入第{i}个元素： "))
        array.append(element)
    print("输入的数组为： ", array)
    
    function()


def function():
    found = False
    for i in range(0,size,1):
        for j in range(i+1,size,1):  # j 从 i+1 开始，避免重复检查同一对元素
            if (array[i] + array[j] == target):
                # if 后面的条件，如果只有一个，可以不用括号，如果超过一个，要用括号
                print(f"array{[i]} + array{[j]} = {target}")
                # found = True
                continue

function()

# Traceback (most recent call last):
#   File "c:\VScode\pythontest\Leecode\1-sum of numbers.py", line 23, in <module>
#     function()
#   File "c:\VScode\pythontest\Leecode\1-sum of numbers.py", line 19, in function
#     if found == True:
#        ^^^^^
# UnboundLocalError: cannot access local variable 'found' where it is not associated with a value
# UnboundLocalError（未绑定局部变量错误）是Python中的一种错误，通常发生在尝试在当前作用域内访问一个变量之前，该变量尚未被定义或赋值的情况下。

# 这种错误通常出现在以下情况：
# 当一个变量在函数或方法的局部作用域内被使用之前，没有在所有可能的执行路径中被赋值时。
# 例如，在一个条件语句中，变量只有在某些条件下才会被赋值，但在其他条件下没有被赋值。
# 为了解决这个错误，你需要确保在尝试访问变量之前，它在当前作用域内已经被定义和赋值。通常的做法是在函数或方法的开始处初始化变量，以一个默认值，例如 False 或 None。
# def example_function():
#     found = False  # 初始化 'found' 变量
#     if some_condition:
#         found = True
#     if found:  # 现在 'found' 已经被定义和赋值
#         print("找到变量为 True.")

# example_function()


# target = int(input("请输入target: "))
#     # 定义一个空的列表
# array=[]
#     # 获取用户输入的数组大小
# size = int(input("请输入数组的大小: "))
#     # 获取用户为数组元素输入的具体值
# for i in range(size):
#     element = input(f"请输入第{i+1}个元素的值: ")
#         # 将输入的值转换为整数（如果需要的话）
#     array.append(int(element)) if element.isdigit() else array.append(element)
#     # 打印输入的数组
# print("您输入的数组是: ", array)

# def function():
#     for i in range(0,size,1):
#         for j in range(i+1,size,1):
#             if (array[i] + array[j] == target):
#                 # if 后面的条件，如果只有一个，可以不用括号，如果超过一个，要用括号
#                 print(f"array{[i]} + array{[j]} = {target}")
#             else:
#                 print(f"array{[i]} + array{[j]} != {target}")
#                 continue
#             continue
#         continue
#     return 
# function()
