# -*- coding: utf-8 -*-
# @Time    : 2021-06-25 11:42
# @Author  : zxl
# @FileName: 417_2.py



class Solution:

    def dfs(self,i,j,m,n,heights,visited,mat,flag):



        if visited[i][j]:
            return
        visited[i][j] = True

        d = [[0,1],[0,-1],[1,0],[-1,0]]

        if flag:
            mat[i][j] = 1
        else:
            if mat[i][j] == 1:
                mat[i][j] = 2

        for x,y in d:
            if x+i>=0 and x+i<m and y+j>=0 and y+j<n and heights[x+i][y+j]>=heights[i][j]:
                self.dfs(x+i,j+y,m,n,heights,visited,mat,flag)


    def pacificAtlantic(self, heights):

        m = len(heights)
        n = len(heights[0])

        visited1 = []
        visited2 = []
        visited3 = []
        visited4 = []
        mat = []
        for i in range(m):
            visited1.append([False for j in range(n)])
            visited2.append([False for j in range(n)])
            visited3.append([False for j in range(n)])
            visited4.append([False for j in range(n)])
            mat.append([0 for j in range(n)])


        for i in range(m):
            self.dfs(i,0,m,n,heights,visited1,mat,True)


        for j in range(n):
            self.dfs(0,j,m,n,heights,visited2,mat,True)

        for i in range(m):
            self.dfs(i,n-1,m,n,heights,visited3,mat,False)

        for j in range(n):
            self.dfs(m-1,j,m,n,heights,visited4,mat,False)

        ans = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 2:
                    ans.append([i,j])
        return ans


obj = Solution()
heights = [[1,1],[1,1],[1,1]]
ans = obj.pacificAtlantic(heights)
