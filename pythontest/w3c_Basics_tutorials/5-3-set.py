# 1 创建定义
thisset={"January","February","March","April","May"}
print (thisset)

#set集合无序不可更改，无法通过索引访问

# 2 遍历
def function_traversal():
    for x in thisset:
        print (x)
function_traversal()

# in 关键字
def function_keyword():
    if "January" in thisset:
        print ("January" in thisset)
function_keyword()

# 3 添加项目
thisset.add("June")
print (thisset)
thisset.update(["July","August"])
#thisset.update("July","August")
print (thisset)

# 4 获取长度
print (len (thisset))

# 5 删除
'''
thisset.remove("August")
print (thisset)
#如果要删除的项目不存在，则 remove() 将引发错误。

thisset.discard("July")
print (thisset)
#如果要删除的项目不存在，则 discard() 不会引发错误。

x = thisset.pop()
print (x)
print (thisset)
#pop() 方法删除最后一项：
'''

'''
thisset.clear()
print (thisset)
#（集合为空，但是集合还在）

del thisset
print (thisset)
#（集合不存在）
'''

# 6 union()  合并两个集合    // 联合，合并，联盟
#union() 和 update() 都将排除任何重复项。
thisset2={"September","October","November","December"}
set = thisset.union(thisset2)
print (set)

set.update(thisset2)
print (set)

# 7 构造函数
thatset = (('one','two','three'))
print (thatset)

if 'one' in thatset:
    print ("yes")
