# coding:utf-8
# File Name：     test1
# Description :
# Author :       microease
# Date：          2019/5/19
list1 = ["111", "222", "333", "444"]

result = []


def fun1(list):
    for i in range(len(list)):
        if i % 2 != 1:
            result.append(list1[i])
    print(result)

def fun2(list):
    return list[0::2]



fun1(list1)
print(fun2(list1))

