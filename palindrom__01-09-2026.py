#check Number is palindrom or not
def isPalindromM1(nums):
  if nums == int(str(nums)[::-1]):
    return True
  else:
    return False

# print(isPalindromM1(1223))

#second Method

def isPalindromM2(data):
  nums = data
  revNums = 0
  while nums>0:
    ld = nums % 10
    revNums = ( revNums * 10 ) + ld
    nums = nums // 10

  if data == revNums:
    return True
  else:
    return False


print(isPalindromM2(1221))