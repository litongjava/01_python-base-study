sum_all = 0  # 1-100 所有数的累加和
sum_even = 0  # 1-100 偶数的累加和
sum_odd = 0  # 1-100 奇数的累加和
for num in range(101):
  sum_all += num
if num % 2 == 0:
  sum_even += num
else:
  sum_odd += num
print("1-100 累加总和{0},奇数和{1},偶数和{2}".format(sum_all, sum_odd, sum_even))
