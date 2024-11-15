#regex --  正则表达式
#match -- 匹配
#regex：是形成搜索模式的字符序列。可用于检查字符串时候包含指定的搜索模式。

# 1  python 提供了名为   re   的内置包，可用于处理正则表达式。
import re

# 2 检索字符串以查看它是否以“China”开头，并以“country”结尾
#元字符与特殊序列
text="China is a great country "
x=re.search("^China.*country$",text)

if(x):
    print("yes,we have a match")
else:
    print("no match")

# 3 findall()函数 返回包含所有匹配项的列表,这个列表以被找到的先后顺序返回。
x=re.findall("a",text)
print (x)
# 如果未找到匹配项，则返回空列表
x=re.findall("x",text)
print(x)

# 4 search()函数：搜索字符串中的匹配项目，如果存在匹配则返回 match 对象。
#如果有多个匹配，则仅返回首个匹配项目
#在字符串中搜索第一个空杯字符
x=re.search("\s",text)
print("The first white-space character is located in position: ",x.start())
#如果未找到匹配，则返回值  None：
x=re.search("USA",text)
print(x)

# 5 split()函数：返回一个列表，其中字符串在每次匹配时被拆分
# 在每个空白字符处进行拆分
x=re.split("\s",text)
print(x)
#可以通过指定 maxsplit 参数来控制拆分次数
#仅在空白字符首次出现时拆分字符串
x=re.split("\s",text,1)
print(x)

# 6 sub()函数：把匹配项替换为准备好的字符：
# 用 -替换空白字符
x=re.sub("\s","-",text)
print(x)
#通过指定 count 参数控制替换次数：
#替换前三个空白字符
x=re.sub("\s","-",text,3)
print(x)

# 7 match 对象
#match 对象是包含有关搜索和结果信息的对象
#注释：如果没有匹配，则返回值 None ，而不是 match  对象
#执行会返回match对象的搜索
x=re.search("a",text)
print(x)
'''
Match 对象提供了用于取回有关搜索及结果信息的属性和方法：
• span() 返回的元组包含了匹配的开始和结束位置
• .string 返回传入函数的字符串
• group() 返回匹配的字符串部分
'''
#输出首个匹配出现的位置（开始和结束位置）
#正则表达式 查找以大写 C 开头的任何单词
x=re.search(r"\bC\w+",text)
print (x.span())

#打印传入函数的字符串
x=re.search(r"\bC\w+",text)
print(x.string)

#打印匹配的字符串部分
#正则表达式查找以大写 C 开头的任何单词
x=re.search(r"\bC\w+",text)
print(x.group())