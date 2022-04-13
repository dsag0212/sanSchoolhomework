# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 15:33:40 2022

@author: Win10
"""
#H1
for i in range(1,6):
    for x in range(i):
        print(i,end = '')
    print()
#H2
print()
for i in range(5,0,-1):
    for x in range(i):
        print(i,end = '')
    print()
#H3
print()
for i in range(9,0,-2):
    for x in range(i):
        print(i,end = '')
    print()
#H4 2 3 5 7 11 13 17 19
print()
for i in range(2,100):
    if i%2 != 0 and i%3 != 0 and i%4 !=0 and i%5 !=0 and i%6 != 0 and i%7 !=0 and i%8 != 0 and i%9 != 0 and i%10 != 0:
        print(i)