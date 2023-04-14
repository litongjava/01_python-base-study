# 测试重写object的__str__()

class Person:  # 默认继承object类

  def __init__(self, name,age):
    self.name = name
    self._age = age

  def __str__(self):
    return "名字是：{0},年龄是:{1}".format(self.name,self._age)


p = Person("Ping", 18)
print(p)