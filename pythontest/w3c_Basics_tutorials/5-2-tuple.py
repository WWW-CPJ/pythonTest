
#元组定义
tuple01=('one','two','three','four','five')
print (tuple01)
#单项元组     注意 逗号
tuple02=('dog',)
print  (tuple02)

#索引
'''
print (tuple[0])
print (tuple[-1])
print (tuple[0:2])
print (tuple[-3:-1])

'''

#更改元组值
thislist=list(tuple01)       #使用list方法将元组改为列表
thislist[0]='ONE'
thistuple=tuple(thislist)    #使用tuple方法将列表改为元组
print (thistuple)

#遍历元组
for x in thistuple:
    print (x)

#检查项目是否存在
if 'one' in thistuple:
    print ('yes')
else :
    print ('no')

#元组长度
print (len(thistuple))

#合并元组
tuple03=tuple02 + thistuple
print (tuple03)

#tuple（）  构建函数
thistuple = tuple(('pig',))
print (thistuple)