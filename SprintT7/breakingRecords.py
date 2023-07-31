#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    games = len(scores)
    curr_max, curr_min = scores[0], scores[0]
    res_max, res_min = 0, 0
    for i in range(1, games):
        if scores[i] < curr_min:
            res_min += 1
            curr_min = scores[i]
        elif scores[i] > curr_max:
            res_max += 1
            curr_max = scores[i]
        
    return [res_max, res_min]

if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)