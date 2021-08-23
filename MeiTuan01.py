# -*- coding: utf-8 -*-
# @Time    : 2021-08-08 10:08
# @Author  : zxl
# @FileName: MeiTuan01.py

import sys

def solve(arr,n,k):

    arr.sort()

    if k == 0:
        return True,1
    num = arr[k-1]+1
    if num>n:
        return False,-1
    if k<n and arr[k] == arr[k-1]:
        return False,-1
    return True,num

if __name__ == "__main__":


    T = sys.stdin.readline().strip()
    T = int(T)

    while T:

        line = sys.stdin.readline().strip()
        n,k = list(map(int, line.split()))
        line = sys.stdin.readline().strip()
        arr = list(map(int, line.split()))

        f,num = solve(arr,n,k)
        if f:
            print('YES')
            print(num)
        else:
            print('NO')

        T-=1
