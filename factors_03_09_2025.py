#all factor of given number
def getFactorsM1(data):
  n = data//2 + 1
  result = []
  count = 0
  for i in range(1,n):
    count +=1
    if data%i == 0:
      result.append(i)
  result.append(data)
  print(count)

  return result

# print(getFactorsM1(10))
from math import sqrt
def getFactorsM2(data):
  n = int(sqrt(data)) + 1
  result = []
  for i in range(1,n):
    if data % i == 0:
      result.append(i)
      temp = data//i
      if temp != i:
        result.append(temp)

  return sorted(result)


print(getFactorsM2(36))