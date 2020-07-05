''' Problem 13 '''
''' Write a program add.py, takes in 2 numbers as command line arguments and prints the sum'''

import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
add = x + y
print('addition:', add)