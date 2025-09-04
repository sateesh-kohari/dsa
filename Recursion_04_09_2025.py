#Recursion
count = 0
def func():
  global count
  if count == 4:
    return
  count = count + 1
  
  count += 1
  print(f"hello {count}")
  func()
  

func()


#recursion with parameter
def func(data, n):
  if n == 0:
    return
  
  print(f"{data} {n}")
  func(data, n-1)

func('Hello', 3)





#print 1 to 5
def func(x,n):
  if x > n:
    return 
  
  func(x+1,n)
  print(x)
  
func(1,5)



#sum of n
def nSum(n ,x = 0):
  if n == 0:
    return 1

  return (n + nSum(n-1))

print(nSum(5))