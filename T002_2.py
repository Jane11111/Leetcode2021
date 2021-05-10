# -*- coding: utf-8 -*-
# @Time    : 2021-04-18 21:25
# @Author  : zxl
# @FileName: T002_2.py



import sys

def solveAll(s,t):
    m = len(s)
    n = len(t)
    dp = []
    for i in range(m+1):
        dp.append([0 for j in range(n+1)])

    for j in range(n+1):
        dp[m][j] = n-j
    for i in range(m+1):
        dp[i][n] = 0

    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if s[i]<t[j]:
                dp[i][j] = m-i+n-j
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j+1])
    return dp



if __name__ == "__main__":
    # 读取第一行的n
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())

    dp = solveAll(s,t)
    for k in range(n):
        line = sys.stdin.readline()
        i,j = line.split()
        i = int(i)
        j = int(j)
        ans = dp[i-1][j-1]
        print(ans)
