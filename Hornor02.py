# -*- coding: utf-8 -*-
# @Time    : 2021-08-10 18:37
# @Author  : zxl
# @FileName: Hornor02.py

import sys

def quicksort(arr,i,j):
    if i>=j:
        return

    r = partition(arr,i,j)
    quicksort(arr,i,r-1)
    quicksort(arr,r+1,j)

def partition(arr,i,j):

    num = arr[j]
    p = i-1
    for k in range(i,j):
        if arr[k]+num>num+arr[k]:
            arr[p+1],arr[k] = arr[k],arr[p+1]
            p+=1

    arr[p+1],arr[j] = arr[j],arr[p+1]
    return p+1

def solve(arr):

    quicksort(arr,0,len(arr)-1)
    return ''.join(arr)



if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    arr = list(map(str, line.split()))
    ans = solve(arr)
    print(ans)