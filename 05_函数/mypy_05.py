a = 100  # 全局变量


def f1():
  global a  # 如果要在函数内改变全局变量的值，增加global 关键字声明
  print(a)  # 打印全局变量a 的值
  a = 300


f1()
print(a)

a = 100


def f1():
  a = 3  # 同名的局部变量
  print(a)


f1()
print(a)  # a 仍然是100，没有变化

a = 100


def f1(a, b, c):
  print(a, b, c)
  print(locals())  # 打印输出的局部变量
  print("#" * 20)
  print(globals())  # 打印输出的全局变量


f1(2, 3, 4)
