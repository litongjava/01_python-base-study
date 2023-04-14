#!/bin/python
# 测试函数也是对象
def print_star(n):
  print("*" * n)


print(print_star)
print(id(print_star))
c = print_star
c(3)
