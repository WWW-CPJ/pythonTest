# 1 python 中的json
# python 中有一个名为 json 的内置包，可用于处理 json 数据。
# 导入 json 模块
import json


# 2 解析json  --  json转换为 python
# 一些json：
x='{"name":"Difa","age":24,"city":"GETAN"}'

#解析x
y=json.loads(x)

#结果是python字典
print (y)
print (y['name'])


# 3 把 python 转换为 json
#python 对象字典
x={
    "name":"Kelaode",
    "sex":"man",
    "age":30,
    "city":"GETAN"
}

#转换为 JSON
y=json.dumps(x)

#结果是json字符串
print (y)


#下列对象可以转换为JSON字符串
print(json.dumps({"name":"Bill","age":63}))
print(json.dumps(["apple","bananas"]))
print(json.dumps(("apple","bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x={
	"name":"Bill",
	"age":63,
	"married":True,
	"divorced":False,
	"children":("Jennifer","Rory","Phoebe"),
	"pets":None,
	"cars":[
		{"model":"Porsche","mpg":38.2},
		{"model":"BMW M5","mpg":26.9}
		  ]
 }
print(json.dumps(x))


# 4 格式化结果
# 上面的示例打印了一个JSON字符串，但它不是很容易阅读，没有缩进和换行。
# json.dumps() 方法提供了令结果更容易读的参数 ： indent
#使用 indent 参数 定义缩进数：
print(json.dumps(x,indent=4))

# 分隔符默认为(", " , ": ") —— 用逗号和空格分隔每个对象，用冒号与空格分隔键与值
#可以使用  separators 参数  修改默认分隔符
print(json.dumps(x,indent=6,separators=("; ","--  ")))


# 5 对结果排序
# json.dumps() 方法提供了对结果中的键进行排序的参数 ： sort_keys
# 使用  sprt_keys  参数来指定是否应对结果进行排序
print(json.dumps(x,indent=4,sort_keys=True))