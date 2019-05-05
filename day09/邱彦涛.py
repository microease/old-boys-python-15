'''
一.
abcdefg


2.
print("周润发")


3.
print("周杰伦)


x = 9
x //= 3
print(x)

a = (1,)
print(type(a))

'''
# s1 = "老男孩"
# s2 = s1.encode("utf-8")
# # s2现在是utf-8 的 bytes
# # 变回字符串
# s2.decode("utf-8").encode("gbk")


# 分别使用while循环，和for循环计算1-3+5-7+9-11...99的结果
# count = 1 # 第几个数
# sum = 0
# for i in range(1,100, 2):
#     if count %2 == 0:
#         sum = sum - i
#     else:
#         sum = sum + i
#     count += 1
# print(sum)

# sum = 0
# fuhao = 1
# for i in range(1, 100, 2):
#     sum = sum + (i*fuhao)
#     fuhao = -fuhao # 关键
# print(sum)

# index = 1
# while index < 100:
#     print(index)
#     index = index + 2


# s = "jay:周杰伦|jj:林俊杰|gg:太白|sb:alex"
# dic = {}
# lst = s.split("|")
# for el in lst:  # jay:周杰伦
#     ll = el.split(":")
#     key = ll[0]
#     value = ll[1]
#     dic[key] = value
# print(dic)

# 实现一个整数加法计算器：（5分）
# 如：content = input('请输入内容:')  # 如用户输入：5+8+7....(最少输入两个数相加)，将最后的计算结果添加到此字典中(替换None)：
# dic={'最终计算结果':None}
# content = input('请输入内容:') #  5+8+7
# # 去掉空格
# content = content.replace(" ", "")
# lst = content.split("+") # 切割之后的结果['5','8','7']
# sum = 0
# for el in lst:
#     sum = int(el) + sum
# print(sum)
# dic['最终计算结果'] = sum


# 开发敏感词语过滤程序，提示用户不停的输入评论内容，
# 如果用户输入的内容中包含特殊的字符则将用户输入的内容中的敏感词替换成等长度的*
# （苍老师替换成***），并添加到列表中，
# 如果用户输入的内容中没有敏感词汇则直接添加到列表中，
# 最终将列表中的全部内容进行打印
# 	敏感词列表：li = [‘苍老师’, ‘东京热’, ‘武藤兰’, ‘波多野结衣’, ‘alex’](5分)
# li = ['苍老师', '东京热', '武藤兰', '波多野结衣', 'alex']
# result = []
# while 1:
#     content = input("请输入你的评论:")
#     if content.upper() == 'Q':
#         break
#     for el in li:
#         if el in content:
#             content = content.replace(el, "*"*len(el))
#     result.append(content)


# 让用户随机输入10个数，
# 将这10个数保存在列表中，
# 将所有大于 55 的值保存至字典的第一个key的值中，
# 将小于 55 的值保存至第二个key的值中。(6分)
# lst = []
# for i in range(10):
#     c = input("请输入一个数:")
#     lst.append(int(c))
#
# key1 = []
# key2 = []
# for el in lst:
#     if el > 55:
#         key1.append(el)
#     elif el < 55:
#         key2.append(el)
#
# dic = {"key1":key1, "key2":key2}
# print(dic)


# 6、车牌区域划分，给出一下车牌和地点信息对照，请根据车牌信息，分析出各省的车牌持有数量。
# cars = ['鲁A32444', '鲁B12333', '京B8989M', '黑C49678', '黑C46555', '沪B25041', '黑C34567']
# locations = {'沪': '上海', '京': '北京', '黑': '黑龙江', '鲁': '山东', '鄂': '湖北', '湘': '湖南'}
# result = {}
# for car in cars: # car 是车牌子
#     result[locations[car[0]]] = result.get(locations[car[0]], 0) + 1 # 上海:1, 北京:1, 黑龙江
# print(result)

# 7. 按要求完成下列转化。(8分)
# list3 = [
#     {"name": "alex", "hobby": "抽烟"},
#     {"name": "alex", "hobby": "喝酒"},
#     {"name": "alex", "hobby": "烫头"},
#     {"name": "alex", "hobby": "Massage"},
#     {"name": "wusir", "hobby": "喊麦"},
#     {"name": "wusir", "hobby": "街舞"},
#     {"name": "taibai", "hobby": "开车"},
#     {"name": "taibai", "hobby": "嫂子"},
#     ]
# list4= []
#
# for ren in list3: # {"name": "alex", "hobby": "抽烟"},
#     for el in list4:
#         if el['name'] == ren['name']:
#             el['hobby_list'].append(ren['hobby'])
#             break
#     else:
#         dic = {}
#         dic['name'] = ren['name']
#         dic['hobby_list'] = [ren['hobby']]
#         list4.append(dic) # 第一个人进去
# print(list4)


list4 = [
    {"name": "alex", "hobby_list": ["抽烟", "喝酒", "烫头", "Massage"]},
    {"name": "wusir", "hobby_list": ["喊麦", "街舞"]},
]
# 将list3 这种数据类型转化成list4类型,你写的代码必须支持可拓展,
# 比如list3 数据在加一个这样的字典{"name": "wusir", "hobby": "溜达"},	你的list4{"name": "wusir", "hobby_list": ["喊麦", "街舞", "溜达"],
# 或者list3增加一个字典{"name": "太白", "hobby": "开车"},
# 你的list4{"name": "太白", "hobby_list": ["开车"],无论按照要求加多少数据,你的代码都可以转化.如果不支持拓展,则4分,支持拓展则8分

