# -*- coding: utf-8 -*-
# @Time    : 2021-06-16 13:57
# @Author  : zxl
# @FileName: 375.py

class Solution:
    def getMoneyAmount(self, n: int) -> int:


        dp = []
        for i in range(n+1):
            dp.append([0 for i in range(n+1)])


        for l in range(2,n+1):
            for i in range(1,n+1):
                j = i+l-1
                if j>n:
                    break
                min_val = float('inf')
                for k in range(i,j+1):
                    v = k

                    if k-1>i and k+1<j:
                        v+= max(dp[i][k-1],dp[k+1][j])
                    elif k-1>i:
                        v+=dp[i][k-1]
                    elif k+1<j:
                        v+=dp[k+1][j]
                    min_val = min(min_val,v)
                dp[i][j] = min_val
        return dp[1][n]