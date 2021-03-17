# -*- coding: utf-8 -*-
# @Time    : 2021-03-13 22:27
# @Author  : zxl
# @FileName: 200.py

class Solution(object):

    def getNeighbors(self,x,y,m,n):
        neighbors = []
        if x-1 >= 0:
            neighbors.append([x-1,y])
        if x+1 <= m-1:
            neighbors.append([x+1,y])
        if y-1 >= 0:
            neighbors.append([x,y-1])
        if y+1 <= n-1:
            neighbors.append([x,y+1])
        return neighbors

    def dfs(self,grid,x,y,m,n):

        grid[x][y] = '0'
        neighbors = self.getNeighbors(x,y,m,n)
        for neighbor in neighbors:
            if grid[neighbor[0]][neighbor[1]] == '1':
                self.dfs(grid,neighbor[0],neighbor[1],m,n)




    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    self.dfs(grid,i,j,m,n)
        return ans

obj = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
ans = obj.numIslands(grid)
print(ans)