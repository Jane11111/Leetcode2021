# -*- coding: utf-8 -*-
# @Time    : 2021-05-12 11:04
# @Author  : zxl
# @FileName: 659_2.py


class Solution:

    def dfs(self,grid,i,j,m,n):

        grid[i][j] = -1
        count = 1

        neighbors = []
        if i+1<m:
            neighbors.append([i+1,j])
        if j+1<n:
            neighbors.append([i,j+1])
        if i-1>=0:
            neighbors.append([i-1,j])
        if j-1>=0:
            neighbors.append([i,j-1])
        for x,y in neighbors:
            if grid[x][y] == 1:
                count+=self.dfs(grid,x,y,m,n)
        return count

    def maxAreaOfIsland(self, grid ) -> int:

        m = len(grid)
        n = len(grid[0])

        max_count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = self.dfs(grid,i,j,m,n)
                    max_count = max(max_count,count)
        return max_count