# -*- coding: utf-8 -*-
# @Time    : 2021-05-08 16:14
# @Author  : zxl
# @FileName: 200_2.py




class Solution:

    def dfs(self,grid,i,j,m,n):

        grid[i][j] = '-1'

        for x,y in [[i-1,j],[i,j-1],[i,j+1],[i+1,j]]:
            if x>=0 and x<m and y>=0 and y<n and grid[x][y] == '1' :
                self.dfs(grid,x,y,m,n)



    def numIslands(self, grid ) :

        m = len(grid)
        n = len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count+=1
                    self.dfs(grid,i,j,m,n)
        return count


obj = Solution()
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
ans = obj.numIslands(grid)
print(ans)

