# -*- coding: utf-8 -*-
# @Time    : 2021-07-26 20:48
# @Author  : zxl
# @FileName: 329_4.py



class Solution:
    def longestIncreasingPath(self, matrix ) -> int:


        dic = {}
        m = len(matrix)
        n = len(matrix[0])
        lst = []

        for i in range(m):
            for j in range(n):

                num = matrix[i][j]
                if num not in dic:
                    dic[num] = []
                    lst.append(num)
                dic[num].append([i,j])
        lst.sort(reverse = True)

        mat = []
        for i in range(m):
            mat.append([0 for j in range(n)])

        ans = 0
        for num in lst:

            for x,y in dic[num]:

                val = 1
                for nx,ny in [[x-1,y],[x,y-1],[x+1,y],[x,y+1]]:
                    if nx>=0 and nx<m and ny>=0 and ny<n and matrix[nx][ny] > matrix[x][y]:
                        val = max(val,mat[nx][ny]+1)
                mat[x][y] = val
                ans = max(ans,mat[x][y])
        return ans







