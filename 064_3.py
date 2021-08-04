# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 14:27
# @Author  : zxl
# @FileName: 064_3.py



class Solution:
    def minPathSum(self, grid ) -> int:

        m = len(grid)
        n = len(grid[0])



        for i in range(1,m):

            grid[i][0] += grid[i-1][0]
        for j in range(1,n):
            grid[0][j] += grid[0][j-1]

        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        return grid[m-1][n-1]



