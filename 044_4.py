# -*- coding: utf-8 -*-
# @Time    : 2021-07-12 21:51
# @Author  : zxl
# @FileName: 044_4.py






class Solution:

    def isMatch(self, s: str, p: str) -> bool:


        m = len(p)
        n = len(s)

        dp = []
        for i in range(m+1):
            dp.append([False for j in range(n+1)])

        dp[0][0] = True

        for i in range(1,m+1):
            dp[i][0] = p[i-1] == '*' and dp[i-1][0]


        for i in range(1,m+1):
            for j in range(1,n+1):

                if p[i-1] == '*':

                    dp[i][j] = dp[i-1][j] or dp[i-1][j-1] or dp[i][j-1]
                elif p[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = p[i-1] == s[j-1] and dp[i-1][j-1]
        return dp[m][n]
