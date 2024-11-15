# Find the index of the first match in a string
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。
#  stack - 堆    needle - 针   pointer - 指针
def function():
    haystack = str(input("请输入一个字符串： "))
    needle = str(input("请输入匹配目标字符： "))

    x = haystack.find(needle)
    print(x)
    return haystack.find(needle)
        
function()


# 暴力法
def strStr(haystack, needle):
    N = len(haystack)
    M = len(needle)
    for i in range(N - M + 1):
        if haystack[i:i+M] == needle:   # 截取字符串在匹配
            return i
    return -1


# KMP 算法是一种用于在字符串中查找子字符串的高效算法，具有线性时间复杂度。它通过构建部分匹配表（即失败函数）来避免重复比较。

# 算法步骤：
# 构建部分匹配表（或称为前缀表）：记录 needle 的前缀和后缀相同的最长部分的长度。
# 使用部分匹配表进行搜索：遍历 haystack 并使用部分匹配表加速匹配过程。
# 代码实现：
# python
# 复制代码
# def strStr(haystack: str, needle: str) -> int:
#     def build_lps(needle: str) -> list[int]:
#         lps = [0] * len(needle)
#         length = 0
#         i = 1
#         while i < len(needle):
#             if needle[i] == needle[length]:
#                 length += 1
#                 lps[i] = length
#                 i += 1
#             else:
#                 if length != 0:
#                     length = lps[length - 1]
#                 else:
#                     lps[i] = 0
#                     i += 1
#         return lps

#     m, n = len(haystack), len(needle)
#     if n == 0:
#         return 0
#     if m < n:
#         return -1
    
#     lps = build_lps(needle)
#     i = j = 0
#     while i < m:
#         if needle[j] == haystack[i]:
#             i += 1
#             j += 1
        
#         if j == n:
#             return i - j
#         elif i < m and needle[j] != haystack[i]:
#             if j != 0:
#                 j = lps[j - 1]
#             else:
#                 i += 1
#     return -1


# Rabin-Karp 算法是一种基于哈希的字符串匹配算法，适用于多模式匹配问题，具有平均线性时间复杂度。它通过计算字符串的哈希值来进行匹配。
# 算法步骤：
# 计算 needle 的哈希值。
# 在 haystack 中滑动窗口，计算每个窗口的哈希值，与 needle 的哈希值进行比较。
# 代码实现：
# python
# 复制代码
# def strStr(haystack: str, needle: str) -> int:
#     if not needle:
#         return 0
#     if len(haystack) < len(needle):
#         return -1
    
#     base = 256
#     mod = 101
#     needle_hash = 0
#     haystack_hash = 0
#     baseL = 1
#     n = len(needle)
#     m = len(haystack)
    
#     for i in range(n):
#         needle_hash = (base * needle_hash + ord(needle[i])) % mod
#         haystack_hash = (base * haystack_hash + ord(haystack[i])) % mod
#         if i < n - 1:
#             baseL = (baseL * base) % mod

#     for i in range(m - n + 1):
#         if needle_hash == haystack_hash:
#             if haystack[i:i + n] == needle:
#                 return i
#         if i < m - n:
#             haystack_hash = (base * (haystack_hash - ord(haystack[i]) * baseL) + ord(haystack[i + n])) % mod
#             if haystack_hash < 0:
#                 haystack_hash += mod
#     return -1