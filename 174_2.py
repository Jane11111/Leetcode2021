# -*- coding: utf-8 -*-
# @Time    : 2021-07-05 17:04
# @Author  : zxl
# @FileName: 174_2.py



class Solution:
    def calculateMinimumHP(self, dungeon ) -> int:

        m = len(dungeon)
        n = len(dungeon[0])

        dp = []
        for i in range(m+1):
            dp.append([float('inf') for j in range(n+1)])

        if dungeon[m-1][n-1]<=0:
            dp[m-1][n-1] = abs(dungeon[m-1][n-1])+1
        else:
            dp[m-1][n-1] = 1

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j == n-1:
                    continue
                h = min(dp[i+1][j],dp[i][j+1])

                if dungeon[i][j]<=0:
                    dp[i][j] = abs(dungeon[i][j])+h
                else:
                    if dungeon[i][j]>=h:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = abs(dungeon[i][j]-h)
        return int(dp[0][0])