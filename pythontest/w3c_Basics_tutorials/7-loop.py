# 1.1 while循环
'''i=3           #while循环需要准备好相关的变量，定义一个索引变量 i 
while i<99:
    print(i)
    i*=3'''

# 1.2  breake 语句   条件为真时，停止
'''i=9
while i<=100:
    if i==69:
        break
    i+=10
    print(i)'''

# 1.3 continue 语句   （继续）条件为真时跳过当前迭代并继续下一个迭代
'''i=3
while i <=99:
    i+=3
    if i==33:
        continue
    print (i)'''

# 1.4 else 语句    条件为假时打印一条消息
'''i=3
while i<=33:
    if i==12:
        continue
    print (i)
    i+=3
else:
    print('i is not less than 33')'''


# 2.1 for 循环
'''list=['january','fuabrary','march']
for x in list:
     print (x)'''

# 2.2 循环遍历字符串
'''for x in "banana":
     print (x)'''

# 2.3  break  语句
'''list=[1,2,3,4,5,6,7,8,9]
for x in list:
    print (x)
    if x==3:
        break
    x+=1'''

#在打印前退出循环
'''list=[1,2,3,4,5,6,7,8,9]
for x in list:
    if x == 5:
        break
    print(x)
    x+=1'''

# 2.4 continue 语句
'''list=[1,2,3,4,5,6,7,8,9]
for x in list:
    if x == 5:
        continue
    print (x)
    x+=1'''

# 2.5  range() 函数
#注意：range(10) 不是 0 到 10 的值，而是值 0 到 9。
'''for x in range(10):
    print (x)'''

#range() 函数默认 0 为起始值，不过可以通过添加参数来指定起始值：range(3, 10)，这意味着值为 3 到 10（但不包括 10）：
'''for x in range(2,10):
    print(x)'''

#range() 函数默认将序列递增 1，但是可以通过添加第三个参数来指定增量值：range(2, 30, 3)。
'''for x in range(3,33,3):
    if (x==6):
        continue
    print (x)'''

# 2.6 for循环中的else
'''for x in range(3,33,3):
    if x == 9:
        continue
    print (x)
else:
    print ("end")'''

# 2.7  嵌套循环
'''list=['January','February','March','April','May','June','July','August','September','October','November','December']
for x in list:
    for y in range (1,30,1):
        print (x,y)
'''

# 2.8  pass 语句
'''for x in [1,2,3]:
    pass
for x in ("a","b","c"):
    pass
for x in {'a','b','c'}:
    pass
for x in {
    'a':1,
    'b':2,
    'c':3
}:
    pass'''