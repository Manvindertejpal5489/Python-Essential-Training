#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x =32
y = 23
print('''Hello, World.{}'.format(x))
using the format method 
in  python
in addindition to a multiline string usage.
'''.format(x))

print('hello world.% d'% y)
# %d is similar to {} 
# % is similar to .format()
# this is legacy code from pyrhon 2
# better use format 

# newer method from python 3.6 on wards uses a fstring
print(f'hello worlds.{44}')
# place an f before the string starts
# put the variable/ value in curly braces
# run the code
# fstring works by calling the format method

