# 测试运算符的重载
a = 20
b = 30
c = a + b
d = a.__add__(b)
print("c=", c)
print("d=", d)


class Person:
  def __init__(self, name):
    self.name = name

  def __add__(self, other):
    if isinstance(other, Person):
      return "{0}--{1}".format(self.name, other.name)
    else:
      return "不是同类对象，不能相加"

  def __mul__(self, other):
    if isinstance(other, int):
      return self.name * other
    else:
      return "不是同类对象，不能相乘"


p1 = Person("张三")
p2 = Person("李四")

x = p1 + p2
print(x)

print(p1 * 3)