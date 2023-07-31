import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    n = len(arr)
    lR = sum(arr[i][i] for i in range(n))
    rR = sum(arr[i][n-i-1] for i in range(n))
    return abs(lR - rR)

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split(" "))))

    result = diagonalDifference(arr)
    print(result)