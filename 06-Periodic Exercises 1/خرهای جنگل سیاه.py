n = int(input())

for i in range(n):
  x, y = map(int,input().split())
  # if y greater than x
  if y > x:
      print("-1")
  # if x is even but y is odd
  elif (x % 2 == 0 and y % 2 != 0) or (abs(x - y) >= 3):
    print("-1")
  # if x is odd but y is even
  elif x % 2 != 0 and y % 2 == 0:
    print("-1")
  # if x is even and y is even
  elif x % 2 == 0 and y % 2 == 0:
    print(x + y)
  # if x is odd and y is odd
  elif x % 2 != 0 and y % 2 != 0:
    print(x + y - 1)
  
