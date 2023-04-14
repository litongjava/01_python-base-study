# 1. 定义一个函数实现反响输出一个整数。比如：输入3245，输出5432.
def resverse(number):
  if (number < 10):
    return number
  else:
    lastNumber = number % 10;
    number = (number - lastNumber) / 10
    retval=resverse(number)
    return lastNumber * 10 +retval;


print(resverse((3245)))

print(32 % 10)
