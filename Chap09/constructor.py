#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
#  an object is an instance of a class
# its created by calling the class itself a if it were a function

# The class constructor
class Animal:
    def __init__(self, type, name, sound):# special class method name  __init__
# this special class function works as a class initialiser or a constructor of a class
# here we pass the class constructor 3 arguments as the first argument is always self, and that is what makes this an object method because the self points to the object
# the 3 arguments are used to make the following 3 object variables

        self._type = type # these are object variables because they are never initialised until the object is defined
        self._name = name # the underscore at the begining of each of the object variables is put there traditionally 
        # the underscores are put there to discourage users from accessing these variables directly
        self._sound = sound


# the getters / accessers - these simply return the value of each of the object variables
    def type(self):
        return self._type
#  the accesser for object variable 1
    def name(self):
        return self._name
#  the accesser for object variable 2 and the next one for 3
    def sound(self):
        return self._sound

def print_animal(o): # function defined that expects an animal object and prints the script seen in the output
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound())) # here we use the getters or accessers to access the object variables
    #  the object is created using a class name as we use a function name


def main():
    a0 = Animal('kitten', 'fluffy', 'rwar') # Object a0 is created and its is initialised with various parameters
    #  the object a0 contains the name of the animal, type of animal and the sound that it makes
    a1 = Animal('duck', 'donald', 'quack') # object a1 is created and its is initialised with various parameters
    #  the object a1 contains the name of the animal, type of animal and the sound that it makes
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal('velociraptor', 'veronica', 'hello')) 
    # here the function print_animal is being called directly without creating an intermediary object.
    #  this works because function parameters work exactly like assignments in python


if __name__ == '__main__': main()
