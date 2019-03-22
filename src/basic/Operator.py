#!/usr/bin/python3

# 运算符

#算术运算符
# 2的3次方
print(2 ** 3)
#取整数,向下取整
print(2 // 3)

##比较运算符
one = 1
two = 1
if one == two:
    print("one = two")
else:
    print("one != two")

##赋值运算符
#幂赋值运算符
c = 2
c **=3
print(c)

#逻辑运算符
a = 10
b = 10
if a and b:
    print("true")
else:
    print("false")

a = 0
if a and b:
    print("true")
else:
    print("false")

#成员运算符 in  not in  针对字符串、列表、元组
list = [1, 2, 3, 4, 5]

if 5 in list:
    print(True)
else:
    print(False)

#身份运算符 用于比较两个对象的存储单元
a = 20
b = 20
if a is b:
    print(True)
else:
    print(False)

#等同于
if id(a) == id(b):
    print(True)
else:
    print(False)
#is 与 == 的区别 is 用于判断变量引用的对象是否为同一个， == 用于判断引用变量的值是否相等

