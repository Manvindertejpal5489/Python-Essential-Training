#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# print('Hello, World.')

def f1():
    print('this is f1')

x = f1

# f1()
# x()

# f1 can be called directly
# this is a wrapper function
def f1(j):
    def f2 ():
        print('this is before function call')
        j ()
        print('this is after function call')
    return f2
# this is a decorator - it assigns the name of f3 to the wrapper itself
@f1
def f3():
    print('this is f3')
# f3 is now wrapped inside the decorator function f1 by using @f1
f3()
# def h():
#     print('dilli door hai')
# x = f1()
# x ()
## f2() # not possible to call f2 directly as  f2 is wrapped inside of f1 function
# h =f1(h)
# h()
# now h in its origunal form is no longer available - its only available a wrapper for f1