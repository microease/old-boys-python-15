# by luffycity.com

name = "aleX leNb"
count = 0
for c in name:
    if c == 'e':
        print(count)
    count = count + 1
# # 请输出 name 变量对应的值中 "e"  所在索引位置?
index = 0 # 手动记录一下索引
for c in name:
    if c == 'e': # 如果字母是e
        print(index)    # 打印索引
    index = index + 1

# s = "123a4b5c"
# # 有字符串s = "123a4b5c"
# # 1) 通过对s切⽚形成新的字符串s1,s1 = "123"
# print(s[:3])
# # 2) 通过对s切⽚形成新的字符串s2,s2 = "a4b"
# print(s[3:6])
# # 3) 通过对s切⽚形成新的字符串s3,s3 = "1345"
# print(s[::2])
# # 4) 通过对s切⽚形成字符串s4,s4 = "2ab"
# print(s[1:7:2])
# # 5) 通过对s切⽚形成字符串s5,s5 = "c"
# print(s[-1])
# # 6) 通过对s切⽚形成字符串s6,s6 = "ba2"
# print(s[-3::-2])

# s = "asdfer"
# for c in s:
#     print(s)


# s = "fklasjdfl"
# for c in s:
#     print(c+"sb")

# s = "321"
# for c in s:
#     print("倒计时%s秒" % c)
# else:
#     print("出发")

# 实现⼀个整数加法计算器(两个数相加)：
# 如：content = input("请输⼊内容:") 用户输⼊：5+9 或5+ 9 或5 + 9，然后进
# ⾏分割再进⾏计算。

# shizi = input("请输入你要计算的内容:")
# # 所有的空格干掉
# shizi = shizi.replace(" ", "") # 5+9
# lst = shizi.split("+") # 用+切割. 切割的结果是list
# print(int(lst[0])+ int(lst[1]))


#计算⽤户输⼊的内容中有⼏个整数（以个位数为单位）。
# 如：content = input("请输⼊内容：")   # 如fhdal234slfh98769fjdla
# zhengshu = 0
# content = input("请输⼊内容：")
# for c in content:
#     if c.isdigit():
#         zhengshu = zhengshu + 1
#
# print(zhengshu)

# 、写代码，完成下列需求：
# ⽤户可持续输⼊（⽤while循环），⽤户使⽤的情况：
# 输⼊A，则显示⾛⼤路回家，然后在让⽤户进⼀步选择：
# 是选择公交⻋，还是步⾏？
# 选择公交⻋，显示10分钟到家，并退出整个程序。
# 选择步⾏，显示20分钟到家，并退出整个程序。
# 输⼊B，则显示⾛⼩路回家，并退出整个程序。
# 输⼊C，则显示绕道回家，然后在让⽤户进⼀步选择：
# 是选择游戏厅玩会，还是⽹吧？
# 选择游戏厅，则显示 ‘ ⼀个半⼩时到家，爸爸在家，拿棍等你。’并让其
# 重新输⼊A，B,C选项。
# 选择⽹吧，则显示‘ 两个⼩时到家，妈妈已做好了战⽃准备。’ 并让其重
# 新输⼊A，B,C选项。

while 1:
    content = input("请输入你要选择的路线A, B, C:")
    if content == 'A':
        print("走大路回家")
        traffic = input("请问, 选择公交还是步行?")
        if traffic == '公交车':
            print("10分钟到家")
        elif traffic == "步行":
            print("20分钟到家")
        else:
            print("原地等待")
        break
    elif content == 'B':
        print("走小路回家")
        break
    elif content == 'C':
        print("绕路回家")
        play = input("请选择去网吧还是游戏厅?")
        if play == '网吧':
            print("两个⼩时到家，妈妈已做好了战⽃准备。")
        elif play == '游戏厅':
            print("一个半小时到家，爸爸在家，拿棍等你。")
        else:
            print("洗浴???")
    else:
        print("滚犊子别捣乱")



# count = 1
# sum = 0
# while count <= 99:
#     if count == 88:
#         count = count + 1
#         continue
#
#     if count %2 == 0:
#         sum = sum - count
#     else:
#         sum = sum + count
#     count += 1
# print(sum)


# 输⼊⼀个字符串，要求判断在这个字符串中⼤写字⺟，⼩写字⺟，数字，
# 其它字符共出现了多少次，并输出出来

