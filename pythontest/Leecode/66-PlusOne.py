from unicodedata import digit

class Solution:
    def function(self, input_string: str) -> list:

        # 拆分输入字符串为列表（按逗号分隔）
        string_list = input_string.split(',')
        # 将每个字符串转换为整数
        integer_list = [int(num.strip()) for num in string_list]
        
        # # 将每个字符串转换为整数，并去除多余的空白字符
        # integer_list = [int(num.strip()) for num in string_list if num.strip().isdigit()]

        print (integer_list)

        # 将数字提取出来成为一个整数  
        #  ''.join(map(str, numbers)):
        # ''.join() 将这些字符串拼接成一个长字符串 '4322'。
        number_str = ''.join(map(str, integer_list))

        result_integer = int(number_str)
        print (result_integer)

        result_integer = result_integer +1

        # 将整数转换为字符串
        result_string = str(result_integer)

        # 将每个字符（数字）转换为整数，并存储在列表中
        number_list = [int(digit) for digit in result_string]

        print (number_list)
        return number_list


input_string = input("输入一串数字，以逗号分隔： ")
objectSolution = Solution()
objectSolution.function(input_string)



# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:

#         # 将数字提取出来成为一个整数  
#         #  ''.join(map(str, numbers)):
#         # ''.join() 将这些字符串拼接成一个长字符串 '4322'。
#         number_str = ''.join(map(str, digits))

#         result_integer = int(number_str)
#         print (result_integer)

#         result_integer = result_integer +1

#         # 将整数转换为字符串
#         result_string = str(result_integer)

#         # 将每个字符（数字）转换为整数，并存储在列表中
#         number_list = [int(digit) for digit in result_string]
        
#         return number_list
    



# def function():
#     input_string = input("输入一串数字，以逗号分隔： ")

#     # 拆分输入字符串为列表（按逗号分隔）
#     string_list = input_string.split(',')
#     # 将每个字符串转换为整数
#     integer_list = [int(num.strip()) for num in string_list]
    
#     # # 将每个字符串转换为整数，并去除多余的空白字符
#     # integer_list = [int(num.strip()) for num in string_list if num.strip().isdigit()]

#     print (integer_list)

#     # 将数字提取出来成为一个整数  
#     #  ''.join(map(str, numbers)):
#     # ''.join() 将这些字符串拼接成一个长字符串 '4322'。
#     number_str = ''.join(map(str, integer_list))

#     result_integer = int(number_str)
#     print (result_integer)

#     result_integer = result_integer +1

#     # 将整数转换为字符串
#     result_string = str(result_integer)

#     # 将每个字符（数字）转换为整数，并存储在列表中
#     number_list = [int(digit) for digit in result_string]

#     print (number_list)
#     return number_list
# function()