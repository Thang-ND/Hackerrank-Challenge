#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#


def absolutePermutation(n, k):
    # Write your code here 4 2  [1,2,3,4]
    a = list(range(n+1))
    if k == 0:
        return a[1:]

    if n%2 ==1:
        return [-1]
    
    for i in range(1, n-k+1):
        if a[i] == a[i+k] - k:
            a[i], a[i+k] = a[i+k], a[i]
        elif abs(i - a[i]) != k:
            return [-1]
        
    for i in range(n-k+1, n+1):
        if abs(i-a[i]) != k:
            return [-1]
        
    return a[1:]
    


if __name__ == '__main__':
    tmp = []
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)
        print(result)


