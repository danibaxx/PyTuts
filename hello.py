''' Problem 2 '''
''' How many multiplications are performed when each of the following lines of code is executed? '''
numcalls = 0
def square(x):
  global numcalls
  numcalls = numcalls + 1
  return x * x

# print(square(5))
# print(square(2*5))
# 3

''' Problem 3 '''
''' What will be the output? '''
x = 1
def f():
  return x
# print(x) # 1
# print(f()) # 1

''' Problem 4 '''
''' What will be the output? '''
x = 1
def fx():
  x = 2
  return x
# print(x) # 1
# print(fx()) # 2
# print(x) # 1

''' Problem 5 '''
''' What will be the output? '''
x = 1
def fxy():
  x = 2
  y = x
  return x + y
# print(x) # 1
# print(fxy()) # 4
# print(x) # 1

''' Problem 6'''
''' What will be the output? '''
x = 2
def fxyz(a):
  x = a * a
  return x
y = fxyz(3)
# print(x,y) # 2, 9

