# -*- coding: utf-8 -*-
# @Time    : 2021-05-08 21:21
# @Author  : zxl
# @FileName: 064_2.py



class Solution:
    def minPathSum(self, grid ) :

        m = len(grid)
        n = len(grid[0])

        for i in range(1,m):
            grid[i][0] += grid[i-1][0]
        for j in range(1,n):
            grid[0][j] += grid[0][j-1]

        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += min(grid[i][j-1],grid[i-1][j])
        return grid[m-1][n-1]




obj = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
ans = obj.minPathSum(grid)
print(ans)

