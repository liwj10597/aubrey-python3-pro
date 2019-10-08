#! /usr/bin/python3

import mysql.connector

mydb = mysql.connector.connect(
  host="172.31.0.68",       # 数据库主机地址
  user="bi_recommend",    # 数据库用户名
  passwd="se12pa@702"   # 数据库密码
)

print(mydb)
