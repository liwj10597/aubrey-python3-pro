#!/usr/bin/python3

#python数据类型
#数值类型
    #整数、bool、浮点数和复数
#字符串类型
    #字符串 python中单引号和双引号完全相同，使用三引号可以指定多行字符串

corp = "jollychic"
print(corp)

corp = '''jollychic
          data'''
print(corp)

#转移符\,使用r可以让反斜杠不发生转义
corp = 'jollychic\ndata'
print(corp)
corp = r'jollychic\ndata'
print(corp)

#字符串用+进行连接，用*表示重复
name = 'li' + 'wei'
print(name)

name = 'li'*2
print(name)

#python没有单独的字符类型，一个字符为1的字符串就是字符类型

str='jollychic'

print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始的后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串

print('------------------------------')

print('hello\njollychic')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\njollychic')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

#不换行输出
print("li", end="")
print("wei", end="")

#查看变量数据类型
print(type(str))

#用isinstance判断数据类型
id = 1001
if isinstance(id, int):
    print('id is int')
else:
    print("id is not int")

#type不会认为子类是一种父类
#isinstance会认为子类是一种父类

#列表。列表中的元素类型可以不相同
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']

print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表

# 为多个变量赋值
a = b = c = 1001
print(a, b, c)

#为多个变量指定多个对象
a, b, c = 1, 2, "li"
print(a, b, c)

#元组 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。元组中的元素类型也可以不相同
tuple = ("li", "wei", "jun", 1001)
print(tuple) #输出完整元组
print(tuple[0])#输出元组第一个元素
print(tuple[1:3])#输出第二个元素到第三个元素
print (tuple[2:])# 输出从第三个元素开始的所有元素
print(tuple * 2)#输出元组两次

#set集合
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素