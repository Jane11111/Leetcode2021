# -*- coding: utf-8 -*-
# @Time    : 2021-08-07 10:28
# @Author  : zxl
# @FileName: Yi01.py


def solve(arr):

    l = 0
    h = len(arr)-1

    while l<h:

        m = (l+h)//2

        m1 = m+1
        while m1<h and arr[m1] == arr[m]:
            m1+=1

        if arr[m1]>arr[h]:
            l = m1
        else:
            if arr[m]<=arr[m1]:
                h = m
            else:
                l = m1
    return arr[l]

arr = [1,1,3,4,5]
ans = solve(arr)
print(ans)
