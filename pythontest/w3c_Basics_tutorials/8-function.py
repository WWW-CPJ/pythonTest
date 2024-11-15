
'''函数是一种尽在调用时运行的代码块。
可以将数据（参数）传递到函数中。
函数可以把数据作为结果返回。'''

# 1 创建，调用 函数，用  def  关键字定义；函数名加括号调用
'''def my_function():
    print (" hello world !")

my_function()'''

# 2.1 参数
#参数在函数名后的括号内指定。可以根据需要添加任意数量的参数，用逗号分隔即可。
#没有定义的参数调用时需要加引号，定义好的不需要加引号
'''def my_function(name):
    print ("ni hao ," + name)

my_function('lihua')
my_function('lina')
my_function('geg')'''

# 2.2 默认参数  如果我们调用了不带参数的函数，则使用默认值：
'''def my_function(name='li ming'):
    print ('come on ! '+ name)

my_function ('lihua')
my_function ('lixin')
my_function ('son!')
my_function ()'''

# 3 以 list 传参
#发送到函数的参数可以是任何类型（字符串，数字，列表，字典等），并且在函数内其将被视为相同数据类型。
#例如，如果您将 List 作为参数发送，它到达函数时仍将是 List（列表）：
'''def my_function (list):
    for x in list:
        print (x)
month=['January','Feubary','March','April','May','June','July','August','September','October','November','December']
my_function (month)'''

# 4 返回值  如需使函数返回值，请使用 return 语句：
'''def my_function(x=11):
    return x*3
print (my_function(3))
print (my_function(4))
print (my_function(6))
print (my_function())'''

# 5 关键字参数    使用  key = value  语法发送参数。参数的顺序无关紧要。
'''def  my_function(yesterday,today,tomorrow):
    print ('In the time of '+ today)
my_function (yesterday='0123',today='0124',tomorrow='0125')'''

# 6 任意参数
'''def my_function(*day):
    print ('In the time of today ' + day [1])
    print ('In the time of tomorrow ' + day [2])

my_function ('0123','0124','0125')'''

# 7 pass 语句
'''def my_function():
    pass'''


# 8 递归
#Python 也接受函数递归，这意味着定义的函数能够调用自身。

#递归是一种常见的数学和编程概念。它意味着函数调用自身。这样做的好处是可以循环访问数据以达成结果。
#开发人员应该非常小心递归，因为它可以很容易地编写一个永不终止的，或者使用过量内存或处理器能力的函数。但是，在被正确编写后，递归可能是一种非常有效且数学上优雅的编程方法。
#在这个例子中，tri_recursion() 是我们定义为调用自身 ("recurse") 的函数。我们使用 k 变量作为数据，每次递归时递减（-1）。当条件不大于 0 时（比如当它为 0 时），递归结束。

'''def my_recursion(x=0):
    if (x>0):
        result=x+my_recursion(x-1)
        print (result)
        return result
    else:
        result=0
        return result
print ("\n\n Example results : ")

my_recursion(6)'''


#lambda 函数  lambda函数是一种小的匿名函数。
#lambda函数可以接受任意数量的参数，但只能有一个表达式。参数之间用逗号隔开
#lambda arguments : expression
x=lambda a:a+10
print (x(9))

x=lambda a,b:a*b
print(x(4,5))

x=lambda a,b,c:a*b*c
print (x(6,6,6))


def my_function(n):
    return lambda a: a * n
mydouber=my_function(2)
print(mydouber(999))