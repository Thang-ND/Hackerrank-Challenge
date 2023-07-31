#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countLuck' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY matrix
#  2. INTEGER k
#
count = 0

def countLuck(matrix, k):
    global count 
    count = 0

    xi = [0, 0, 1, -1]
    yi = [1, -1, 0, 0]
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        matrix[i] = list(matrix[i])

    def neighbor(i, j, matrix):
        temp = 0
        for x, y in zip(xi, yi):
            if 0 <= i+x < n and 0 <= j+y < m and matrix[i+x][j+y] != 'X':
                temp += 1

        return temp
    
    def dfs(i, j, matrix):
        global count
        if matrix[i][j] == '*':
            return True
        flag = False
        matrix[i][j] = 'v'

        for x, y in zip(xi, yi):
            if 0 <= i+x < n and 0 <= j+y < m and matrix[i+x][j+y] in ['*', '.']:
                flag = dfs(i+x, j+y, matrix)
                if flag == True:
                    count += 1 if neighbor(i, j, matrix) > 2 else 0
                    #matrix[i][j] = '0'
                    return flag
                
        matrix[i][j] = '.'
        return flag 
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'M':
                flag = dfs(i, j, matrix)
                count -= 1 if neighbor(i, j, matrix) > 2 else 0
                count += 1 if neighbor(i, j, matrix) > 1 else 0
                break

    if flag == True and count == k:
        return "Impressed"
    return "Oops!"


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input().strip())

        result = countLuck(matrix, k)
        print(result)

