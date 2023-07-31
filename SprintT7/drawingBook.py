#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    drawers = n//2 + 1
    pos = p//2 + 1
    return min(abs(p-1), abs(drawers-p))

if __name__ == '__main__':


    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(result)
