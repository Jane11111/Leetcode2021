# -*- coding: utf-8 -*-
# @Time    : 2021-08-21 15:35
# @Author  : zxl
# @FileName: Nest04.py

import sys

def solve(arr):

    n = len(arr)
    l2r = [1 for i in range(n)]
    r2l = [1 for i in range(n)]

    min_idx = 0
    for i in range(n):
        if arr[i]<arr[min_idx]:
            min_idx = i

    for num in range(min_idx+1,min_idx+n):
        i = num%n
        ni = i-1
        if arr[i]>arr[ni]:
            l2r[i] = l2r[ni]+1
    for num in range(min_idx-1,min_idx-n):
        # if arr[i] == arr[i+1]:
        #     r2l[i] = r2l[i+1]
        i = num
        ni = i+1
        if arr[i]>arr[ni]:
            r2l[i] = r2l[ni]+1
    ans = 0
    for i in range(n):
        ans += max(l2r[i],r2l[i])
    return ans

if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    arr = list(map(int, line.split()))

    ans = solve(arr)
    print(ans)
