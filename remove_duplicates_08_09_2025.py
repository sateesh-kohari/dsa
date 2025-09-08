#remove duplicates
def removeDuplictes(data):
  data = data
  n = len(data)
  res = {}
  for i in range(n):
    if data[i] not in res:
      res[data[i]] = 0

  k = 0
  for j in res:
    data[k] = j
    k+=1
  # print(res)
  print(data)
  return k

# data = [1,1,1,2,3,4,4,7,9,9,9,10]
# removeDuplictes(data)



def removeDuplictesM2(data):
  n = len(data)
  freq = []
  count = 0
  for num in data:
    if num not in freq:
      count += 1
      freq.append(num)
  print(freq)
  return count


def removeDuplictesM3(data):
  n = len(data)
  i = 0
  j = i + 1
  while j < n:
    if data[i] < data[j]:
      data[i+1], data[j] = data[j], data[i+1]
      i += 1
    j += 1
  print(data)
  return i+1

data = [1,1,1,2,3,4,4,7,9,9,9,10]
removeDuplictesM3(data)