# 测试参数的类型：位置参数、默认值参数、命名参数
def f1(a, b, c):
  print(a, b, c)


f1(2, 3, 4)


# f1(2, 3)  # 报错，位置参数不匹配
def f01(a, b, c=10, d=20):  # 默认值参数必须位于普通位置参数后面
  print(a, b, c, d)


f01(8, 9)
f01(8, 9, 19)
f01(8, 9, 19, 29)


def f03(a, b, c):
  print(a, b, c)


f1(8, 9, 19)  # 位置参数
f1(c=10, a=20, b=30)  # 命名参数


def f04(a, b, *c):
  print(a, b, c)


f04(8, 9, 19, 20)


def f05(a, b, **c):
  print(a, b, c)


f05(8, 9, name='gaoqi', age=18)


def f06(a, b, *c, **d):
  print(a, b, c, d)


f06(8, 9, 20, 30, name='gaoqi', age=18)


def f07(*a, b, c):
  print(a, b, c)


# f07(2,3,4) #会报错。由于a 是可变参数，将2,3,4 全部收集。造成b 和c 没有赋值。
f07(2, b=3, c=4)
