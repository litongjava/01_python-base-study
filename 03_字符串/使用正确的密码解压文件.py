import zipfile

zfile = zipfile.ZipFile(r"G:\package\1+x 考题\211204AS1.zip", 'r')
password="499510"
try:
  zfile.extractall(path='.', pwd=password.encode())
  print("成功密码：", password)
except Exception as e:
  print(e)
  print("失败密码：", password)
  pass
