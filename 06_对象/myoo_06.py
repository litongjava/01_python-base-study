# 测试继承的基本使用

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age  # 私有属性

  def say_age(self):
    print("年龄，年龄，我也不知道")


class Student(Person):
  def __init__(self, name, age, score):
    # 构造函数中包含调用父类构造函数。根据需要，不是必须。子类并不会自动调用父类的__init__()，我们必须显式的调用它。
    Person.__init__(self, name, age)
    self.score = score


# Student-->Person-->object类
print(Student.mro())

s = Student("Ping", 18, 60)
s.say_age()
print(dir(s))
print(s._Person__age)
