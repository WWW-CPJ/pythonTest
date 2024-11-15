"""
https://www.w3school.com.cn/python/index.asp

# 1.输出
if 5 > 2:
  print ("five is greater than two!")

#单引号和双引号效果等同
print('hello')
print("hello")

a='hello'
b="hello"
print(a)
print(b)

"""
#三引号的应用：1 多行注释；2 多行字符串赋值给变量
"""xxx"""
'''xxx'''
#a = """Python is a widely used general-purpose, high level programming language. 
#It was initially designed by Guido van Rossum in 1991 
#and developed by Python Software Foundation. 
#It was mainly developed for emphasis on code readability, 
#and its syntax allows programmers to express concepts in fewer lines of code."""
#print(a)


"""
# 2.def 定义函数
x="hello world!"

def function():   
  print(x)

function()
"""

"""
# 3.数字类型转换，
x=10
y=6.6
z=9j
def functiona(): 
     print(type(x))
     print(type(y))
     print(type(z))

a=float(x)
b=int(y)
c=complex(z)
def functionb(): 
     print(type(a))
     print(type(b))
     print(type(c))

functiona()
functionb()

指定变量类型
x=int(3.3)
y=float(4)
z=str(4.0)
def function(): 
     print(type(x))
     print(type(y))
     print(type(z))

function()
"""



"""
# 4.随机数  python没有random函数来创建随机数，而是用内置模块生成随机数
import random

def randonnum():
    print(random.randrange(1,20))
    print(random.randrange(1,30))
    print(random.randrange(1,40))

randonnum()
"""



"""
# 5 字符串 是数组
#获取位置 1 处的字符（请记住第一个字符的位置为 0）：
x="hello world"
print(x[0],x[1])

裁切
指定开始索引和结束索引，以冒号分隔，以返回字符串的一部分。
x="hello world"
print(x[0],x[1:8])
#不包括8
负的索引
使用负索引从字符串末尾开始切片：.
print(x[-5],x[-8:-1])
x="hello world"
print(x[0],x[-1])

字符串长度
如需获取字符串的长度，请使用 len() 函数。
x="hello world"
print(len(x))
"""

"""
字符串方法
1 strip() 删除开头和结尾的空白字符
x="hello world "
print(x.strip())
2 lower() 返回小写字符串
print(x.lower())
3 upper() 返回大写字符串
print(x.upper())
4 replace() 用另一段字符串替换字符串
print(x.replace("world","nima"))+
5 split() 找到分隔符的实例时将字符串拆分为子字符串（空格也可以作为分隔符）
print(x.split(" "))
"""

"""
检查字符串
如需检查字符串中是否存在特定短语或字符，我们可以使用 in 或 not in 关键字。
x="HELLO  world"
a="o" in x
b="a" not in x
print (a)
print(b)
"""

"""
字符串串联  
1  串联字符串
x="HELLO  world"
y="nimade"
z=x+y
print(z)
2  字符串中间插入字符
m=x +"wocao"+y
print(m)

*3 字符串数字组合  format() 方法 接收传递的参数--格式化他们--将其放在占位符所在的字符串中
age=36
n="nima jinnian {}" 
print (n.format(age))

format() 方法 不限制参数的数量，并放在各自的占位符中
age=36
mage=37
hage=38
n="nima jinnian {},next year is {},the year after next is {}" 
print (n.format(age,mage,hage))
可以用索引号{0来确保参数被放在正确的占位符中}
text="nima jinnian {2},next year is {0},the year after next is {1}" 
print (text.format(age,mage,hage))
"""

"""
x="Wo  Cao "
y="Ni Ma!"
z=x+y
print(z)
m=x +" wocao "+y
print(m)

age=36
mage=37
hage=38
n="nima jinnian {},next year is {},the year after next is {}" 
text="nima jinnian {2},next year is {0},the year after next is {1}" 
print (n.format(age,mage,hage))
print (text.format(age,mage,hage))
"""

