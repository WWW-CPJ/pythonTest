#scope:变量仅在创建区域内可用，称为作用域。

# 1 local scope：局部作用域，在函数内部创建的变量属于该函数的局部作用域，并且只能在该函数内部使用。
def function():
    x=100
    print(x)
function ()

# 函数内部的函数：
def function():
    x=99
    def sonfunction():
        print (x)
    sonfunction()
function()

# 2 global scope:全局作用域，
#在python代码主体中创建的变量是全局变量，属于全局作用域。
#在函数外部创建的变量是全局变量。全局变量在任何范围中可用
x=100
def function():
    print(x)
function()
print(x)

#命令变量
#如果在函数外部和内部操作同名变量，python会将他们视为两个单独的变量，一个是在全局范围内可用（在函数外部），而一个是在局部范围内可用（在函数内部）
x=100
def function ():
    x=200
    print (x)
function ()
print(x)

# 3 global关键字：如果需要创建一个全局变量，但被卡在本地作用域内，则可以使用global关键字
# global 关键字使变量成为全局变量
def function():
    global x 
    x=100
    print(x)
function()
print(x-1)

# 在函数内部更改全局变量，也请使用global关键字
x=100
def function():
    global x  #新的全局变量回覆盖掉同名的变量，此时x=200
    x=200
    print (x)
function()
print (x-1)