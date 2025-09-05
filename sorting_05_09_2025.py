#sorting
def sortAscM1(data):
  n = len(data)
  for i in range(n-1):
    for j in range(i,n):
      if data[i] > data[j]:
        data[i] , data[j] = data[j] , data[i]
  
  print(data)
  

# bubble sort
def sortAscM2(data):
  left = 0
  right = left + 1
  while True:
    if data[left] > data[right]:
      data[left] , data[right] = data[right] , data[left]
      right += 1


sortAscM2([5,7,8,4,1,6,9,2])