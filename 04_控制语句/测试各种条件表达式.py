if 3: #整数作为条件表达式
  print("ok")
a = [] #列表作为条件表达式，由于为空列表，是False
if a:
  print("空列表，False")
s = "False" #非空字符串，是True
if s:
  print("非空字符串，是True")
c = 9
if 3<c<20:
  print("3<c<20")
if 3<c and c<20:
  print("3<c and c<20")
if True: #布尔值
  print("True")