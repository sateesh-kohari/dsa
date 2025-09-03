#store frequency in dictionary
def getFrequencyM1(data):
  result = {}
  for num in data:
    if num in result:
       result[num] += 1
    else:
      result[num] = 1

  # print(result)
  return result

data = [5,6,7,7,1,9,11,1,1,5,1,1]


def getFrequencyM2(data):
  result = {}
  for num in data:
    result[num] = result.get(num, 0) + 1

  return result

print(getFrequencyM2(data))