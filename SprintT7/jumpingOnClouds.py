#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    curr = 0
    lenth = len(c)
    res = 0
    while curr + 2 < lenth:
        print(f"step: {curr}")
        if c[curr+2] == 0:
            curr = curr + 2
        else:
            curr = curr + 1
        
        res += 1 
    
    if curr != lenth-1:
        res += 1

    return res 

if __name__ == '__main__':

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print(result)
