# 1 if关键词
'''
a=30
b=60
if a < b:
    print("a is less than b")
'''

# 2 缩进
#没有缩进的if语句会报错
'''
a=30
b=60
if a < b:
    print("a is less than b")
'''

# 3 elif    (if之后的第二条件)
'''
a=30
b=60
if a > b:
    print("a is greater than b")
elif a < b:
    print ("a is less than b")
'''

# 4 else     否则
'''
a=60
b=60
if a > b:
    print("a is greater than b")
elif a < b:
    print ("a is less than b")
else :
    print("a is equal to b")
'''

# 没有elif的else
'''
a=60
b=70
if a == b:
    print("a is equal to b")
else :
    print("a is not equal to b")
'''

# 5 简写 if   如果只有一条语句执行，可以将其与if语句放在同一行。
'''
a=30
b=60
if a < b:print("a is less than b")
'''

# 6 简写 if ... else 
'''
a=30
b=40
print ('a') if a>b else print ("b")
'''

# 同一行上使用多个else语句：
'''
a=60
b=70
print ("a") if a > b else print ('b') if a < b else print ('a is equal to b')
'''

# 7 and
'''a=30
b=40
c=50
if a>b and a>c:
    print ('a is maximum')
else:
    print ("no")'''

# 8  or  
'''
a=30
b=40
c=50
if a>b or a>c:
    print ('a is maximum')
else:
    print ("no")
'''

# 9 嵌套 if
'''x=20
if x >30:
    print ("x is greater than 30")
    if x >60:
        print('x is greater than 60')
    else:
        print('x is less than 60')
else:
    print ('x is less than 30')'''

# 10 pass语句
a=30
b=90
if a<b:
    pass