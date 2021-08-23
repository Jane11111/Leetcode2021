# -*- coding: utf-8 -*-
# @Time    : 2021-08-18 19:16
# @Author  : zxl
# @FileName: Huawei02.py


import sys


def recSolve(lst,idx,left,dic):

    if left == 0:
        return 1

    if idx == len(lst):
        return 0

    if idx in dic and left in dic[idx] :
        return dic[idx][left]
    if idx not in dic:
        dic[idx] = {}

    n1 = recSolve(lst,idx+1,left,dic)
    n2 = recSolve(lst,idx+1,left-lst[idx],dic)

    dic[idx][left] = n1+n2

    return n1+n2


def solve(X,M,lst):

    ans = recSolve(lst,0,X,{})
    if ans == 0:
        return -1
    return ans


if __name__ == '__main__':
    line = sys.stdin.readline().strip()

    X, M = list(map(int, line.split()))

    line = sys.stdin.readline().strip()

    lst = list(map(int, line.split()))

    ans = solve(X,M,lst)
    print(ans)
