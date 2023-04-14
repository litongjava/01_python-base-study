# 测试方法的重写

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age  # 私有属性

  def say_age(self):
    print("我的年龄:", self.__age)

  def say_name(self):
    print("我的名字是{0}".format(self.name))


class Student(Person):
  def __init__(self, name, age, score):
    Person.__init__(self, name, age)  # 必须显式的调用父类初始化方法，不然解释器不会去调用
    self.score = score

  def say_score(self):
    print(self.name, "的分数是：", self.score)

  def say_name(self):
    '''重写了父类的方法'''
    print("报告老师，我的名字是：{0}".format(self.name))


s1 = Student("Litong", 18, 80)

s1.say_score()
s1.say_name()
s1.say_age()
