#! /usr/bin/python3

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

# 从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。
# （方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号）
list_one.pop(2)
print("list_one=", list_one)
list_one.pop()
print("list_one=", list_one)