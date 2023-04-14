import zipfile, time, threading

start_time = time.time()
flag = True  # 用于判断线程是否需要终止，为True时程序执行


def extract(password, file):
  try:
    file.extractall(path='.', pwd=password.encode('utf-8'))
    print("成功密码：", password)
    end_time = time.time()
    print('多线程破解压缩包花了%s秒' % (end_time - start_time))
    global flag
    flag = False  # 成功解压其余线程终止
  except Exception as e:
    print("失败密码：", password)
    pass


def main():
  zfile = zipfile.ZipFile(r"G:\package\1+x 考题\211204AS1.zip", 'r')
  for number in range(1, 999999, 1):
    if flag:
      canBeAPassword=str(number).rjust(6, "0")
      thr1 = threading.Thread(target=extract, args=(canBeAPassword, zfile))
      thr2 = threading.Thread(target=extract, args=(canBeAPassword, zfile))

      thr1.start()
      thr2.start()

      thr1.join()
      thr2.join()


if __name__ == '__main__':
  main()