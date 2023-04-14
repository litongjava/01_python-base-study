class A:
  def aa(self):
    print("aa")


class B:
  def bb(self):
    print("bb")


class C(B, A):
  def cc(self):
    print("cc")


c = C()
c.cc()
c.bb()
c.aa()
