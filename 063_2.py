# -*- coding: utf-8 -*-
# @Time    : 2021-05-16 15:40
# @Author  : zxl
# @FileName: 063_2.py



class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:


        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = []
        for i in range(m):
            dp.append([1 for j in range(n)])
        i = 0
        while i<m:
            if obstacleGrid[i][0] == 1:
                for j in range(i,m):
                    dp[i][0] = 0
                break
            else:
                i+=1
        j = 0
        while j<n:
            if obstacleGrid[0][j] == 1:
                for i in range(j,n):
                    dp[0][i] = 0
                break
            else:
                j+=1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


