a = [x * 2 for x in range(1, 20) if x % 5 == 0]
print(type(a))
print(a)

for x in range(1, 20):
  print(x)

cells = [(row, col) for row in range(1, 10) for col in range(1, 10)]  # 可以使用两个循环
print(type(cells))
for cell in cells:
  print(cell)
