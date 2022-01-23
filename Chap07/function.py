#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


# the special variable _name_ will return the name of the current module
# if __name__ == '__main__': main()
# This helps bypass the the paraadox of calling on the function kitten before it gets defined

# mod 
# def main():
#     kitten(5)

# def kitten(n):
#         print(f'{n} Meow.')

# if __name__ == '__main__': main()


def main():
    x = kitten()
    print(type(x),x)
    

def kitten():
    print('Meow.')
    return True

if __name__ == '__main__': main()
