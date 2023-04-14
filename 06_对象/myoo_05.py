# 测试类方法、静态方法
class Student:
  @staticmethod
  def add(a, b):  # 静态方法
    print("{0}+{1}={2}".format(a, b, (a + b)))
    return a + b


Student.add(20, 30)
