import sys

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_val = max(arr)
    res = -sys.maxsize
    for i in range(len(arr)):
        if arr[i] != max_val and arr[i] > res:
            res = arr[i]
            
    print(res)
