# by luffycity.com
# 1，老男孩好声⾳选秀⼤赛评委在打分的时候呢,
# 可以进⾏输入. 假设, 老男孩有10个评委.
# 让10个评委进⾏打分, 要求, 分
# 数必须⼤于5分, ⼩于10分
# count = 1
# while count <= 10:
#     fen = int(input("请第%s号评委评分:" % count))
#     if fen < 5 or fen > 10:
#         print("是不是傻?")
#         continue
#     else:
#         print("第%s位评委打分为:%s" %(count, fen) )
#     count = count + 1


# 电影投票. 程序先给出⼀个⽬前正在上映的电影列表. 由⽤户给每⼀个电影投票.
# 最终 将该⽤户投票信息公布出来
# lst = ['⾦瓶梅', '解救吾先⽣', '美国往事', '⻄⻄⾥的美丽传说']
# 结果: {'⾦瓶梅': 99, '解救吴先⽣': 80, '美国往事': 6, '⻄⻄⾥的美丽传说': 23}

# lst = ['金瓶梅', '解救吾先生', '美国往事', '西西里的美丽传说']
# dic = {}
# for el in lst:
#     fen = input("请给%s电影打分" % el)
#     dic[el] = fen
# print(dic)

cars = ["鲁A12345","鲁B12345", "沪B45678", "黑A12345", "黑A12345"]
locals = {"鲁": "山东", "沪": '上海', "黑": '黑龙江'}
result = {}
for car in cars: # car 车牌子
    first_name = car[0]
    location = locals[first_name] # 山东
    # 进行统计
    if result.get(location) == None: # 如果获取当前位置. 找不到对应的车辆的数量
        result[location] = 1 # 第一辆车
    else:
        result[location] = result[location] + 1 # 第n量

print(result)



