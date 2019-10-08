#!/usr/bin/python3

#列表更新
list = ['Google', 'Runoob', 1997, 2000]

print("第三个元素为 : ", list[2])
list[2] = "2001a"
print("更新后的第三个元素为 : ", list[2])

#列表删除
print("原始列表", list)
del list[2]
print("删除列表元素后的列表", list)

#列表运算 相加
print(list + list)
#列表运算 相乘
print(list * 3)
#列表循环
for iLoop in list:
    print(iLoop, end=" ")

#返回列表中元素最大的
list = [3, 2, 10, 1]
print("列表中最大的元素是：", max(list))

#在末尾添加新的对象
list.append(13)
print(list)
#统计某个元素在列表中出现的个数
print(list.count(3))

a, b = 1, 2
a, b = b, a + b
print(a, b)

for i in range(-10, -100, -w30):
    print(i)
