import math 
import os 
import random 
import re
import sys 
import datetime

def timeConversion(s):
    hour = int(s[0:2])
    min = int(s[3:5])
    sec = int(s[6:8])
    isAM = (s[8:10] == 'AM')

    if isAM:
        if hour == 12:
            hour = 0
    else:
        hour += 12
        if hour == 24:
            hour -= 12
    
    res = f"{hour:0>2}:{min:0>2}:{sec:0>2}"
    return res
    
if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)