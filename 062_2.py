# -*- coding: utf-8 -*-
# @Time    : 2021-05-16 15:16
# @Author  : zxl
# @FileName: 062_2.py


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = []
        for i in range(m):
            dp.append([1 for i in range(n)])

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]

        return dp[m-1][n-1]