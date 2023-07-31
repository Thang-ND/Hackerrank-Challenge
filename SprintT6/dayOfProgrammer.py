import math
import os
import random
import re
import sys 

def isLeap(year):
    if year == 1918:
        return -1
    elif year >= 1700 and year <= 1917:
        if year % 4 == 0:
            return 1
        else:
            return 0
    else:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return 1
        else: 
            return 0

def dayOfProgrammer(year):
    tmp = isLeap(year)
    if tmp == -1:
        return '26.09.1918'
    elif tmp == 1:
        return '12.09.' + str(year)
    else:
        return '13.09.' + str(year)

if __name__ == '__main__':
    year = int(input().strip())
    result = dayOfProgrammer(year)
    print(result)