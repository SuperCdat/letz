def bai1():
  x = int(input("N: "))

  xdivisors = []
  for i in range(1, x + 1):
    if x % i == 0:
      xdivisors.append(i)

  xprimedivisors = []
  for i in xdivisors:
    if i != 1:
      isprime = True
      for ix in range(2, i):
        if i % ix == 0:
          isprime = False
      if isprime:
        xprimedivisors.append(i)


  print("uoc x:", str(xdivisors).replace("[", "").replace("]", ""))
  print("uoc x", len(xprimedivisors), "nguyen to:", str(xprimedivisors).replace("[", "").replace("]", ""))

def bai2():
  x = input("Xau: ")

  listing = []
  using = 0
  appendingletters = ""
  for i in x:
    if i != "¬":
      appendingletters += i
      
    else:
      if (using > 0 and listing[using - 1] != ""):
        using += 1
      if (appendingletters != ""):
        listing.append(appendingletters)
      appendingletters = ""

  shouldprint = ""
  for i in listing:
    if shouldprint == "":
      shouldprint += i
    else:
      shouldprint += "¬" + i

  print(shouldprint)

def bai3():
  xx = input("So so: ")
  x = input("Day so: ")

  numberlist = x.split(" ")

  print("so lon nhat:", max(x))
  print("vi tri so lon nhat:", numberlist.index(max(x)) + 1)

# bai1()
# bai2()
# bai3()