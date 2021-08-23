# -*- coding: utf-8 -*-
# @Time    : 2021-08-18 19:04
# @Author  : zxl
# @FileName: Huawei01.py

import sys

def solve(X,N,lst):
    dp = []
    for i in range(X+1):
        dp.append([0 for j in range(N+1)])

    for i in range(1,X+1):
        for j in range(1,N+1):
            p,a,s = lst[j-1]
            v = dp[i][j-1]
            for k in range(1,a+1):
                if k*p>i:
                    break
                v = max(v,dp[i-k*p][j-1]+s*k)
            dp[i][j] = v

    return dp[-1][-1]

if __name__ == "__main__":
    line = sys.stdin.readline().strip()

    X,N = list(map(int, line.split()))

    lst = []
    for i in range(N):
        line = sys.stdin.readline().strip()

        arr = list(map(int, line.split()))
        lst.append(arr)

    ans = solve(X,N,lst)
    print(ans)