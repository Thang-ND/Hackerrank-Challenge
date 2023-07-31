import math 
import os
import random
import re
import sys 
import decimal

def plusMinus(arr):
    posNum = 0 
    negNum = 0 
    zeroNum = 0
    n = len(arr)

    for i in range(len(arr)):
        if arr[i] > 0:
            posNum += 1
        elif arr[i] < 0:
            negNum += 1
        else:
            zeroNum += 1
    
    print(f"{round(posNum/n, 6):.6f}")
    print(f"{round(negNum/n, 6):.6f}")
    print(f"{round(zeroNum/n, 6):.6f}")


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split(" ")))
    plusMinus(arr)