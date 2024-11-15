#list=["草泥马","去尼玛","滚犊子","你大爷","煞笔","没钱开什么公司", '老玩意儿', '老登']

#创建列表
# 1 lista=["ONE","TWO","THREE","FOUR","FIVE"]
# 2 list()  构造函数
'''
thislist=list(('one','two'))  
print (thislist)
'''

'''
https://www.w3school.com.cn/python/python_lists.asp
append()	在列表的末尾添加一个元素
clear()	删除列表中的所有元素
copy()	返回列表的副本
count()	返回具有指定值的元素数量。
extend()	将列表元素（或任何可迭代的元素）添加到当前列表的末尾
index()	返回具有指定值的第一个元素的索引
insert()	在指定位置添加元素
pop()	删除指定位置的元素
remove()	删除具有指定值的项目
reverse()	颠倒列表的顺序
sort()	对列表进行排序
'''

#1  访问项目
"""
print(list)
print(list[1]+"的")
print(list[-1]+"你")
print(list[4:6])
print(list[-3:-1])
"""


#2  更改项目值
"""
list[1]="草 尼玛的"
print(list[1])
"""


#3  遍历列表
"""
for x in list:
    print (x+"你")
"""

#4  检查项目是否存在
"""
if "尼玛" in list:
    print ("yes")
else:
    print("没")
"""

#5  列表长度
#print (len(list))

#6  添加项目
"""
list.append("老登")  #末尾添加
list.insert(-1,"老玩意儿")  #指定位置添加
print(list)
"""


#7  删除项目
# 1  remove()
"""
list.remove("老玩意儿")
print(list)
"""
# 2  pop()
"""
list.pop(0)
print(list)
"""
# 3 del  关键字
# 删除指定索引
"""
del list[6]
print (list)
"""
#全部删除
"""
del list
print (list)
"""

# 4 clear()方法 清空列表
"""
list.clear()
print (list)
"""

#8  复制列表
"""
1
lista=list
print (lista)

2
copy() 方法
listb=list.copy()
print(listb)

3
list() 方法
lista=list(mylist)
"""

#9  合并列表
"""
1  "+" 合并
list=lista+listb      

2 append()方法 逐一加到末尾
for x in list2:
     list1.append(x)

3 extend() 整个列表加到末尾
listb.extend(lista)
"""
"""
lista=["ONE","TWO","THREE","FOUR","FIVE"]
listb=["SIX","SEVEN","EIGHT","NINE","TEN"]
listc=["january"," "]

listb.extend(lista)
print(listb)

"""

lista=["ONE","TWO","THREE","FOUR","FIVE"]
listb=["SIX","SEVEN","EIGHT","NINE","TEN"]

'''
print (lista[-4:-1])
lista.append("eleven")
lista[1]="one"

for x in lista:
    print (x + "  yuan")

lista.extend(listb)
print (lista)

if "ONE" in lista:
    print ('全场1元! 全场1元!')
else:
    print ("全场两元") 

def function_len():
    global x
    x=len(lista)
    print ( 100 +  x )

function_len()

lista.append('eleven')
print (lista)

lista.insert(0,'zero')
print (lista)


lista.remove("one")
print (lista)
'''

lista.pop(1)
print (lista)

del lista[2]
print (lista)

#lista.clear()


listc=lista
print (listc)

listd=lista.copy()
print (listd)


list_fangfa=list(lista)
print (list_fangfa)


liste=lista + listb
print (liste)

lista.append('yuan')
print (lista)


y=lista.count('one')
print (y)


listc=list(('one','two','three'))
print (listc)





