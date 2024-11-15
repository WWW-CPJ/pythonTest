# 1 创建类 create a class
class myclass:
    x=5

# 2 创建对象  create an object
p1=myclass()
print(p1.x)

# 3 _init_() 函数
#创建名为 Person 的类，使用 __init__() 函数为 name 和 age 赋值：
'''
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Person('lihua','26')       #p1对象 为 类person 的 属性 (name,age) =('lihua',26) 时的产物
print(p1.name)
'''


# 4 对象方法
'''
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def my_function(self):
        print ("my name is "+ self.name)
        print (self.age)

p1=Person('lihua',26)
p1.my_function()                 #参数赋值后的类，执行参数为当前值时的方法
'''

# 5 self参数，使用单词 mysillyobject 和 abc 代替 self：
'''
class Person():
    def __init__(mysillyobject,name,age):
        mysillyobject.name=name
        mysillyobject.age=age

    def my_function(abc):
        print (abc.name)
        print (abc.age)

p1=Person('xiaoming',30)
p1.my_function()
'''

# 6 修改对象属性
'''
class Person():
    def __init__(mysillyobject,name,age):
        mysillyobject.name=name
        mysillyobject.age=age

    def my_function(abc):
        print (abc.name)
        print (abc.age)

p1=Person('xiaoming',30)
p1.my_function()
p1.age=40
p1.my_function()
'''

# 7 删除对象属性
'''
class Person():
    def __init__(mysillyobject,name,age):
        mysillyobject.name=name
        mysillyobject.age=age

    def my_function(abc):
        print (abc.name)
        print (abc.age)

p1=Person('xiaoming',30)
p1.my_function()
del p1.age
p1.my_function()
'''

# 8 删除对象
class Person():
    def __init__(mysillyobject,name,age):
        mysillyobject.name=name
        mysillyobject.age=age

    def my_function(abc):
        print (abc.name)
        print (abc.age)

p1=Person('xiaoming',30)
p1.my_function()
del p1
p1.my_function()

# 9 pass 语句
class muyclass():
    pass