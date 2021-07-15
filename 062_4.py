# -*- coding: utf-8 -*-
# @Time    : 2021-07-14 15:57
# @Author  : zxl
# @FileName: 062_4.py



class Solution:
    def uniquePaths(self, m: int, n: int) -> int:


        dp = []
        for i in range(m+1):
            dp.append([0 for i in range(n+1)])

        dp[1][1] = 1

        for i in range(1,m+1):
            for j in range(1,n+1):
                if i == 1 and j  == 1:
                    continue
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m][n]
