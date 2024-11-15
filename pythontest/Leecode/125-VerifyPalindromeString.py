# Verify palindrome string
# 如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。
# 字母和数字都属于字母数字字符。
# 给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_case_str = s.casefold()
        plain_string = re.sub(r'[^a-zA-Z0-9]', '', lower_case_str)
        # r'[^a-zA-Z0-9]' 是一个正则表达式模式，匹配所有非字母数字字符。
        # '' 表示用空字符串替换匹配到的字符。

        reverse_string = plain_string[::-1]
        if plain_string == reverse_string:
            return True
        else:
            return False

s = input("输入字符串： ")

objectSolution = Solution()
print(objectSolution.isPalindrome(s))




# 要移除字符串中所有非字母数字字符，可以使用 Python 的字符串方法和正则表达式。以下是几种不同的方法来实现这一功能：
# ### 方法 1: 使用正则表达式
# Python 的 `re` 模块可以用来匹配并移除字符串中的非字母数字字符。
# ```python
# import re
# def remove_non_alphanumeric(s: str) -> str:
#     return re.sub(r'[^a-zA-Z0-9]', '', s)

# # 示例
# s = "Hello, World! 123"
# result = remove_non_alphanumeric(s)
# print(result)  # 输出: HelloWorld123
# ```

# **解释**:
# - `re.sub(r'[^a-zA-Z0-9]', '', s)`:
#   - `r'[^a-zA-Z0-9]'` 是一个正则表达式模式，匹配所有非字母数字字符。
#   - `''` 表示用空字符串替换匹配到的字符。

# ### 方法 2: 使用字符串生成表达式
# 你可以通过字符串生成表达式来过滤掉非字母数字字符。
# ```python
# def remove_non_alphanumeric(s: str) -> str:
#     return ''.join(char for char in s if char.isalnum())

# # 示例
# s = "Hello, World! 123"
# result = remove_non_alphanumeric(s)
# print(result)  # 输出: HelloWorld123
# ```

# **解释**:
# - `char for char in s if char.isalnum()`:
#   - 生成一个只包含字母数字字符的生成器表达式。
#   - `''.join()` 将生成器表达式的结果连接成一个新的字符串。

# ### 方法 3: 使用 `str.translate` 和 `str.maketrans`
# Python 字符串的 `translate` 方法配合 `str.maketrans` 可以实现字符的删除。
# ```python
# def remove_non_alphanumeric(s: str) -> str:
#     # 创建一个翻译表，将所有非字母数字字符映射到 None
#     translation_table = str.maketrans('', '', ''.join(chr(i) for i in range(256) if not chr(i).isalnum()))
#     return s.translate(translation_table)

# # 示例
# s = "Hello, World! 123"
# result = remove_non_alphanumeric(s)
# print(result)  # 输出: HelloWorld123
# ```

# **解释**:
# - `str.maketrans('', '', ''.join(chr(i) for i in range(256) if not chr(i).isalnum()))`:
#   - 创建一个翻译表，将所有非字母数字字符映射到 `None`。
#   - `s.translate(translation_table)` 根据翻译表删除字符。

# ### 总结
# - **正则表达式** 是最灵活的方法，适用于复杂的模式匹配。
# - **字符串生成表达式** 提供了简洁且易于理解的解决方案。
# - **`str.translate`** 方法适合处理更大范围的字符集删除操作。
# 你可以根据具体的需求选择最合适的方法。