# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
import math
class Solution:
    def mySqrt(self, x: int) -> int:
        square_root = math.sqrt(x)
        print(int(square_root))
        return square_root




# import math
# def function():
#     x = int(input("输入一个非负整数: "))
#     square_root = math.sqrt(x)
#     print(int(square_root))
# function()







# 算术平方根是数学中的一个基本概念，指的是一个非负实数的平方根。具体来说，给定一个非负实数 \( x \)，其算术平方根是一个非负实数 \( y \)，使得 \( y^2 = x \)。

# ### 计算算术平方根

# 有多种方法可以计算一个数的平方根，以下是一些常见的方法：

# #### 1. **数学公式**

# 平方根可以通过数学公式来计算。对于任意非负数 \( x \)，其平方根 \( \sqrt{x} \) 是满足 \( y^2 = x \) 的非负数 \( y \)。

# #### 2. **编程语言中的计算**

# 许多编程语言提供了内置函数或方法来计算平方根。以下是一些常见编程语言中的示例：

# - **Python**:
#   使用 `math` 模块的 `sqrt()` 函数：
#   ```python
#   import math

#   number = 16
#   square_root = math.sqrt(number)
#   print(square_root)  # 输出: 4.0
#   ```

#   你也可以使用 `**` 运算符：
#   ```python
#   number = 16
#   square_root = number ** 0.5
#   print(square_root)  # 输出: 4.0
#   ```

# - **JavaScript**:
#   使用 `Math.sqrt()` 方法：
#   ```javascript
#   let number = 16;
#   let squareRoot = Math.sqrt(number);
#   console.log(squareRoot);  // 输出: 4
#   ```

# - **Java**:
#   使用 `Math.sqrt()` 方法：
#   ```java
#   public class Main {
#       public static void main(String[] args) {
#           double number = 16;
#           double squareRoot = Math.sqrt(number);
#           System.out.println(squareRoot);  // 输出: 4.0
#       }
#   }
#   ```

# - **C#**:
#   使用 `Math.Sqrt()` 方法：
#   ```csharp
#   using System;

#   class Program {
#       static void Main() {
#           double number = 16;
#           double squareRoot = Math.Sqrt(number);
#           Console.WriteLine(squareRoot);  // 输出: 4.0
#       }
#   }
#   ```

# #### 3. **手动计算方法**

# 平方根也可以通过手动方法计算，例如牛顿法（Newton's method）或其他数值计算算法，但通常在编程中使用内置函数更为方便和精确。

# ### 处理负数

# 平方根的计算只适用于非负数。如果尝试计算负数的平方根，结果会是一个复数。例如，平方根函数在复数域中可以扩展以处理负数，但在标准的实数运算中，负数没有实数平方根。

# ### 总结

# 算术平方根是一个常见的数学运算，涉及到求解一个数的平方根。在编程中，利用内置函数通常可以高效且精确地完成这个计算。