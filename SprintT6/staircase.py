import math 
import os 
import random 
import re
import sys 

def staircase(n):
    for i in range(n):
        print(" " * (n-1-i), end='')
        print("#" * (i + 1))
    
if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)
