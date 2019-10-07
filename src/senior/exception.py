#! /usr/bin/python3

import sys


# try:
#     file = open("D:\\foo.txt")
#     s = file.readline()
#     i = int(s.strip())
#     print(i)
# except OSError as err:
#     print("OS error:{}".format(err))
# except ValueError:
#     print("could not convert data to an integer.")
# except:
#     print("Unexcepted error:", sys.exc_info()[0])
#     raise


# try except 语句还有一个可选的else子句，如果使用这个子句，
# 那么必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行。
# for arg in sys.argv[:]:
#     try:
#         f = open(arg, 'r')
#     except IOError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()

# Python 使用 raise 语句抛出一个指定的异常
# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise


# 你可以通过创建一个新的异常类来拥有自己的异常。异常类继承自 Exception 类，可以直接继承，或者间接继承
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError(2 * 2)
except MyError as e:
    print('My exception occurred, value:', e.value)
else:
    print("this is else")
finally:
    print("exec finally model")
