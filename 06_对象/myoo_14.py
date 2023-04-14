# 测试对象的浅拷贝、深拷贝
import copy


class MobilePhone:
  def __init__(self, cpu, screen):
    self.cpu = cpu
    self.screen = screen


class CPU:
  def calculate(self):
    print("算你个12345")
    print("cpu对象：", self)


class Screen:
  def show(self):
    print("显示一个好看的画面，亮瞎你的钛合金大眼")
    print("screen对象：", self)


c = CPU()
s = Screen()
m = MobilePhone(c, s)
m.cpu.calculate()
n = m  # 两个变量，但是指向了同一个对象
print(m, n)
m2 = copy.copy(m)  # m2 是新拷贝的另一个手机对象
print(m, m2)
m.cpu.calculate()
m2.cpu.calculate()  # m2 和m 拥有了一样的cpu 对象和screen 对象
m3 = copy.deepcopy(m)
m3.cpu.calculate()  # m3 和m 拥有不一样的cpu 对象和screen
