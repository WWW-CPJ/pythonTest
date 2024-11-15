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