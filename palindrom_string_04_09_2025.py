#palindrom string

def palindromM1(data, left, right):
  result = True
  while left < right:
    if data[left] != data[right]:
      result = False
      break
    left += 1 
    right -= 1
  return result


def palindromM2(data, left, right):
  if left < right:
    if data[left] != data[right]:
      return False
    palindromM2(data, left+1, right-1)
  return True


data = 'nitin1'
# print(palindromM2(data, 0 ,len(data)-1))

if data == data[::-1]:
  print(True)
else:
  print(False)