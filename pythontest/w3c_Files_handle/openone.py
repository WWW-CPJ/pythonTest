# 一  文件读取
# 1 read()方法读取文件
x=open("hello.txt")
print (x.read())

# 2 只读前五个字符
x=open("hello.txt")
#print (x.read(5))

# 3 读行
'''
print (x.readline())
print (x.readline())
print (x.readline())

'''
# 4 遍历
'''
for y in x:
    print (y)
'''

# 5 关闭文件
x.close()



# 二  文件写入
#  "a" - 追加 - 会追加到文件的末尾                         append
#  "w" - 写入 - 会覆盖任何已有的内容

# 1 追加
x=open("hello.txt","a")
x.write("four")
x.close
x=open("hello.txt","r")
print(x.read())

# 2 覆盖
x=open("hello.txt","w")
x.write("four")
x.close
x=open("hello.txt","r")
print(x.read())

# 3 创建新文件
#  y=open("two.txt","x")
#  y=open("three.txt","w")

# 三  删除文件
# 1 删除
'''
import os
os.remove("aaa.txt")
'''

# 2 检查文件是否存在
import os
if os.path.exists("aaa.txt"):
    os.remove("aaa.txt")
else:
    print("files already removed")

# 3 删除空文件夹
os.rmdir("Files_handle")