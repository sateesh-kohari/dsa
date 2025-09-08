#check array is sorted
def isSorted(data):
  n = len(data)
  for i in range(n-1):
    if data[i] > data[i+1]:
      return False
  return True

data = [2,5,6,8,9,10,20]
# data = [1,2,8,5,3,10,14,15]
# print(isSorted(data))
