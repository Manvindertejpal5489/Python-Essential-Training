#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
# key wor arguments are like list arguments for dictionaries instead of tuples


def main():
    #kitten(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')
    x = dict(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')
    kitten(**x)
def kitten(**kwargs):# conve tionally named as kwargs for key word arguments
    # it has 2 * instead of the single * for list arguments
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('Meow.')

if __name__ == '__main__': main()
