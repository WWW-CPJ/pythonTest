# 给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
# 二进制转为十进制，求和，再转为二进制

class Solution:
    def addBinary(self, a:str, b:str) -> str:
        # 将二进制字符串 转换为整数，指定为二进制（不指定则默认为十进制）
        int_a = int(a, 2)
        int_b = int(b, 2)

        int_sum = int_a + int_b

        # 将和转换为二进制字符串，并去掉 字面量前缀 '0b' 
        binary_sum = bin(int_sum)[2:]
        print(binary_sum)
        return binary_sum


a = input("输入字符串a: ")
b = input("输入字符串b: ")
objectSoluction = Solution()
objectSoluction.addBinary(a, b)




# def function():
#     binary_stra = input("输入字符串a: ")
#     binary_strb = input("输入字符串b: ")

#     int_numbera = int(binary_stra)
#     int_numberb = int(binary_strb)

#     int_sum = int_numbera + int_numberb
#     binary_sum = bin(int_sum)
#     print(binary_sum)
# function()






# 二进制转换
# 将二进制数转换为十进制数是计算机科学中的一个基本操作。二进制是由 `0` 和 `1` 组成的数字系统，而十进制是我们日常生活中使用的数字系统。每个二进制位（bit）在其对应的位置上有一个权重，这个权重是 `2` 的幂。下面是将二进制数转换为十进制数的一般步骤和一个示例：

# ### 转换步骤

# 1. **标识每个位的权重**：
#    - 从右到左，每一位的权重是 `2` 的相应幂次。例如，二进制数的最右边的位是 `2^0`，下一个是 `2^1`，依此类推。

# 2. **计算每一位的值**：
#    - 将每一位的二进制数字与其对应的权重相乘。如果该位是 `1`，则计算其贡献；如果是 `0`，则该位的贡献为 `0`。

# 3. **将所有贡献值相加**：
#    - 把所有位的计算结果加在一起，就得到十进制数。

# ### 示例

# 假设你要将二进制数 `1011` 转换为十进制数：

# 1. **标识每个位的权重**：
#    - 从右到左，第一个位的权重是 `2^0`，第二个是 `2^1`，第三个是 `2^2`，第四个是 `2^3`。

#    ```
#    位:    3  2  1  0
#    二进制: 1  0  1  1
#    权重:  2^3 2^2 2^1 2^0
#    ```

# 2. **计算每一位的值**：
#    - 从右到左：
#      - 1（在 `2^0` 位）: `1 * 2^0 = 1`
#      - 1（在 `2^1` 位）: `1 * 2^1 = 2`
#      - 0（在 `2^2` 位）: `0 * 2^2 = 0`
#      - 1（在 `2^3` 位）: `1 * 2^3 = 8`

# 3. **将所有贡献值相加**：
#    - `1 + 2 + 0 + 8 = 11`

# 所以，二进制数 `1011` 对应的十进制数是 `11`。

# ### 公式

# 如果你有一个二进制数 `b_k b_{k-1} ... b_1 b_0`，其中 `b_i` 表示每一位的二进制数字（0 或 1），那么它转换成十进制数的公式是：

# \[ \text{Decimal} = b_k \cdot 2^k + b_{k-1} \cdot 2^{k-1} + \cdots + b_1 \cdot 2^1 + b_0 \cdot 2^0 \]

# ### 代码示例

# 在编程中，你可以使用内置函数来进行二进制到十进制的转换。例如，在 Python 中，你可以使用 `int()` 函数：

# ```python
# binary_str = "1011"
# decimal_number = int(binary_str, 2)
# print(decimal_number)  # 输出: 11
# ```

# 这个示例中，`int(binary_str, 2)` 函数将二进制字符串 `1011` 转换为十进制数 `11`。

# 通过这些步骤，你可以将任何二进制数转换为其十进制表示。





# decimal` 和 `int` 

# 在编程中，`decimal` 和 `int` 是两种不同的数据类型，它们在表示数字和进行数学运算时有不同的特性和用途。下面是这两种数据类型的详细介绍：

# ### `int`

# - **含义**：`int` 代表整数（Integer），是一种数据类型，用于表示没有小数部分的数字。
# - **范围**：在大多数编程语言中，`int` 的范围是有限的，取决于系统架构和语言的实现。例如，在许多语言中，`int` 的范围通常是 `-2,147,483,648` 到 `2,147,483,647`（32 位整数）。
# - **用途**：用于表示基本的整数值，如计数、索引、日期时间的计算等。
# - **示例**（Python）：
#   ```python
#   x = 10  # 这是一个整数
#   y = -3  # 负整数
#   ```

# ### `decimal`

