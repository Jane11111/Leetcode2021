# -*- coding: utf-8 -*-
# @Time    : 2021-05-30 14:44
# @Author  : zxl
# @FileName: 329_2.py



class Solution:

    def dfs(self, i,j,memo,matrix,m,n):

        if memo[i][j] != 0:
            return memo[i][j]
        ans = 1
        for x,y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
            if x>=0 and x<m and y>=0 and y<n and matrix[x][y]>matrix[i][j]:
                ans = max(ans,1+self.dfs(x,y,memo,matrix,m,n))
        memo[i][j] = ans
        return ans

    def longestIncreasingPath(self, matrix ) -> int:


        m = len(matrix)
        n = len(matrix[0])

        memo = []
        for i in range(m):
            memo.append([0 for j in range(n)])
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans,self.dfs(i,j,memo,matrix,m,n))
        return ans

