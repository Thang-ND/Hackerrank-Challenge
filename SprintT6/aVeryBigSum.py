import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split(" ")))
    result = aVeryBigSum(ar)
    print(result)