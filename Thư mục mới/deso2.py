import math

def bai1():
  x = int(input("A: "))
  y = int(input("B: "))

  primelist = []
  for i in range(2, x + y):
    isprime = True
    for ix in range(2, i):
      if i % ix == 0:
        isprime = False
    if isprime:
      primelist.append(i)


  print("uoc chung lon nhat:", math.gcd(x, y))
  print("tong so:", x + y)
  print("so nguyen to:", str(primelist).replace("[", "").replace("]", ""))

def bai2():
  x = input("S: ")

  s1 = ""
  s2 = ""

  for i in x:
    try:
      s2 += str(int(i))
    except:
      s1 += i

  sums2 = 0
  for i in s2:
    sums2 += int(i)

  print("s1:", s1)
  print("s2:", s2)
  print("s1 hoa:", s1.upper())
  print("so chu s1:", len(s1))
  print("tong s2:", sums2)

def bai3():
  xx = input("N: ")
  x = input("Day N: ").split(" ")

  for i in x:
    x[x.index(i)] = int(i)


  print(sum(x))
  print("n lon nhat: ", max(x))
  print("vi tri n lon nhat: ", x.index(max(x)) + 1)
  print("n nho nhat: ", min(x))
  print("vi tri n nho nhat: ", x.index(min(x)) + 1)
  x.sort()
  print("n sap xep: ", str(x).replace("[", "").replace("]", "").replace(",", ""))

# bai1()
# bai2()
# bai3()