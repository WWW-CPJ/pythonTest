# 1  Python 日期
# Python 中的日期不是其自身的数据类型，但是我们可以导入名为 datetime 的模块，把日期视作日期对象进行处理。
# 导入 datetime 模块并显示当前日期：

import datetime
x=datetime.datetime.now()
print (x)

# 2 日期输出
#日期包含年、月、日、小时、分钟、秒和微秒。datetime 模块有许多方法可以返回有关日期对象的信息。
print (x.year)
print (x.month)
print (x.day)
print (x.strftime('%A'))

# 3 创建日期对象 ： 使用 datetime 模块的 datetime() 类（构造函数）。
#  datetime() 类需要三个参数来创建日期：年、月、日。
a=datetime.datetime(2021,3,6)
print (a)

# 4 strftime() 方法
# datetime  对象拥有把日期对象格式化为可读字符串的方法。
# 该方法称为 strftime()，并使用一个 format  （格式）参数来指定返回字符串的格式：
#显示月份的名称：
print (a.strftime('%B'))