#check number is armstrong or not
def isArmstrongM1(data):
  nums = str(data)
  n = len(nums)

  result = 0
  for digit in nums:
    result += int(digit) ** n
  
  if result == data:
    return True
  else:
    return False

# print(isArmstrongM1(153))


#second method

def isArmstrongM2(data):
    nums = data
    n = len(str(data))
    total = 0

    while nums > 0:
      digit = nums % 10
      total += digit ** n
      nums //= 10

    return True if data == total else False


print(isArmstrongM2(152))