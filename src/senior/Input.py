#! /usr/bin/python3

s = 'Hello, Runoob'

#  str 函数返回一个用户易读的表达形式。repr 产生一个解释器易读的表达形式。
print(str(s), repr(s))

#12的前面补3个0
zfil = '12'.zfill(5)
print(zfil)

# format的使用
print("{}网址：{}".format("百度", "www.baidu.com"))

table = {"google":1, "runoob":2, "taobao":3}
for name, num in table.items():
    print("{0:10}==>{1:10d}".format(name, num))


# str = input("请输入：")
# print("你输入的内容是：", str)


# 追加两行数据到文件
# file = open("D:\\foo.txt", "a+")
# file.write("python是一个非常好的语言\n是的，非常好！\n")
# file.close()

# 读取文件中的数据
# file = open("D:\\foo.txt", "r")
# file_string = file.read()
# print(file_string)
# file.close()


# 迭代文件对象，读取每一行
file = open("D:\\foo.txt", "r")
for line in file:
    print(line, end="")
file.close()


