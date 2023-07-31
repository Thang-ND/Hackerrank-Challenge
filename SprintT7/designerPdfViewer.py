#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    # ord(char)-97
    width = len(word)
    height = [h[ord(word[i]) - 97] for i in range(width)]
    return max(height) * width

if __name__ == '__main__':


    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)
