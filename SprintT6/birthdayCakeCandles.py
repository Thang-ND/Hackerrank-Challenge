import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    n = len(candles)
    maxHeight = max(candles)
    result = 0
    for can in candles:
        result = result + (maxHeight == can)
    return result

if __name__ == '__main__':
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split(" ")))
    result = birthdayCakeCandles(candles)
