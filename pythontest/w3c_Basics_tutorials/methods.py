string = "fuck you every Day"
print(string)

capitaliza_string = string.capitalize()
print(capitaliza_string)
# 第一个单词的首字母大写

casefold_string = string.casefold()
print(casefold_string)
# 每个单词的字母都小写

center_string = string.center(30, "~")
print(center_string)

count_string = string.count("u", 0, 20)
print(count_string)
# 返回指定值在字符串中指定范围内，出现的次数

encode_string = string.encode(encoding="UTF-16", errors="errors")
print(encode_string)
# 返回字符串的编码版本

startwith_string = string.startswith("fuck", 0, 20)
print(startwith_string)
# 指定范围内，是否以指定值开头

endswith_string = string.endswith("mother", 0, 20)
print(endswith_string)
# 指定范围内，是否以指定值结尾

expandtabs_string = string.expandtabs(12)
print(" string")
# 将制表符的大小设置为指定的空格数，默认的空格数是8， tabsize 不用带双引号，直接写数字就可以  

find_string = string.find("fucl", 0, 20)
print(find_string)
# 指定范围内搜索指定的值，并返回首次出现的位置，空格也算位置，如果找不到该值，则返回-1
# find() 与 index()方法几乎相同，唯一的区别是index如果找不到会引发异常

index_string = string.index("fuck", 0, 20)
print(index_string)
# 指定范围内搜索指定的值，并返回首次出现的位置，空格也算位置，如果找不到该值，则引发异常

txt = "{shui} fuck {who}"
print(txt.format(shui="TMD,", who="everything"))
txt = "{0} , fuck {1}"
print(txt.format("艹", "NMD"))
txt= "{}, {}"
print (txt.format("艹! ", "FUCK!"))
txt= "fuck you {price:.3f}"
print(txt.format(price=100000))
# 格式化指定的值，并将其插入字符串的占位符内，返回格式化的字符串，参数 value可以是一个或者多个，也可以是数字（指定位置）
# 这些值可以是用逗号分隔的值列表、键=值列表，或两者的组合。这些值可以是任何数据类型。

txt = "艹! fuck!"
alpha = "TaMaDe"
print(string.isalpha())
print(txt.isalpha())
print(alpha.isalpha())
# 检查所有的字符（包括空格和符号）是否都是字母。alpha：字母

print(string.isdigit())
digit= "123456"
txt="123.456"
print(digit.isdigit())
print(txt.isdigit())
# 检查所有的字符（包括空格和符号）是否都是数字。不接受小数点，空格，字母，符号。接受阿拉伯数字字符

numeric = "123一二三"
print(numeric.isnumeric())
# 检查是否是 “数字字符”，定义广泛，只要代表意思是数字就可以。中文，数字，罗马数字，阿拉伯数字都可以。
# 空格标点符号不识别

txt = "123FUCK"
print(txt.isalnum())
# 检查文本中的所有字符是否都是数字和字母组成，（不包括符号和空格）

decimal_number="\u0030"     # unicode for 0
decimal_alpha="\u0047"      # unicode for G
print(decimal_number.isdecimal())
print(decimal_alpha.isdecimal())
# 检查Unicode对象代表的是不是小数，在0-9 范围中的数字

txt1="demo"
txt2="123_abc"
txt3="123 abc"
print(txt1.isidentifier())
print(txt2.isidentifier())
print(txt3.isidentifier())
# 检查是否是有效标识符，仅包含字母数字下划线的

txt= "fuck you"
txt2= "fuck \n you "
print(txt2)
print(txt.isprintable())
print(txt2.isprintable())
# 检查文本中的字符是否可打印。只有回车符：\r 和 换行符：\n 不可打印。

space_txt="    "
not_space_txt="  fuck   "
print(space_txt.isspace())
print(not_space_txt.isspace())
# 检查所有字符是否都是空格

title="Fuck You! Cao"
not_title="Fuck -everything 300"
print(title.istitle())
print(not_title.istitle())
# 检查字符串的每个单词是否都是以大写字母开头，单词其余部分均为小写字母。符号和数字将被忽略

upper="FUCK YOU!"
not_upper="Fuck You"
print(upper.isupper())
print(not_upper.isupper())
# 检查文本中的所有字符是否都是大写，仅检查字母字符，不检查数字，符号，空格。

lower="fuck you"
not_lower="Fuck you 1132.333"
print(lower.islower())
print(not_lower.islower())
# 检查字符串中的所有字母字符是否都是小写，进检查字母字符，不检查数字，符号，空格。

