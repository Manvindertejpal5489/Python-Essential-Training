#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# significance of white spaces

import platform

def main():
    print("component of main block")
    message()
# message func is a part of the main function
def message():
    print('This is python version {}'.format(platform.python_version()))
    print("thsi iis line 2 of this block")
    print("a block gets defined by its level of indentation")
# above is an example of a block
if __name__ == '__main__': main()
