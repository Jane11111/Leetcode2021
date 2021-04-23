# -*- coding: utf-8 -*-
# @Time    : 2021-04-23 09:57
# @Author  : zxl
# @FileName: Offer047.py


class Solution:
    def maxValue(self, grid ) :

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0

        for i in range(1,m):
            grid[i][0] += grid[i-1][0]
        for j in range(1,n):
            grid[0][j] += grid[0][j-1]

        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = max(grid[i-1][j],grid[i][j-1])+grid[i][j]

        return grid[m-1][n-1]