# content = input("请输入一句话:")
# daxie = 0
# xiaoxie = 0
# shuzi = 0
# other = 0
#
# for c in content:
#     if c.isupper():
#         daxie += 1
#     elif c.islower():
#         xiaoxie += 1
#     elif c.isdigit():
#         shuzi += 1
#     else:
#         other += 1
#
# print(daxie, xiaoxie, shuzi, other)

# name = input("请输入你的名字:")
# location = input("请输入地点:")
# hobby = input("请输入爱好:")
#
# print("敬爱可亲的{} 最喜欢在{}干{}".format(name, location, hobby))


# first_names = '''赵钱孙李，周吴郑王。
# 冯陈褚卫，蒋沈韩杨。
# 朱秦尤许，何吕施张。
# 孔曹严华，金魏陶姜。
# 戚谢邹喻，柏水窦章。
# 云苏潘葛，奚范彭郎。
# 鲁韦昌马，苗凤花方。
# 俞任袁柳，酆鲍史唐。
# 费廉岑薛，雷贺倪汤。
# 滕殷罗毕，郝邬安常。
# 乐于时傅，皮卞齐康。
# 伍余元卜，顾孟平黄。
# 和穆萧尹，姚邵湛汪。
# 祁毛禹狄，米贝明臧。
# 计伏成戴，谈宋茅庞。
# 熊纪舒屈，项祝董梁。
# 杜阮蓝闵，席季麻强。
# 贾路娄危，江童颜郭。
# 梅盛林刁，钟徐邱骆。
# 高夏蔡田，樊胡凌霍。
# 虞万支柯，昝管卢莫。
# 经房裘缪，干解应宗。
# 丁宣贲邓，郁单杭洪。
# 包诸左石，崔吉钮龚。
# 程嵇邢滑，裴陆荣翁。
# 荀羊於惠，甄曲家封。
# 芮羿储靳，汲邴糜松。
# 井段富巫，乌焦巴弓。
# 牧隗山谷，车侯宓蓬。
# 全郗班仰，秋仲伊宫。
# 宁仇栾暴，甘钭厉戎。
# 祖武符刘，景詹束龙。
# 叶幸司韶，郜黎蓟薄。
# 印宿白怀，蒲邰从鄂。
# 索咸籍赖，卓蔺屠蒙。
# 池乔阴鬱，胥能苍双。
# 闻莘党翟，谭贡劳逄。
# 姬申扶堵，冉宰郦雍。
# 卻璩桑桂，濮牛寿通。
# 边扈燕冀，郏浦尚农。
# 温别庄晏，柴瞿阎充。
# 慕连茹习，宦艾鱼容。
# 向古易慎，戈廖庾终。
# 暨居衡步，都耿满弘。
# 匡国文寇，广禄阙东。
# 欧殳沃利，蔚越夔隆。
# 师巩厍聂，晁勾敖融。
# 冷訾辛阚，那简饶空。
# 曾毋沙乜，养鞠须丰。
# 巢关蒯相，查后荆红。
# 游竺权逯，盖益桓公。
# 万俟司马，上官欧阳。
# 夏侯诸葛，闻人东方。
# 赫连皇甫，尉迟公羊。
# 澹台公冶，宗政濮阳。
# 淳于单于，太叔申屠。
# 公孙仲孙，轩辕令狐。
# 钟离宇文，长孙慕容。
# 鲜于闾丘，司徒司空。
# 丌官司寇，仉督子车。
# 颛孙端木，巫马公西。
# 漆雕乐正，壤驷公良。
# 拓跋夹谷，宰父谷梁。
# 晋楚闫法，汝鄢涂钦。
# 段干百里，东郭南门。
# 呼延归海，羊舌微生。
# 岳帅缑亢，况郈有琴。
# 梁丘左丘，东门西门。
# 商牟佘佴，伯赏南宫。
# 墨哈谯笪，年爱阳佟。
# 第五言福，百家姓终。
# '''
# # 欧阳娜娜
# sum = ""
# name = input("请输入你的姓名:")
# for c in name:
#     sum = sum + c
#     if sum in first_names:
#         print("在百家姓中")
#         break
# else:
#     print("不在百家姓中")
