#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# x = 'seven'.capitalize()# using string attributes # use single quote
'''x = 'seven "{1:<049}" "{0:>029}"'.format(3,8)
print(x.upper())
print(type(x))
print(x.capitalize())'''

'''a = 9
b = 10
x = f'trying an f function with {a:<09} & {b:>09}' # f string
print(x)
'''

x = 7 // 3 # gives quotient
x = 7 % 3 # gives remainder
x = .1 + .1 + .1 - .3 # computers sacrifise accuracy for precision
# Hence, floating points dont work well with money
print('x is {}' .format(x))
print (type(x))

# to use for money we need to import a module - decimal

from decimal import *
a = Decimal ('.10')
b = Decimal ('.20')
x = a + b + a + a
print (x)
print(type(x))

# x = True
x = 7 > 2
print (x)
print(type(x))
# bool type is for logical expressions and comparison ooperator


# how to inspect individual elements in a given structure 

x = (21, 9, 8.9, 'mam', [1,2,3,4,5,],9.87)
for i in x:
    print(f'component of tuple is: {i}')
    print(type (i))