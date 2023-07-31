import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    result = []
    s_new = s.replace(" ", "")
    len_s = len(s_new)

    sqrtL = math.sqrt(len_s)
    l_sqrt = math.floor(sqrtL)
    r_sqrt = math.ceil(sqrtL)

    if l_sqrt * r_sqrt < len_s:
        l_sqrt = r_sqrt

    for i in range(l_sqrt): # 0 1 2 
        try:
            result.append(s_new[i*r_sqrt: i*r_sqrt+r_sqrt])
        except:
            result.append(s_new[i*r_sqrt:])
    result2 = []

    for c in range(r_sqrt):
        tmp = ""
        for i in range(l_sqrt):
            try:
                tmp += result[i][c]
            except:
                continue
        result2.append(tmp)

    return ' '.join(result2)

if __name__ == '__main__':

    s = input()

    result = encryption(s)
    print(result)
