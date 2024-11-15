# 迭代  -iteration
#迭代器 -iterator
# 1 迭代器包含方法 __iter__() 方法和 __next__() 方法

# 2 迭代对象，列表、元组、字典和集合都是可迭代的对象
#从元组返回一个迭代器，并打印每个值
'''
mytuple=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
myiterator=iter(mytuple)       #myiterator就是一个迭代器
for x in myiterator:
    print (x)
'''
'''
print (next(myiterator))
print (next(myiterator))
print (next(myiterator))
print (next(myiterator))
print (next(myiterator))
print (next(myiterator))
print (next(myiterator))
'''

#从字符串返回一个迭代器，并打印每个值
'''
mystring="FUCK YOU !"
myiterator=iter(mystring)

for x in myiterator:
    print (x)
'''


# 3 遍历迭代器
#  提示：for 循环实际上创建了一个迭代器对象，并为每个循环执行 next() 方法。
'''
for x in mytuple:
    print (x)

for x in mystring:
    print (x)

'''
# 4 创建迭代器
"""
要把对象/类创建为迭代器，必须为对象实现    __iter__()  方法和  __next__()  方法。
 __iter__() 方法的作用相似，可以执行操作（初始化等），但必须始终返回迭代器对象本身。
__nect__() 方法也允许执行操作，并且必须返回序列中的下一个项目。
必须有iter和next两个方法。
"""
#创建一个返回数字的迭代器，从 1 开始，每个序列将增加 1（返回 1、2、3、4、5 等）：
'''
class number:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a +=1
        return x
    
myclass=number()
myiterator=iter(myclass)
print (next(myiterator))
print (next(myiterator))
print (next(myiterator))
print (next(myiterator))
print (next(myiterator))
print (next(myiterator))
'''

# 5 停止迭代  StopIteration
'''

class number:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a <=20:
            x=self.a
            self.a  +=1

            return x 
        else:
            raise StopIteration    #引发停止迭代
myclass=number()
myiterator=iter(myclass)
for x in myiterator:
    print(x)
    '''


mylist=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
mytuple=('january','february','march','april','May')
myset={'June','July','August','September','Octomber','November','December'}

myiterator=iter(mylist)
print (next(myiterator))
for x in mylist:
    print (x)

class number:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a <=20:
            x=self.a
            self.a +=1
            return x
        else:
            raise StopIteration

object=number()
myiterator=iter(object)
for x in myiterator:
    print (x)