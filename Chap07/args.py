# #!/usr/bin/env python3
# # Copyright 2009-2017 BHG http://bw.org/

# def main():
#     kitten('meow', 'grrr', 'purr')

# def kitten(*args):# (*args) is the variable length argument list
#     # its traditional to name the variable name lisk as * args
#     if len(args):
#         for s in args:
#             print(s)
#     else: print('Meow.')

# if __name__ == '__main__': main()

def main():
    x = ('meow', 'grrr', 'purr','dumn')
    kitten(*x)

def kitten(*args):
        if len(args):
            for s in args:
                print(s)
            else: 
                print('Meow.')

if __name__ == '__main__': main()
