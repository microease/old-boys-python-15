# by luffycity.com
# 模块
# random
    # 随机小数/随机整数/随机抽取/乱序
    # 10个数字 彩票的中奖号码
    # 随机验证码
    # 发红包
# time 和时间交互
    # 时间戳
    # 结构化时间 只能取值不能修改
    # 格式化时间  %m/%d/%Y %H:%M:%S
    # 时间戳 -localtime/gmtime->结构化时间 -strftime->格式化时间
    # 时间戳 <-mktime-结构化时间 <-strptime-格式化时间
# sys
    # sys.argv
        # 当你在命令行执行python文件,而不是在pycharm中执行这个文件的时候
            # 你的命令>>> python python文件的路径 参数1 参数2 参数3 ...
            # sys.argv = ['python文件的路径','参数1','参数2','参数3'...]
            # 好处:这些需要输入的参数不需要在程序中以input的形式输入了
        # 文件名: 文件路径不能有中文 所有的文件名都应该符合变量命名规范
            # 整个文件路径不能有空格 不支持中文
    # sys.path 模块搜索路径 是一个列表,这个列表中存的都是文件夹的绝对路径
        # 一个模块能被导入,是因为这个模块所在的文件夹在sys.path的列表中
        # 内置模块和第三方模块安装之后,不需要操作sys.path,直接用就行了
        # 如果一个模块导入不进来,那把这个模块的文件夹添加到sys.path中就行了
import sys
print(sys.path)
    # sys.modules
        # 所有被导入的模块的内存地址都存在sys.modules里
# os
# 创建和删除空文件夹
# 文件的重命名和删除
# listdir 查看当前目录下的所有文件夹和文件
# stat 获得文件的信息

# system popen getcwd chdir

# os.path.join 拼接目录


# D:\sylar\s15 >>> python day19\3.内容回顾.py
# C: >>> python D:\sylar\s15\day19\3.内容回顾.py
