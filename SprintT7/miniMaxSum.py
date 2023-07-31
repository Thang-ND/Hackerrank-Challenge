#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    minVal = min(arr)
    maxVal = max(arr)
    sumArr = sum(arr)
    # return [sumArr - maxVal, sumArr - minVal]
    print(f"{sumArr-maxVal} {sumArr-minVal}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    res = miniMaxSum(arr)

