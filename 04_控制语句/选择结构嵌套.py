#或者也可以用下面代码更少的方法。不过，需要大家思考为什么这么写了
score = int(input("请输入一个在0-100 之间的数字："))
degree = "ABCDE"
num = 0
if score>100 or score<0:
  score = int(input("输入错误！请重新输入一个在0-100 之间的数字："))
else:
  num = score//10
  if num<6:num=5

  print("分数是{0},等级是{1}".format(score,degree[9-num]))