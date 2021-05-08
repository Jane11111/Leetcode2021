# -*- coding: utf-8 -*-
# @Time    : 2021-05-08 10:42
# @Author  : zxl
# @FileName: 072_2.py



class Solution:
    def minDistance(self, word1: str, word2: str) -> int:


        m = len(word1)
        n = len(word2)

        dp = []
        for i in range(m+1):
            dp.append([0 for j in range(n+1)])

        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j


        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1])

                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i][j],dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i][j],1+dp[i-1][j-1])

        return dp[m][n]