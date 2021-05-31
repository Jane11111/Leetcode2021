# -*- coding: utf-8 -*-
# @Time    : 2021-05-30 14:27
# @Author  : zxl
# @FileName: 329.py

class Solution:
    def longestIncreasingPath(self, matrix ) -> int:


        lst = set([])
        m = len(matrix)
        n = len(matrix[0])
        dic = {}
        for i in range(m):
            for j in range(n):
                lst.add(matrix[i][j])
                if matrix[i][j] not in dic:
                    dic[matrix[i][j]] = []
                dic[matrix[i][j]].append([i,j])

        lst = list(lst)
        lst.sort()
        len_matrix = []
        for i in range(m):
            len_matrix.append([-1 for j in range(n)])

        ans = 0

        for i in range(len(lst)-1,-1,-1):
            v = lst[i]
            pos_lst = dic[v]
            for x,y in pos_lst:

                max_len = 1
                for x1,y1 in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
                    if x1<0 or x1>=m or y1<0 or y1>=n:
                        continue
                    if matrix[x1][y1]>v and len_matrix[x1][y1]+1>max_len :
                        max_len = len_matrix[x1][y1]+1
                len_matrix[x][y] = max_len
                ans = max(ans,max_len)
        return ans






