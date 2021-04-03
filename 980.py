# -*- coding: utf-8 -*-
# @Time    : 2021-03-26 14:14
# @Author  : zxl
# @FileName: 980.py


class Solution(object):

    def getNeighbors(self,i,j,m,n):
        neighbors = []
        if j-1>=0:
            neighbors.append([i,j-1])
        if j+1<n:
            neighbors.append([i,j+1])
        if i-1>=0:
            neighbors.append([i-1,j])
        if i+1<m:
            neighbors.append([i+1,j])
        return neighbors


    def recursiveWalk(self,grid,i,j,path_num,total_count):

        if grid[i][j] == 2 and path_num == total_count:
            return 1
        elif grid[i][j] == 2 and path_num != total_count:
            return 0

        count = 0

        num = grid[i][j]
        grid[i][j] = 3

        m = len(grid)
        n = len(grid[0])
        neighbors = self.getNeighbors(i,j,m,n)
        for x,y in neighbors:
            if grid[x][y] == 0:
                count += self.recursiveWalk(grid,x,y,path_num+1,total_count)
            elif grid[x][y] == 2:
                count += self.recursiveWalk(grid, x, y, path_num, total_count)

        grid[i][j] = num
        return count


    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])
        total_count = 0
        s = 0
        e = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    total_count+=1
                elif grid[i][j] == 1:
                    s = i
                    e = j
        count = self.recursiveWalk(grid,s,e,0,total_count)
        return count

obj = Solution()
grid = [[0,1],[2,0]]
count = obj.uniquePathsIII(grid)
print(count)
