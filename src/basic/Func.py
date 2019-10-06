#! /usr/bin/python3

# 定义函数
def hello():
    print("hello python")


hello()


def area(width, height):
    return width * height


def print_welcome(name):
    print("welcome", name)


width = 12
height = 10
print(print_welcome(name="aubrey"), "width=", width, "height=", height, "area=", area(width, height))


def change_me(list_p):
    list_p.append(5)


list_param = [1, 2, 3, 4]
change_me(list_param)
print("list=", list_param)


def print_info(name, age=25):
    print("name=", name, "age=", age)


print_info(name="aubrey")


# 不定长参数
def print_param(arg1, *params):
    print(arg1)
    print(params)


print_param(70, 50, 60)


def print_param2(arg1, **params):
    print(arg1)
    print(params)


print_param2(70, a=50, b=60)


# 匿名函数
sum_lambda = lambda arg1, arg2: arg1 + arg2


print("sum=", sum_lambda(2, 5))
