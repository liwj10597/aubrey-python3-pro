#! /usr/bin/python3

import copy

list_one = [1, 2, 3]
# 1.把一个元素添加到列表结尾
list_one.append(4)
print("list_one=", list_one)

# 2.将list_two添加到list_one结尾
list_two = [5, 6]
list_one[len(list_one):] = list_two
print("list_one=", list_one)

# 3.功能同2，将list_three添加到list_one结尾
list_three = [7, 8]
list_one.extend(list_three)
print("list_one=", list_one)

# 4.删除列表中值为x的第一个元素,如果元素不在列表中，则报错
list_one.remove(3)
print("list_one=", list_one)

# 5.从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。
# （方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号）
list_one.pop(2)
print("list_one=", list_one)
list_one.pop()
print("list_one=", list_one)

# 6.返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
print("元素7第一次出现的位置索引=", list_one.index(7))

# 7.返回 x 在列表中出现的次数。
print("元素7在列表中出现的次数=", list_one.count(7))

list_one.append(3)
list_one.sort()
print("排序后list_one=", list_one)

# 8.倒排列表中的元素。
list_one.reverse()
print("倒排后list_one=", list_one)

list_four = list_one.copy()


# 9.浅拷贝，只拷贝第一层，2层以上 都是拷贝元素的地址
list_names = ["he", "li", ["liu", "li"], "fu", "chen"]
list_names2 = list_names.copy()
list_names[3] = "平"
print(list_names)
print(list_names2)

# 多维列表：，所以2层以后的元素，会跟着原来的列表改变
list_names[2][0] = "高"
print(list_names)
print(list_names2)

print("\n")
# 深拷贝：拷贝的内容 不会随原列表list_names内容的更改而更改
list_names = ["he", "li", ["liu", "li"], "fu", "chen"]
list_names2 = copy.deepcopy(list_names)
list_names[3] = "平"
print(list_names)
print(list_names2)

# 多维列表
list_names[2][0] = "高"
print(list_names)
print(list_names2)

# 列表推导式
vec = [2, 4, 6]
vec_two = [3 * x for x in vec]
print("vec_two=", vec_two)

vec_four = [3*x for x in vec if x > 3]
print("vec_four=", vec_four)

vec_three = [[x, x**2] for x in vec]
print("vec_three=", vec_three)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
freshfruit_two = [weapon.strip() for weapon in freshfruit]
print("freshfruit_two=", freshfruit_two)

# 矩阵转化
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
matrix_z = [[row[i] for row in matrix] for i in range(4)]
print(matrix_z)