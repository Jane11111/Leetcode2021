# -*- coding: utf-8 -*-
# @Time    : 2021-05-21 14:55
# @Author  : zxl
# @FileName: 1143.py



class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:


        m = len(text1)
        n = len(text2)
        dp = []
        for i in range (m+1 ):
            dp.append([0 for i in range(n +1)])

        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[m][n]
