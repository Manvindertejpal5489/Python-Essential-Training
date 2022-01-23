#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

    # a class is how an object is defined

class Duck: # here we have a class definition begining with the keyword class 
# after the keyword class lies the name of the class followed by a :
# this is followed by data in the form of some variables
 
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

# this followed by some methods or behaviours in the form of some function definitions
# the first parameter of a method is always self which could had been anything but is set to self by protocol
# the first argument is self which is a reference to the object being put in the class
# everything deefined subsequently in the class is dereferenced from self to get the instantiated object version of it
# the period . operator is used to dereference the object - The same is true outside of the class

    def quack(self):
        print(self.sound)

# this method used data from the first variable 

    def move(self):
        print(self.movement)

# this method used data from the second variable

def main():
    donald = Duck()
    donald.quack()
# donald is the object, quack is the method
# the period . operator is used to dereference the object
    donald.move()
# donald is the obect, move is the method

if __name__ == '__main__': main()
