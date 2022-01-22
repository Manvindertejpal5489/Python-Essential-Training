#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 90
y = 90

if x < y:
    print('x < y: x is {} and y is {}'.format(x, y))
    z = 23
elif x == y:
    print ('x = y: x is {} and y is {}'.format(x,y))
else :
    print('x > y: x is {} and y is {}'.format(x, y))
    q = 45

# print(q)
# print (z)

# Blocks are defined by the level of indentation
# Blocks do not define the scope of variables in python
# scope of variable is defined by functions, modules and objects
# however blocks do determine the flow of the given path
