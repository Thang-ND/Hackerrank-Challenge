import math
import os
import random
import re
import sys
#import numpy as np

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
def getCost(arr, magic):
    cost = 0
    for i in range(3):
        for j in range(3):
            cost += abs(arr[i][j] - magic[i][j])

    return cost


def formingMagicSquare(s):
    # Write your code here
    minCost = sys.maxsize
    magic = [
                [[8, 1, 6],[3, 5, 7],[4, 9, 2]],
                [[6, 7, 2],[1, 5, 9], [8, 3, 4]],
                [[2, 9, 4],[7, 5, 3],[6, 1, 8]],
                [[4, 3, 8],[9, 5, 1], [2, 7, 6]],
                [[6, 1, 8],[7, 5, 3],[2, 9, 4]],
                [[2, 7, 6],[9, 5, 1],[4, 3, 8]],
                [[4, 9, 2],[3, 5, 7],[8, 1, 6]],
                [[8, 3, 4],[1, 5, 9],[6, 7, 2]]
            ]

    for m in magic:
        cost = getCost(s, m)
        minCost = min(minCost, cost)
    return minCost

if __name__ == '__main__':

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print(result)
