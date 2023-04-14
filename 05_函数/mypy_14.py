# 测试递归函数的基本原理

def factorial(n):
  if n == 1: return 1
  return n * factorial(n - 1)

for i in range(1, 6):
  print(i, '!=', factorial(i))
