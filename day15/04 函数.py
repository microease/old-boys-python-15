# by luffycity.com

def func():
    print("你好")


def func2():
    print("不好")


def gn(fn):  # fn是一个参数. 根据实参给的值的变化而变化
    print(fn.__name__)  # func
    fn()


gn(func2)
