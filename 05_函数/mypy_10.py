# 传递不可变对象时。不可变对象里面包含的子对象是可变的。则方法内修改了这个可变对象，源对象也发生了变化。

def test01(m):
  print("m:", id(m))
  print(m)
  m[2][0] = 888
  print(m)
  print("m:", id(m))

a = (10, 20, [5, 6])
print("a:", id(a))
test01(a)
