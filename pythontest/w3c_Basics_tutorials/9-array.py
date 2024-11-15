# array  数组 ：Python 没有内置对数组的支持，但可以使用 Python 列表代替。
# 数组用于在单个变量中存储多个值：
# 数组是一种特殊变量，能够一次包含多个值。

# 1 创建 (create): 同创建 list
week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
month=['January','February','March','April','May','June','July','August','September','October','November','December']

# 2 访问  (access):通过索引访问
'''print (week[0])'''
#修改某个项目的值 (edit)  : 通过索引指定项目，同list
'''week[0]='monday'
print (week[0])'''

# 3 array longth: 使用len() 方法，同list
'''print (len(week))
print (len(month))'''

# 4 traversal 遍历: for  in
'''for x in week:
    print(x)'''

# 5 add an element: append(附加) 方法  加到末尾
week.append('today')
print (week)

# 6 delete an element:
#pop() 方法
week.pop(7)
print (week)

#remove()  方法
week.remove('Monday')
