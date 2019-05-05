# coding:utf-8
# File Name：     test01
# Description :
# Author :       microease
# Date：          2019/5/5
name = input("Name:")
age = input("Age:")
job = input("Job:")
hobby = input("Hobbie:")
info = '''
------------ info of %s ----------- #这⾥里里的每个%s就是⼀一个占位符，本⾏行行的代表 后⾯面拓拓号⾥里里的 name
Name : %s #代表 name
Age : %s #代表 age
job : %s #代表 job
Hobbie: %s #代表 hobbie
------------- end -----------------
''' % (name, name, age, job, hobby)  # 这⾏行行的 % 号就是 把前⾯面的字符串串 与拓拓号 后⾯面的 变量量 关联起来
print(info)
