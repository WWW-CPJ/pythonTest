# class palindrome():
#     def __init__(self):
#         pass
    
def function():
    number = int(input("输入目标数字："))
    if number < 0:
        print (f"数字: {number}小于零，不是回文数")
        return False
    if number == 0:
        print(f"数字: {number} 为零，是回文数")
        return True
    if number > 0:
        str_number = str (number)
        reversedNumber = str_number[::-1]
        if str_number == reversedNumber:
            print(f"数字：{number} 是回文书，反转前后 相同")
            return True
        else:
            print(f"数字：{number} 不是回文书，反转前后不相同")
            return False
        
function()

# reversed_s = s[::-1]:
# 这行代码使用了 Python 的切片（slicing）语法来反转字符串 s。
# 切片语法: s[start:stop:step] 用于从字符串 s 中提取子字符串。
# start: 切片的起始位置（默认为 0）。
# stop: 切片的结束位置（默认为字符串的末尾）。
# step: 步长（默认为 1）。如果步长为负值，则表示从右向左反向提取。
# s[::-1]:
# 这里 start 和 stop 都没有指定，表示切片操作涵盖了整个字符串。
# step 为 -1，表示步长为负值，这会使得切片从字符串的末尾向开头反向提取字符。
# 因此，s[::-1] 产生了字符串 s 的反转版本。
# 变量 reversed_s 现在包含了反转后的字符串 "olleh"。
# 切片操作适用于字符串，而整数不支持这种操作