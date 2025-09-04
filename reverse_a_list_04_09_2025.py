#reverse a list
arr = [5,7,3,2,6,1,5,9, 10]
# print(arr[::-1])
# print(arr.reverse())

def reverseM1(arr):
  rev = []
  for i in range(len(arr)-1,-1, -1):
    rev.append(arr[i])
  return rev

def reverseM2(data):
  left = 0
  right = len(arr) - 1
  while left < right:
    data[left], data[right] = data[right], data[left]
    left += 1
    right -= 1
  
  return data

# print(reverseM2(arr))

def reverseM3(arr, left , right):

  if left >= right:
    return

  arr[left], arr[right] = arr[right], arr[left]
  reverseM3(arr, left+1 , right-1)
  return arr


print(reverseM3(arr, 0 , len(arr)-1))
