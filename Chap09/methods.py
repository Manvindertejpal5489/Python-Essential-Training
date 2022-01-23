#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# a function that is associated with a class is called a method
# this provides an interface to the class and its objects


class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

#  here we have a method called type which serves both as a getter and a setter
    def type(self, t = None):# the first argument to the function is to  self and thats what makes it a method and not just a plane function
        #  in the above scenario the second argument give a default value to the object being defined by this method
        if t: self._type = t # if there is a value called t then type ia set to t and returned as t
        # if there is no value assigned then the object takes up the default value None
        return self._type  # in either scenario type is returned with a value - t/None
        #  the underscore _ designates this as a private variable marked for limiting its use outside this specific block

    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def main():
    a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
    a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')
    print(a0)
    print(a1)

if __name__ == '__main__': main()
