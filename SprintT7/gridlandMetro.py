import math
import os
import random
import re
import sys

#
# Complete the 'gridlandMetro' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY track
#
def cal_subtrack(arr):
    result = 0
    for x in arr:
        result += x[1] - x[0] + 1
    return result

def gridlandMetro(n, m, k, track):
    # Write your code here
    if k==0:
        return m*n
    track = sorted(track)
    res = 0
    sub_track = []
    sub_track.append([track[0][1], track[0][2]])
    
    for i in range(1, k):
        area = [track[i][1], track[i][2]]
        if track[i][0] != track[i-1][0]:
            res += cal_subtrack(sub_track)
            sub_track = []
            sub_track.append(area)
            print("Not enter here")
        else:
            for j in range(len(sub_track)):
                x = sub_track[j]
                l = min(x[0], area[0])
                r = max(x[1], area[1])
                olap = r-l+1
                sum2 = (x[1]-x[0]+1) + (area[1]-area[0]+1)
                if sum2 >= olap:
                    sub_track[j][0] = l
                    sub_track[j][1] = r
                    break

                if j == len(sub_track) - 1:
                    sub_track.append(area)
            
        if i==k-1:
            #print(sub_track)
            res+=cal_subtrack(sub_track)
    return m*n - res

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)
    print(result)
