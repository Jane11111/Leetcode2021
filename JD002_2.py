# -*- coding: utf-8 -*-
# @Time    : 2021-04-24 20:01
# @Author  : zxl
# @FileName: JD002_2.py


import sys

def solve(n):

    dp= [1 for i in range(n+1)]
    dp[0] = 1
    for i in range(3,n+1):
        dp[i] = dp[i-1]+dp[i-3]
    return dp[n]



if __name__ == "__main__":
    # 读取第一行的n
    n = sys.stdin.readline().strip()
    n = int(n)

    used = {i:False for i in range(1,n)}
    used[0] = True
    used[-1] = True
    used[-2] = True
    used[n] = True
    used[n+1] = True
    used[n+2] = True
    num = solve(n )
    print(num)
