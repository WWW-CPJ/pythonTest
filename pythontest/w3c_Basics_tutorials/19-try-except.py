'''
try块: 允许测试代码块以查找错误。
except块: 允许您处理错误。
finally块: 允许执行代码,无论 try 和 except 块的结果如何。
'''
# 1 异常处理
#调用python 发生异常或错误时，通常会停止并生成错误消息。可以使用  try  语句处理这些异常
#try 块将生成异常，因为 x 未定义：
try:
    print(x)
except:
    print("An exception occurred")


# 2 多个异常
#可以根据需要定义任意数量的  exception 块，例如，假如要为特殊类型的错误执行特殊代码块：
try:
    print(x)
except NameError:
    print("Something went wrong")
except:
    print("Nothing went wrong")

# 3 else
#如果没有引发错误，可以使用 else 关键字来定义要执行的代码块：
#本例中，try  块不会生成任何错误：
try:
	print("Hello")
except:
	print("Something went wrong")
else:
    print("Nothing went wrong")

# 4 finally
#如果制定了 finally 块，则无论  try 块是否引发错误，都会执行  finally  块。
try:
     print(x)
except:
     print("Something went wrong")
finally:
     print("The 'try except' is finished")

# 5 引发异常,可以选择在条件发生时抛出异常。如需抛出（引发）异常，请使用 raise 关键词。
x=-1
if x <0:
     raise Exception("Sorry,no numbers below zero")

# 能够定义所引发异常的类型、以及打印给用户的文本。
#如果 x 不是整数，则引发 TypeError：
x="hellp"
if not type(x) is int:
     raise TypeError("Only integers are allowed")