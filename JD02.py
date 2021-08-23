# -*- coding: utf-8 -*-
# @Time    : 2021-08-21 19:29
# @Author  : zxl
# @FileName: JD02.py


import sys


def recSolve(n,arr,idx,dic):
    if n == 0:
        return 0

    if idx == len(arr): # 无法分割
        return -1
    if n in dic and idx in dic[n]:
        return dic[n][idx]

    num = arr[idx]
    ans = -1
    for i in range(n//num+1):

        if num*i>n:
            break
        left_cut = recSolve(n-i*num,arr,idx+1,dic)
        if left_cut == -1:
            continue

        ans = max(ans,i+left_cut)
    if n not in dic:
        dic[n] = {}
    dic[n][idx] = ans
    return ans


def solve(n,arr):
    ans = recSolve(n,arr,0,{})
    return ans



if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    arr = list(map(int, line.split()))

    ans = solve(arr[0],arr[1:])
    print(ans)
