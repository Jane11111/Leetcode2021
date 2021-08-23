# -*- coding: utf-8 -*-
# @Time    : 2021-08-08 10:29
# @Author  : zxl
# @FileName: MeiTuan03.py

import sys


def biInsert(lst,num):
    if len(lst) == 0:
        lst.append(num)
        return 0
    if lst[0]>=num:
        lst.insert(0,num)
        return 0
    # elif lst[0] == num:
    #     return 0
    if num>lst[-1]:
        lst.append(num)
        return lst[-2]

    l = 0
    h = len(lst)-1
    while l<h:
        m = (l+h)//2
        if lst[m]<num:
            l = m+1
        else:
            h = m
    # if lst[l] == num:
    #     return lst[l-1]
    lst.insert(l,num)
    return lst[l-1]


def solve(arr):

    ans = 0
    lst = []
    for i in range(len(arr)):
        max_val = biInsert(lst,arr[i])
        ans += max_val*(i+1)
    return ans


if __name__ == "__main__":


    N = sys.stdin.readline().strip()
    line = sys.stdin.readline().strip()
    arr = list(map(int, line.split()))

    ans = solve(arr)
    print(ans)
