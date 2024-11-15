#1 创建
dictionary={
    'one':'January',
    'two':'February',
    'three':'March',
    'four':'April',
    'five':'May',
    'Six':'June'
}
print (dictionary)

# 2 访问
'''
print (dictionary['one'])
print (dictionary.get("one"))
'''

# 3 更改值
'''
dictionary['one'] = 'january'
x = dictionary.get("one")
print (x)
'''

# 4 遍历
'''
for x in dictionary:
 print (x)

for x in dictionary:
 print (dictionary[x])
'''

'''
for x in dictionary.values():
  print (x)

  for x,y in dictionary.items():
  print (x,y)
'''



'''
# 5 检查键是否存在
if "one" in dictionary:
  print ('yes')

# 6 长度
print(len(dictionary))

# 7 添加新项目
dictionary['seven']='July'
print (dictionary)
'''

# 8 删除项目
"""
#pop()方法删除指定项目
dictionary.pop('seven')
print (dictionary)
#popitem()方法删除最后插入的项目
dictionary.popitem()
print (dictionary)
'''
#del关键字 删除指定项目
del dictionary['five']
print (dictionary)
#del关键字 完全删除字典(删除后字典不存在)
del dictionary
print (dictionary)
'''

#clear() 方法清空字典
dictionary.clear()
print (dictionary)
"""
# 9 复制字典

dictionary2=dictionary
print (dictionary2)

dictionary3=dictionary.copy()
print (dictionary3)

dictionary4=dict(dictionary)
print (dictionary4)

# 10 嵌套字典
dictionary5={
    'thisdict':{
        "one":1,
        "two":2
    },
    'thisdict2':{
        'one':'monday',
        'two':'funday'
    },
    'thisdic3':{
        "today":'tuesday',
        "tommrow":'friday'
    }
}
print (dictionary5)

# 11 dict()构造函数
thisdict4=dict (today='tuesday',tommorow='weisday')
print (thisdict4)