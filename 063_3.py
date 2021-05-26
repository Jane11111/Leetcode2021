# -*- coding: utf-8 -*-
# @Time    : 2021-05-16 15:49
# @Author  : zxl
# @FileName: 063_3.py



class Solution:

    def memorizeDFS(self,i,j,m,n,visited ):
        if i>=m or j>=n:
            return 0
        if visited[i][j]!=-1:
            return visited[i][j]
        if i==m-1 and j==n-1:
            return 1

        visited[i][j] = 0
        n1 = self.memorizeDFS(i+1,j,m,n,visited )
        n2 = self.memorizeDFS(i,j+1,m,n,visited)
        visited[i][j] = n1+n2
        return n1+n2

    def uniquePathsWithObstacles(self, obstacleGrid) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        visited = []
        for i in range(m):
            visited.append([-1 for j in range(n)])
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    visited[i][j] = 0
        n = self.memorizeDFS(0,0,m,n,visited)
        return n




