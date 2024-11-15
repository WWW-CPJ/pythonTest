def is_valid() -> bool:

    #定义一个字典，键为右括号，值为对应的 左括号
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    # 初始化一个空栈
    stack = []

    # 获取用户输入。
    strs = input("请输入括号：").strip()
    
    x = len(strs)
    if x % 2 == 1:
        print ("括号个数为奇数，不是有效括号")
        return  False

    # 遍历字符串中的每个 字符
    for char in strs:
        if char in bracket_map.values():
            # 如果是左括号，压入栈中,char in bracket_map.values(): 检查当前字符 char 是否是字典 bracket_map 的值之一。bracket_map.values() 返回所有的左括号字符（如 '(', '[', '{'）。
            # stack.append(char): 如果 char 是左括号，则将它压入栈 stack 中。栈用于记录左括号，以便后续检查右括号时进行匹配。
            stack.append(char)
        elif char in bracket_map.keys():
            # 如果是右括号，检查栈是否为空或者栈顶元素是否匹配
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return False
        else:
            # 如果字符不是括号，按需处理
            print("输入的字符串包括非括号字符")
            return False
    # 如果栈为空，说明所有左括号 都有对应的右括号
    return not stack
    # if not stack:
    #     print("括号有效")
    #     return True
    # else:
    #     print("括号不匹配")
    #     return False

# 主程序 执行
if __name__ == "__main__":
    if is_valid():
        print("括号有效")
    else:
        print("括号无效")

# char in bracket_map.keys(): 检查当前字符 char 是否是字典 bracket_map 的键之一。bracket_map.keys() 返回所有的右括号字符（如 ')', ']', '}'）。
# stack and stack[-1] == bracket_map[char]:
# stack: 确保栈不为空。这是因为如果栈为空，表示没有相应的左括号可供匹配。
# stack[-1] == bracket_map[char]: 检查栈顶的元素是否与当前的右括号 char 对应的左括号匹配。bracket_map[char] 是与右括号 char 对应的左括号。
# stack.pop(): 如果匹配成功，移除栈顶的左括号，因为当前右括号与它匹配。


# 字典初始化: bracket_map 现在明确地映射了右括号到左括号的关系。
# 处理输入: 使用 input().strip() 确保处理了可能存在的首尾空白字符。
# 字符检查: 只有括号字符才会被处理，其他字符会被忽略。

# is_valid()

'''
疑难点：
栈
字典的相关操作'''

'''
代码解释
字典 bracket_map 用来映射每种右括号到其对应的左括号。
栈 stack 用来存储未匹配的左括号。
在遍历过程中，如果遇到左括号，则将其压入栈中；如果遇到右括号，则从栈中弹出一个元素并检查是否匹配。
最后检查栈是否为空，如果为空则说明括号匹配成功，否则说明字符串无效。'''


'''
是的，`stack` 在你的代码中是一个 Python 列表（`list`）。在 Python 中，列表可以用作栈，因为它支持在末尾添加（`append`）和删除（`pop`）元素，这些操作与栈的基本操作（后进先出）一致。

### 栈的基本操作

- **入栈(Push)**: 使用 `append` 方法将元素添加到栈的末尾。相当于将元素推入栈中。
- **出栈(Pop)**: 使用 `pop` 方法从栈的末尾移除并返回元素。相当于从栈中弹出最上面的元素。
- **查看栈顶元素**: 通过访问 `stack[-1]` 获取栈顶的元素，但不移除它。 

### 在代码中的使用

在你的代码中，`stack` 用作存储括号的栈。具体来说：

- 当遇到左括号时，`stack.append(char)` 将其压入栈中。
- 当遇到右括号时，`stack.pop()` 从栈中移除栈顶的左括号，并检查是否与当前右括号匹配。

### 示例代码

这里是一个简单的示例，演示如何使用列表作为栈：

```python
stack = []

# 入栈操作
stack.append('(')
stack.append('[')
stack.append('{')

print(stack)  # 输出: ['(', '[', '{']

# 出栈操作
top_element = stack.pop()
print(top_element)  # 输出: '{'
print(stack)  # 输出: ['(', '[']
```

### 总结

在 Python 中，列表非常适合用作栈数据结构，因为它提供了必要的 `append` 和 `pop` 方法来实现栈的基本操作。这使得列表成为实现栈操作的自然选择。
'''

'''
https://blog.csdn.net/weixin_47667133/article/details/112611610?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522172420408016800172510090%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=172420408016800172510090&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-1-112611610-null-null.142^v100^pc_search_result_base1&utm_term=%E6%A0%88%E5%92%8C%E9%98%9F%E5%88%97%E4%BB%A5%E5%8F%8A%E9%93%BE%E8%A1%A8&spm=1018.2226.3001.4187

'''