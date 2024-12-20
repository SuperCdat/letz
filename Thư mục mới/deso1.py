def bai1():
  print("Bài 1:")
  x = input("Số: ")

  getting = 0
  for i in x:
    getting += int(i)
  print("Độ dài:", len(x))
  print("Tổng các số:", getting)
  print("Số lớn nhất:", max(x), "\n")

def bai2():
  print("Bài 2:")
  x = int(input("dài "))
  y = int(input("rộng "))
  print("Chu vi:", 2*(x+y))
  print("Diện tích:", x*y, "\n")

def bai3():
  print("Bài 3:")
  x = input("Dãy chữ số:\n").replace(" ", "")

  numbercount = 0
  numbernumber = 0
  stringstring = ""

  for i in x:
    try:
      numbernumber += int(i)
      numbercount += 1
    except:
      stringstring += i

  print("Số lượng số:", numbercount)
  print("Tổng các số:", numbernumber)
  print("Dãy chữ:", stringstring, "\n")

def bai4():
  print("Bài 4:")
  x = input("Gồm bao nhiêu số: ")
  y = input("Dãy số: ").split(" ")

  sumy = 0
  for i in y:
    sumy += int(i)

  gotnumber = []
  numbercount = dict({})
  for i in y:
    if i not in gotnumber:
      gotnumber.append(i)
      counted = 0
      for i2 in y:
        if (i == i2):
          counted += 1
      numbercount[str(i)] = counted

  print("Tổng các số:", sumy)
  for i in numbercount:
    print(i + ":" + str(numbercount[i]))

  print("\n")

# bai1()
# bai2()
# bai3()
# bai4()



