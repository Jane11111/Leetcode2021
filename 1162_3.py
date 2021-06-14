# -*- coding: utf-8 -*-
# @Time    : 2021-06-10 20:21
# @Author  : zxl
# @FileName: 1162_3.py


class Solution:

    def bfs(self,x,y,grid,m,n):


        if grid[x][y] == 1:
            return 0
        visited = []
        for i in range(m):
            visited.append([False for j in range(n)])
        st = [[x,y]]
        dis = [0]
        visited[x][y] = True
        while len(st)>0:
            x,y = st.pop(0)
            d = dis.pop(0)
            if grid[x][y] == 1:
                return d
            for i,j in [[x-1,y],[x,y-1],[x+1,y],[x,y+1]]:
                if i>=0 and i<m and j>=0 and j<n:

                    if not visited[i][j]:
                        st.append([i,j])
                        dis.append(d+1)
                        visited[i][j] = True
        return float('-inf')




    def maxDistance(self, grid) -> int:

        m = len(grid)
        n = len(grid[0])
        ans = float('-inf')

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j ]== 1:
                    count+=1
        if count == 0 or count == m*n:
            return -1


        for i in range(m):
            for j in range(n):
                d = self.bfs(i,j,grid,m,n)
                ans = max(ans,d)
        if ans == float('-inf'):
            return -1
        return ans





