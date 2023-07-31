#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    num = ["zero minute", "one minute", "two minutes", "three minutes", "four minutes", "five minutes", "six minutes", "seven minutes", "eight minutes", "nine minutes" ,"ten minutes",
           "eleven minutes", "twelve minutes", "thirteen minutes", "fourteen minutes", "quarter", "sixteen minutes", "seventeen minutes", "eighteen minutes", 
           "nineteen minutes", "twenty minutes", "twenty one minutes", "twenty two minutes", "twenty three minutes", "twenty four minutes", "twenty five minutes",
             "twenty six minutes", "twenty seven minutes", "twenty eight minutes", "twenty nine minutes", "half"]

    hour = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]

    if m == 0:
        return hour[h] + " " + "o' clock"
    elif m <= 30:
        return num[m] + " " + "past" + " " + hour[h]
    else:
        return num[60-m] + " " + "to" + " " + hour[h+1]
if __name__ == '__main__':
    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)
    print(result)

