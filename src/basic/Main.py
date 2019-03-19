#!/usr/bin/python3

import keyword


print("Hello Python")

"""
打印
关键字列表
"""

print(keyword.kwlist)

# 缩进
if True:
    print("true")

# 多行书写需要用 \ 来连接
item_one = "one"
item_two = "two"
total = item_one + \
        item_two
print(total)

# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)
total = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']
print(total)