"""
字符串方法
Python 有一组可以在字符串上使用的内建方法。
注释：所有字符串方法都返回新值。它们不会更改原始字符串。

字符串方法
Python 有一组可以在字符串上使用的内建方法。
注释：所有字符串方法都返回新值。它们不会更改原始字符串。

1 strip() 删除开头和结尾的空白字符
x="hello world "
print(x.strip())
2 lower() 返回小写字符串
print(x.lower())
3 upper() 返回大写字符串
print(x.upper())
4 replace() 用另一段字符串替换字符串
print(x.replace("world","nima"))
5 split() 找到分隔符的实例时将字符串拆分为子字符串（空格也可以作为分隔符）
print(x.split(" "))

方法	                            描述
capitalize() 把首字符转换为大写。
casefold()  把字符串转换为小写。
center()	  返回居中的字符串。
count()	返回指定值在字符串中出现的次数。
encode()	返回字符串的编码版本。
endswith()	如果字符串以指定值结尾，则返回 true。
expandtabs()	设置字符串的 tab 尺寸。
find()	在字符串中搜索指定的值并返回它被找到的位置。
format()	格式化字符串中的指定值。
format_map()	格式化字符串中的指定值。
index()	在字符串中搜索指定的值并返回它被找到的位置。
isalnum()	如果字符串中的所有字符都是字母数字，则返回 True。
isalpha()	如果字符串中的所有字符都在字母表中，则返回 True。
isdecimal()	如果字符串中的所有字符都是小数，则返回 True。
isdigit()	如果字符串中的所有字符都是数字，则返回 True。
isidentifier()	如果字符串是标识符，则返回 True。
islower()	如果字符串中的所有字符都是小写，则返回 True。
isnumeric()	如果字符串中的所有字符都是数，则返回 True。
isprintable()	如果字符串中的所有字符都是可打印的，则返回 True。
isspace()	如果字符串中的所有字符都是空白字符，则返回 True。
istitle()	如果字符串遵循标题规则，则返回 True。
isupper()	如果字符串中的所有字符都是大写，则返回 True。
join()	把可迭代对象的元素连接到字符串的末尾。
ljust()	返回字符串的左对齐版本。
lower()	把字符串转换为小写。
lstrip()	返回字符串的左修剪版本。
maketrans()	返回在转换中使用的转换表。
partition()	返回元组，其中的字符串被分为三部分。
replace()	返回字符串，其中指定的值被替换为指定的值。
rfind()	在字符串中搜索指定的值，并返回它被找到的最后位置。
rindex()	在字符串中搜索指定的值，并返回它被找到的最后位置。
rjust()	返回字符串的右对齐版本。
rpartition()	返回元组，其中字符串分为三部分。
rsplit()	在指定的分隔符处拆分字符串，并返回列表。
rstrip()	返回字符串的右边修剪版本。
split()	在指定的分隔符处拆分字符串，并返回列表。
splitlines()	在换行符处拆分字符串并返回列表。
startswith()	如果以指定值开头的字符串，则返回 true。
strip()	返回字符串的剪裁版本。
swapcase()	切换大小写，小写成为大写，反之亦然。
title()	把每个单词的首字符转换为大写。
translate()	返回被转换的字符串。
upper()	把字符串转换为大写。
zfill()	在字符串的开头填充指定数量的 0 值。
注释：所有字符串方法都返回新值。它们不会更改原始字符串。
"""




"""
x="wo diao ni ma de"
y="Ai XiBa"

def lower():
    z=x.lower()
    print(z)
lower ()
def upper():
    print(x.upper())
upper ()
def capitalize():
    print(x.capitalize())
capitalize()
def casefold():
    print(x.casefold())
casefold()
def swapcase():
    print(y.swapcase())
swapcase()
def title():
    print(x.title())
title()

def isupper():
    print(x.isupper())
    print(y.isupper())
isupper()
def islower():
    print(x.islower())
    print(y.islower())
islower()
def center():
    print(x.center(50))
center()
def count():
    a=x.count("i")
    print(a)
count()
def encode():
    global b
    b=x.encode()
    print(b)
encode()
def endswith():
    c=x.endswith(".",5,10)
    print(c)
endswith()
def find():
    print (x.find("o",0,10))
find()
"""

"""
def expandtabs():
    m="qunide"
    x="woc\tcao\tni\tma\tde\t!"
    y=x.expandtabs(x)
    z=y.title()
    print (y)
    print (z)
expandtabs()
"""

"""
布尔
1 表达式
print (8>7)

2 if 语句
a=300
b=400

if a>b:
    print("你是个傻逼")
else :
    print("长脑子了")

    
输出false
print(bool("false"))
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool())
print(bool([]))
print(bool({}))
"""



"""
x=100
y=200

def hanshu(x,y):
    
    if x>0:
        return x
    return y
"""

"""
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
"""

