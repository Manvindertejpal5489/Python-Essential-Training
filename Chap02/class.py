#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    sound = 'Quack!!'
    walking = 'Walks like a duck.'
# this class contains two functions
# sometimes functions are called methods
# sometimes variables are called properties
    def quack(self): # The  first argument while defining a method inside a class is always NAMED self CONVENTIONALLY
        print(self.sound)

    def walk(self):
        print(self.walking)
        
# donald is a variable who we are assigning to the class Duck
def main():
    donald = Duck() # donald is now an object of the class duck
    donald.quack() # . is the reference operator to reference members of the object donald to the method called quack()
    donald.walk() # . is the reference operator to reference members of the object donald to the method called walk()

if __name__ == '__main__': main()
