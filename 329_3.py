# -*- coding: utf-8 -*-
# @Time    : 2021-05-30 17:08
# @Author  : zxl
# @FileName: 329_3.py


class Solution:

    def longestIncreasingPath(self, matrix) -> int:


        m = len(matrix)
        n = len(matrix[0])

        outdegree = []
        for i in range(m):
            outdegree.append([0 for j in range(n)])

        for i in range(m):
            for j in range(n):
                for x,y in [[i-1,j],[i,j-1],[i+1,j],[i,j+1]]:
                    if x>=0 and x<m and y>=0 and y<n and matrix[x][y]>matrix[i][j]:
                        outdegree[i][j]+=1

        queue = []
        for i in range(m):
            for j in range(n):
                if outdegree[i][j] == 0:
                    queue.append([i,j])
        ans = 0
        while len(queue)>0:
            ans +=1
            l = len(queue)
            while l:
                l-=1
                i,j = queue.pop(0)
                for x,y in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
                    if x>=0 and x<m and y>=0 and y<n and matrix[x][y]<matrix[i][j] :
                        outdegree[x][y]-=1
                        if outdegree[x][y] == 0:
                            queue.append([x,y])
        return ans