# - **含义**：`decimal` 通常指代一种用于表示高精度数字的数据类型，特别是具有小数部分的数字。它通常用来处理需要高精度的数值计算，比如财务计算。
# - **特性**：
#   - **高精度**：`decimal` 类型可以避免浮点数运算中的舍入误差，提供更高的精度。
#   - **控制精度**：允许指定小数位数和舍入模式，适合需要严格精度控制的应用场景。
# - **实现**：
#   - 在 Python 中，`decimal` 是一个内置模块，提供了 `Decimal` 类型。
#   - 在其他编程语言（如 C#、Java）中也有类似的高精度小数数据类型，如 C# 中的 `Decimal` 类型。
# - **示例**（Python）：
#   ```python
#   from decimal import Decimal
  
#   a = Decimal('10.12345678901234567890')  # 高精度的十进制数
#   b = Decimal('2.5')
  
#   result = a + b  # 高精度加法
#   print(result)   # 输出: 12.62345678901234567890
#   ```

# ### 对比与用途

# - **精度**：
#   - `int` 类型只处理整数，不涉及小数部分。
#   - `decimal` 类型提供了高精度的浮点数表示，可以精确处理小数部分。

# - **应用场景**：
#   - `int` 适用于普通的整数计算，如计数、索引等。
#   - `decimal` 适用于需要高精度计算的场景，例如财务计算、科学计算等，特别是当你需要避免由于浮点数舍入误差带来的问题时。

# - **性能**：
#   - `int` 的计算通常比 `decimal` 更快，因为 `int` 是一种基本的数据类型。
#   - `decimal` 的计算可能会稍慢，因为它涉及到更多的精度控制和舍入规则。

# 在编程实践中，选择哪种数据类型取决于你需要处理的数据和精度要求。例如，处理金融数据时，使用 `decimal` 可以确保计算的准确性；而在一般的整数计算中，`int` 是足够且高效的。






# 十进制转换
# 将十进制数转换为其他进制（如二进制、八进制、十六进制）是编程和计算机科学中的常见操作。以下是如何将十进制数转换为不同进制的步骤及示例：

# ### 1. 十进制到二进制

# #### 步骤

# 1. **除以 2**：将十进制数除以 2，并记录下余数。
# 2. **记录商**：记录下除法的商。
# 3. **重复步骤**：将商再次除以 2，重复步骤 1 和 2，直到商为 0。
# 4. **构建结果**：将所有余数倒序排列，得到二进制数。

# #### 示例

# 将十进制数 `13` 转换为二进制：

# 1. `13 ÷ 2` = 6 余 1
# 2. `6 ÷ 2` = 3 余 0
# 3. `3 ÷ 2` = 1 余 1
# 4. `1 ÷ 2` = 0 余 1

# 将余数倒序排列，得到 `1101`，所以 `13` 的二进制表示是 `1101`。

# ### 2. 十进制到八进制

# #### 步骤

# 1. **除以 8**：将十进制数除以 8，并记录下余数。
# 2. **记录商**：记录下除法的商。
# 3. **重复步骤**：将商再次除以 8，重复步骤 1 和 2，直到商为 0。
# 4. **构建结果**：将所有余数倒序排列，得到八进制数。

# #### 示例

# 将十进制数 `83` 转换为八进制：

# 1. `83 ÷ 8` = 10 余 3
# 2. `10 ÷ 8` = 1 余 2
# 3. `1 ÷ 8` = 0 余 1

# 将余数倒序排列，得到 `123`，所以 `83` 的八进制表示是 `123`。

# ### 3. 十进制到十六进制

# #### 步骤

# 1. **除以 16**：将十进制数除以 16，并记录下余数（如果余数大于 9，用字母 A-F 表示）。
# 2. **记录商**：记录下除法的商。
# 3. **重复步骤**：将商再次除以 16，重复步骤 1 和 2，直到商为 0。
# 4. **构建结果**：将所有余数倒序排列，得到十六进制数。

# #### 示例

# 将十进制数 `254` 转换为十六进制：

# 1. `254 ÷ 16` = 15 余 14 (E)
# 2. `15 ÷ 16` = 0 余 15 (F)

# 将余数倒序排列，得到 `FE`，所以 `254` 的十六进制表示是 `FE`。

# ### 代码示例

# 在不同编程语言中，可以利用内置函数或方法来进行进制转换。例如：

# #### Python

# ```python
# # 十进制到二进制
# decimal_number = 13
# binary_string = bin(decimal_number)  # '0b1101'
# print(binary_string[2:])  # 输出: 1101

# # 十进制到八进制
# octal_string = oct(decimal_number)  # '0o15'
# print(octal_string[2:])  # 输出: 15

# # 十进制到十六进制
# hex_string = hex(decimal_number)  # '0xd'
# print(hex_string[2:])  # 输出: d
# ```

# #### JavaScript

# ```javascript
# // 十进制到二进制
# let decimalNumber = 13;
# let binaryString = decimalNumber.toString(2);  // '1101'
# console.log(binaryString);  // 输出: 1101

# // 十进制到八进制
# let octalString = decimalNumber.toString(8);  // '15'
# console.log(octalString);  // 输出: 15

