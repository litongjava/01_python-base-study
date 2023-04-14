class Person:
  def __init__(self,name,age):
    self.name=name;
    self.age=age;

  def say_age(self):
    print(self.name,"年龄是:",self.age)

obj=object()
print(dir(obj))

p=Person("Ping",18)
print(dir(p))