# -*- coding: utf-8 -*-
# @Time    : 2021-06-15 21:49
# @Author  : zxl
# @FileName: 097_2.py



class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:


        m = len(s1)
        n = len(s2)
        if m+n != len(s3):
            return False
        dp = []
        for i in range(m+1):
            dp.append([False for i in range(n+1)])

        dp[0][0] = True
        for i in range(1,m+1):
            dp[i][0] = (s1[:i] == s3[:i])

        for j in range(1,n+1):
            dp[0][j] = (s2[:j] == s3[:j])

        for i in range(1,m+1):
            for j in range(1,n+1):

                dp[i][j] = (dp[i][j-1] and s2[j-1]==s3[i+j-1]) or(dp[i-1][j] and s1[i-1] == s3[i+j-1])
        return dp[m][n]