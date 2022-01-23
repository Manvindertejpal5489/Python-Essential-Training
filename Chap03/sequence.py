# #!/usr/bin/env python3
# # Copyright 2009-2017 BHG http://bw.org/

# x = [ 1, 2, 3, 4, 5 ]
# x[3] = 97 # 3 is the index number in the fiven list which starts from 0
# for i in x:
#     print('i is {}'.format(i))
#     # print(f'i is {i} in {x}')

# u = (2,3,5,6,9,'f','jsdaf',True,'+')
# print(u)
# # this is a tuple
# # a tuple is imutable
# for v in u:
#     print('i is {}'.format(v)) 
#     # but it can be used like a list

# # creating a sequence using a range
# x = range(5,16)# the last number in range is 1 less tahn the numver given the bracket
# for i in x :
#     print(f'numbers in range are {i}')

# # creating a sequence using a range
# x = range(16)# the last number in range is 1 less tahn the numver given the bracket
# for i in x :
#     print(f'numbers in range are {i}')

# # creating a sequence using a range
# x = range(1,9)# the last number in range is 1 less tahn the numver given the bracket
# for i in x :
#     print(f'numbers in range are {i}')

    # dictionary
# from multiprocessing import Value


# from multiprocessing.sharedctypes import Value


x = {'one':23,'two':32, 'three':90}
x['two'] = 99
for k,v in x.items() :
    print(f' key : {k}, value : {v}'.format(k,v))