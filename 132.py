# -*- coding: utf-8 -*-
# @Time    : 2021-06-15 16:58
# @Author  : zxl
# @FileName: 132.py




class Solution:
    def minCut(self, s: str) -> int:


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
                    dp[i][j] = dp[i+1][j-1] if j-i>=2 else True

        arr = [0 for i in range(n)]

        for i in range(1,n):

            if dp[0][i]:
                arr[i] = 0
                continue
            min_val = float('inf')

            for j in range(i+1):
                if dp[j][i]:
                    min_val = min(min_val,1+arr[j-1])
            arr[i] = min_val
        return arr[-1]
