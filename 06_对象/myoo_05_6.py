# @property装饰器的用法

class Employee:
  def __init__(self, name, salary):
    self.__name = name
    self.__salary = salary

  @property
  def salary(self):
    return self.__salary

  @salary.setter
  def salary(self, salary):
    if 1000 < salary < 50000:
      self.__salary = salary
    else:
      print("录入错误！薪水在1000--50000这个范围")


emp1 = Employee("高淇", 100)
print(emp1.salary)
emp1.salary = -200
print(emp1.salary)
