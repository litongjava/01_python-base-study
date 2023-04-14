# 测试类方法
class Student:
  company = "PingPing"  # 类属性

  @classmethod
  def printCompany(cls):
    print(id(cls))
    print(cls.company)


Student.printCompany()
print(id(Student))