# // 十进制到十六进制
# let hexString = decimalNumber.toString(16);  // 'd'
# console.log(hexString.toUpperCase());  // 输出: D
# ```

# 通过这些步骤和示例，你可以将十进制数转换为二进制、八进制、十六进制等不同的进制表示。






# 二进制字面量（binary literal）
# `0b10111` 不是普通的二进制字符串，而是一种特定的表示方法，用于在许多编程语言中表示二进制数。它是一种二进制字面量（binary literal）或二进制前缀表示法。

# ### 解释

# - **`0b` 前缀**：在许多编程语言中，`0b` 或 `0B` 前缀用于指示后面的数字是二进制数。它是二进制字面量的标记。
# - **`10111`**：这是二进制数的实际值，表示的是一个二进制数。

# ### 在不同编程语言中的用法

# #### Python

# 在 Python 中，`0b` 前缀用于定义二进制字面量：

# ```python
# binary_value = 0b10111  # 二进制的 10111
# print(binary_value)  # 输出: 23（十进制表示）
# ```

# 这里，`0b10111` 表示的二进制数 `10111` 转换成十进制是 `23`。

# #### JavaScript

# 在 JavaScript 中，`0b` 也是用来表示二进制数的：

# ```javascript
# let binaryValue = 0b10111;  // 二进制的 10111
# console.log(binaryValue);  // 输出: 23（十进制表示）
# ```

# 同样地，`0b10111` 转换成十进制是 `23`。

# #### Java

# 在 Java 中，二进制字面量的前缀也是 `0b`（从 Java 7 开始支持）：

# ```java
# public class Main {
#     public static void main(String[] args) {
#         int binaryValue = 0b10111;  // 二进制的 10111
#         System.out.println(binaryValue);  // 输出: 23（十进制表示）
#     }
# }
# ```

# ### 与普通二进制字符串的区别

# - **普通二进制字符串**：是用字符串的形式表示二进制数，例如 `'10111'`。这只是一个包含二进制数字的字符串，并不表示数值本身。

#   ```python
#   binary_string = '10111'
#   ```

#   如果你想将这个字符串转换为整数，需要使用额外的函数：

#   ```python
#   decimal_value = int(binary_string, 2)  # 将字符串 '10111' 转换为十进制数
#   print(decimal_value)  # 输出: 23
#   ```

# - **二进制字面量**：直接在代码中表示数值，使用前缀 `0b` 来指示它是一个二进制数，并且可以直接用于数值计算。

# ### 总结

# `0b10111` 是一种二进制字面量，用于在编程语言中直接表示二进制数。它与普通的二进制字符串（例如 `'10111'`）不同，后者只是一个字符串，需要通过转换函数才能得到实际的数值。





# int(a, 2)
# `int(a, 2)` 是 Python 中的一个内置函数，用于将一个字符串 `a` 解析为一个整数，且该字符串被视为一个指定进制（在这里是二进制）的数字。

# ### 解释

# - **`int()` 函数**：这是 Python 的内置函数，用于将一个数字或字符串转换为整数。它的基本用法是 `int(x)`，其中 `x` 是一个数字或字符串。
# - **第二个参数 `2`**：这是 `int()` 函数的一个可选参数，指定了字符串 `a` 使用的进制。在这种情况下，`2` 表示二进制进制。

# ### 语法

# ```python
# int(x, base)
# ```

# - **`x`**：要转换的字符串或数字。
# - **`base`**：指定 `x` 的进制（如果 `x` 是一个字符串）。范围是 `2` 到 `36`。

# ### 使用示例

# 假设 `a` 是一个二进制字符串 `'1011'`：

# ```python
# a = '1011'
# int_a = int(a, 2)  # 将二进制字符串 '1011' 转换为十进制整数
# ```

# #### 详细步骤

# 1. **解析字符串**：`int(a, 2)` 解析字符串 `'1011'`，将其视为二进制数。
# 2. **计算十进制值**：在二进制系统中，`1011` 代表的是：

#    \[
#    1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0
#    \]

#    计算结果是：

#    \[
#    8 + 0 + 2 + 1 = 11
#    \]

# 3. **返回值**：`int(a, 2)` 的结果是整数 `11`，它是二进制字符串 `1011` 对应的十进制值。

# ### 其他进制示例

# - **二进制（base 2）**：
#   ```python
#   int('1101', 2)  # 13
#   ```

# - **八进制（base 8）**：
#   ```python
#   int('17', 8)  # 15
#   ```

# - **十六进制（base 16）**：
#   ```python
#   int('1A', 16)  # 26
#   ```

# ### 总结

# - `int(a, 2)` 是一个用于将字符串 `a` 按二进制进制解释并转换为十进制整数的函数。
# - 它使得你可以轻松地将不同进制的数字字符串转换为标准的十进制整数，方便进行数学计算和进一步处理。