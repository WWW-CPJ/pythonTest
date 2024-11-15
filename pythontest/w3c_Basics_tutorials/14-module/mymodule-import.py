# 2 用 import 语句使用模块
import mymodule


#如果使用模块中的函数时，请使用以下语法：
#module_name.function_name
mymodule.Hello('Difa')


# 3 模块中的变量:访问module中的list-weekly
a=mymodule.month[0]
print (a)

# 4 重命名:在导入模块时 使用  as  关键字创建别名
import mymodule as module

a=module.month[1]
print (a)

# 5 内建模块：python中有几个内建模块，可以随时导入
import platform

x=platform.system()
print (x)

# 6 dir() 函数  (Directory -- 目录)
#内置函数可以列出模块中的所有函数名（或变量名）
#dir() 函数可用于所有模块，也可用于您自己创建的模块。
x=dir(platform)
y=dir(module)

print (y)

# 7 从模块导入：使用  from  关键字选择仅从模块中导入 部件
#提示：在使用 from 关键字导入时，请勿在引用模块中的元素时使用模块名称。示例：person1["age"]，而不是 mymodule.person1["age"]。
from mymodule import weekly
x=weekly[0]
y=mymodule.weekly[1]
print (x)
print (y)