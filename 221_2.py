# -*- coding: utf-8 -*-
# @Time    : 2021-05-26 21:49
# @Author  : zxl
# @FileName: 221_2.py



class Solution:


    def maximalSquare(self, matrix ) -> int:


        m = len(matrix)
        n = len(matrix[0])
        max_len = 0
        for i in range(m):
            matrix[i][0] = int(matrix[i][0])
            max_len = max(max_len,matrix[i][0])
        for j in range(n):
            matrix[0][j] = int(matrix[0][j])
            max_len = max(max_len,matrix[0][j])

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]== '0':
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = min(matrix[i-1][j],matrix[i-1][j-1],matrix[i][j-1])+1
                    max_len = max(matrix[i][j],max_len)
        return max_len**2


