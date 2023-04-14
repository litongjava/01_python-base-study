class Animal:
  def shout(self):
    print("动物叫了一声")


class Dog(Animal):
  def shout(self):
    print("小狗，汪汪汪")


class Cat(Animal):
  def shout(self):
    print("小猫，喵喵喵")


def animalShout(a):
  if isinstance(a, Animal):
    a.shout()  # 传入的对象不同，shout 方法对应的实际行为也不同。


animalShout(Dog())
animalShout(Cat())
