#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
# a generator is a special class of function that works as an iterator
# instead of returning a single value a generator returns a string of values

def main():
    for i in inclusive_range(40):
        print(i, end = ' ')
    print()

def inclusive_range(*args): # using a variable arguments list
    numargs = len(args) # number of args is the length
    start = 0
    step = 1
    
    # conditions to initialize parameters
    if numargs < 1: # number of arguments < 1
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # generator
    i = start
    while i <= stop:
        yield i # yeild is return value for a generator
        i += step

if __name__ == '__main__': main()
