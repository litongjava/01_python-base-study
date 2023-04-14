class Person:
  def say_hi(self):
    print("hello")

  def say_hi(self, name):
    print("{0},hello".format(name))


p1 = Person()
#p1.say_hi() #不带参，报错：TypeError: say_hi() missing 1 required positional argument: 'name'
p1.say_hi("Ping")
