# 组合测试
class MobilePhone:
  def __init__(self, cpu, screen):
    self.cpu = cpu
    self.screen = screen


class CPU:
  def calculate(self):
    print("计算，算个12345")


class Screen:
  def show(self):
    print("显示一个好看的画面，亮瞎你的钛合金大眼")


c = CPU()
s = Screen()
m = MobilePhone(c, s)
m.cpu.calculate()  # 通过组合，我们也能调用cpu 对象的方法。相当于手机对象间接拥有了“cpu的方法”
m.screen.show()
