# coding:utf-8
# File Name：     test
# Description :
# Author :       microease
# Date：          2019/5/25
s = [1,2,3,3]
res = s.index(3)
print(res)
d = {1:2,2:3}
print(d.values())
print(3 in d)

N = input()
st = set(N)
sum = 0
for i in st:
    sum += int(i)
print(sum)


dict_name = {}
names = s.split()
for name in names:
    dict_name[name] = dict_name.get(name, 0) + 1
items = list(dict_name.items())
items.sort(key=lambda x:x[1], reverse=True)
print(items[0][0])