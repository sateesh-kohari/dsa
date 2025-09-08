#right rotate array

def rightRotateArray(data):
  data[:] =  data[-1] + data[:-1]
  print(data)


def rightRotateArrayM2(data):
  n = len(data)
  last = data[n-1]
  for i in range(n-1, -1,-1):
    data[i] = data[i-1]

  data[0] = last
  print(data)


data = [5,-2,3,9,0,6,10,7]
rightRotateArrayM2(data)