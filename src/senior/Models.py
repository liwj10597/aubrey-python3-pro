#!/usr/bin/python3
# 文件名: using_sys.py

import sys
from src.basic import Func
from src.common.common_func import sum_common

print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')

Func.print_param2(70, a=50, b=60)

print(sum_common(2, 4))


