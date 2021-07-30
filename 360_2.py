# -*- coding: utf-8 -*-
# @Time    : 2021-07-29 20:38
# @Author  : zxl
# @FileName: 360_2.py


import sys

def solve(s ):

    n = len(s)

    dp = []
    for i in range(n):
        dp.append([False for j in range(n)])
        dp[i][i] = True


    for l in range(2,n+1):
        for i in range(n):
            j = i+l-1
            if j>=n:
                break
            if s[i] == s[j]:
                dp[i][j] = True if (j-i<2 or dp[i+1][j-1] ) else False

    arr = []
    for i in range(n):
        arr.append([0 for j in range(n)])

    dic = {'1':[100,120],'2':[200,350],'3':[360,200],'4':[220,320]}

    for l in range(2,n+1):
        for i in range(n):
            j = i+l-1
            if j>=n:
                break
            if dp[i][j]:
                continue

            arr[i][j] = min(arr[i][j-1]+dic[s[j]][1],
                           arr[i][j-1]+dic[s[j]][0],
                           arr[i+1][j]+dic[s[i]][1],
                           arr[i+1][j]+dic[s[i]][0])

    return arr[0][-1]



if __name__ == '__main__':

    s = sys.stdin.readline().strip()
    # s = '12322'
    num = solve(s )
    print(num)