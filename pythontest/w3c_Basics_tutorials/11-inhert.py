# 1 创建一个类作为父类
class Person:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname

    def printname(self):
        print('my name is '+self.lastname + self.firstname,)

x=Person('Xiaoming','Wang')
x.printname()

# 2 创建子类，将父类作为参数
'''
如果您不想向该类添加任何其他属性或方法，请使用 pass 关键字。
现在,Student 类拥有与 Person 类相同的属性和方法。
'''
class son(Person):
    pass

y=son('Xiaobai','Li')                   #使用 Student 类创建一个对象，然后执行 printname 方法：
y.printname()

# 3 添加__init__()函数   每次使用类创建新对象时，都会自动调用 __init__() 函数。
'''
在子类中添加 __init__() 函数时，子类将不再继承父的 __init__() 函数。
注释：子的 __init__() 函数会覆盖对父的 __init__() 函数的继承。
'''

'''
class son (Person):
    def __init__(self, firstname, lastname):
             #添加属性等   pass  
        self.firstname=firstname
        self.lastname=lastname

    def printsonname(self):
        print ('My name was  '+self.firstname)

z=son('NIMA','WANG')
z.printsonname()
'''
 

#如需保持父的 __init__() 函数的继承，请添加对父的 __init__() 函数的调用：
class son (Person):
    def __init__(self, firstname, lastname):
        Person.__init__(self,firstname,lastname)

# 4 使用super()函数，可不必使用父元素的名称，它将自动从其父元素继承方法和属性。
class son(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        #将父类的name用super函数替换掉，但是没有self参数了

# 5 添加属性  graduationyear 
class son(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        self.graduationyear=2019
x=son('Ni','Ma')
print (x.graduationyear)
        #2019 年应该是一个变量，并在创建 student 对象时传递到 Student 类

#请在 __init__() 函数中添加另一个参数：添加 year 参数，并在创建对象时传递正确的年份：
class son(Person):
    def __init__(self, firstname, lastname,year):
        super().__init__(firstname, lastname,)
        self.year=year

x=son('Li','ming',2024)
print (x.year)

# 6 添加方法
class son(Person):
    def __init__(self, firstname, lastname,year):
        super().__init__(firstname, lastname)
        self.graduationyear=year

    def welcome(self):
        print("Welcome ",self.firstname , self.lastname,"to the class of ",self.graduationyear)
        #用加号不能连结数字和字符，但是逗号可以
        print (self.graduationyear)
x=son('Zhang','dan',2024)
x.welcome()



#example
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Elon", "Musk", 2019)
x.welcome()