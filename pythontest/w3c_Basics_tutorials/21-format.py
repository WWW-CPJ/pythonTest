# 1 format()允许格式化字符串的选定部分
#添加要显示价格的占位符
price=60
text="The price is {} dollars."
print (text.format(price))  

# 2 多个值
price=60
quantity=3
itemo=666
text="I want {} prices  of item number {} for {:.2f} dollars."     #  :.2f -- 代表小数点后两位
print(text.format(quantity,itemo,price))

# 3 索引号
# 使用索引号（花括号 {}内的数字 ）来确保将值放在正确的占位符中：
quantity=6
itemo=3
price=66
text="I want {0} prices  of item number {1} for {2:.2f} dollars." 
print (text.format(quantity,itemo,price))

#可以使用相同的索引号，多次引用相同的值
age=24
name="LiMA"
text="He name is {1},{1} is {0} years old."
print (text.format(age,name))

# 4 命名索引
#在花括号中驶入名称来使用命名索引 ：{caename} ，但是在传递参数值  text.format(carname="Ford")时，必须使用名称
text="I have a {carname},it is a {model}."
print(text.format(carname="HAVE",model="大狗2.0"))