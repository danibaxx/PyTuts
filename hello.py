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

''' Problem 7 '''
''' Write a function count_digits to find number of digits in the given number '''
def count_digits(x):
  x = x
  return x
x = count_digits(str(12345))
# print(len(x)) # 5

'''Problem 8'''
''' Write a function istrcmp to compare two strings, ignoring the case. '''
''' >>> istrcmp('python', 'Python')
True
>>> istrcmp('LaTeX', 'Latex')
True
>>> istrcmp('a', 'b')
False '''
def istrcmp1(a, b):
  if a.lower() == b.lower():
    return True
  else:
    return False
lang = istrcmp1('python', 'Python')
# print(lang) # True

def istrcmp2(c, d):
  if c.lower() == d.lower():
    return True
  else:
    return False
glove = istrcmp2('LaTeX', 'Latex')
# print(glove) # True

def istrcmp3(e,f):
  if e.lower() == f.lower():
    return True
  else:
    return False
alpha = istrcmp3('a', 'b')
# print(alpha) # False