tuple=("yaoxi", "GIAO", "TMd")
print("*".join(tuple))
mydictionary={"name": "Bill", "age":33}
separator=" and "
print(separator.join(mydictionary))
# 用指定分隔符，将元素都链接起来成为一个字符串
# 注释：在使用字典作为迭代器时，返回的值是键，而不是值。

print(string.ljust(30, "*"))
# 指定输出字符串长度，使用指定的字符（默认为空格）作为填充字符，使字符串左对齐
# fuck you every Day************

print(string.rjust(30, "*"))
# 指定输出字符串长度，使用指定的字符（默认为空格）作为填充字符，使字符串右对齐
# ************fuck you every Day

txt1= "GOOD GOOD STUDY, DAY DAY UP, 123, abc, ()"
print(txt1.lower())
# 所有字母字符小写，其他都将被忽略
# casefold() 方法返回一个字符串，其中所有字符均为小写。
# 此方法与 Lower() 方法相似，但是 casefold() 方法更强大

txt2="good good study. day day up, 123, abc, ()"
print(txt2.upper())
# 所有字符大写，其他的都将被忽略

title_txt="good study, day up (123)go"
print(title_txt.title())
# 把每个单词的首字母（如果有别的字符，大写第一个字母）都大写

txt="*********gogogo"
print(txt.lstrip("*"))
# 删除字符串左边的所有 指定的前导字符。默认要删除的前导字符是空格
txt="gogogo********"
print(txt.rstrip("*"))
# 删除字符串右边的所有 指定的前导字符。默认要删除的前导字符是空格

print(string.partition("you"))
print(string.partition("your"))
txt="123 456,789 and 999-888 456"
print(txt.partition("456"))
# partition方法，用指定的值将字符串分割为三部分，（value前面的，value，value后面的）
# 注意搜索指定字符串的第一个匹配项，从搜索到的第一个开始分隔
# 如果没有找到指定项，会返回一个元组：("整个字符串"， "空字符串"， "空字符串")

print(txt.rpartition("456"))
# rpartition 用指定的值分隔但部分，同上
# 注意搜素的是指定字符串的最后一次出现
# 如果没找到，同上

txt = "起床，上班，吃饭，上班，吃饭，回家，吃饭，睡觉,上班"
print(txt.replace("上班", "搬砖", 2))
# string . replace （oldvalue, newvalue, count）
# 将指定值用指定值来替换掉，默认替换所有旧值。可以指定替换几次

print(string.rfind("day", 0, 30))
print(string.rfind("y", 0, 30))
# 在指定范围寻找指定的值，返回该值最后一次出现的位置
# 如果找不到该值，返回-1。

print(string.index("y", 0, 30))             # 第一次出现
print(string.rindex("y", 0, 30))            # 最后一次出现 
# 在指定范围内寻找指定值，返回该值出现的位置，
# 与find 不同的是，如果找不到就会引发异常：ValueError: substring not found

txt1="*******%%%   000 一夜暴富 000  ~~~~~~"
print(txt1.strip("*  ~ % 0"))
# 删除字符串开头和结尾的 任何 前导和尾随字符。默认删除的是空格，只有一个参数，各个字符之间可以用空格隔开
# 数字不是字符串，不是前导和尾随字符

print(txt1.lstrip("*0 ~"))
# 删除字符串左侧的前导字符

print(txt1.rstrip("~ %"))
# 删除字符串右边的尾随字符

txt="apple, banana, tomato, orange, yellow, watermelon"
print(txt.split(",", 3))
print(txt.split(","))
# 在指定的分隔符处拆分字符串，并指定拆分次数。默认拆分次数为 -1,即全部拆分
# 分隔符默认为空白

print(txt.rsplit(",", 3))
# ['apple, banana, tomato', ' orange', ' yellow', ' watermelon']
# 从后往前拆分

txt1="来来来\n 让我将你心儿摘下 \n 喝完这一杯还有三杯 \n 天气晴朗"
print(txt1.splitlines(False))
print(txt1.splitlines(True))
# 在换行字符：\n 处拆分字符串，并将拆分后的字符串输出为一个列表。
# 只有一个参数。默认参数为false，输出内容不包含换行字符，参数为true时，输出后会显示换行符

txt1="abc WDNMD CNM nmlgb"
print(txt1.swapcase())
# 无参数，大小写转换，大写换小写，小写换大写

txt="你看你吗呢"
print(txt.zfill(20))
# 在字符串填满0，满足 长度参数。长度参数如果小于字符串长度，不填充
# 只能填充 0

txt="fuck"
print(txt.translate())