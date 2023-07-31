#!/bin/python3

import math
import os
import random
import re
import sys
from queue import PriorityQueue

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    rank = []
    distinct_rank = sorted(set(ranked), reverse=True)
    l = len(distinct_rank)

    for p in player:
        left, right = 0, l
        while left < right:
            mid = (left + right)//2
            if distinct_rank[mid] == p:
                left = mid
                break
            elif distinct_rank[mid] > p:
                left = mid + 1 
            else: 
                right = mid 

        rank.append(left + 1)
    return rank

if __name__ == '__main__':
    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)
    print(result)

