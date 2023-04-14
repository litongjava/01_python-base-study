#【操作】定义一个打印n 个星号的无返回值的函数
def print_star(n):
  print("*" * n)


print_star(5)


# 测试返回值的基本用法

def add(a, b):
  print("计算两个数的和：{0},{1},{2}".format(a, b, (a + b)))
  return a + b


def test02():
  print("sxt")
  print("gao")

  return  # return两个作用：1.返回值   2. 结束函数的执行

  print("hello")


def test03(x, y, z):
  return [x * 10, y * 10, z * 10]


c = add(30, 40)
print(add(30, 40) * 10)
d = test02()
print(d)

print(test03(4, 3, 2))
